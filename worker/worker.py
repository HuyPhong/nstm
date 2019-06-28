from kazoo.client import KazooClient
from kazoo.exceptions import NodeExistsException
import logging
import logging.handlers
import time
import platform
import services_pb2
import grpc
import subprocess
import os
import git
import shutil
import json
from google.cloud import storage
import virtualenv
from pip._internal import main as pipmain
import os
import zipfile
from multiprocessing import Process


import services_pb2_grpc

zk = KazooClient(hosts="127.0.0.1:2181")
zk.start()

log_server = '127.0.0.1:8001'
log_path = '/'
tasks = {}
clone_dir = "/home/phong/WorkSpace/nstm/worker/tmp"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/phong/Downloads/NextSmarty-75687328ad51.json"
class Task:

    def __init__(self, task_descr):
        self._log_server = log_server
        self._log_path = log_path
        self.task_descr = task_descr
        self.logger = logging.getLogger(task_descr.taskName)
        self.logger.setLevel(logging.INFO)
        self._path = clone_dir + '/' + task_descr.taskName
        ch = logging.handlers.HTTPHandler(self._log_server, "/", method='GET')

        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        tasks[task_descr.taskName] = {}

    def setup_environment(self):
        venv_dir = os.path.join(os.path.expanduser(self._path), ".venv")
        virtualenv.create_environment(venv_dir)
        execfile(os.path.join(venv_dir, "bin", "activate_this.py"))
        #pipmain(["install", "--prefix", venv_dir, "kafka"])

    def download_from_cloud(self):
        if os.path.isdir(self._path):
            shutil.rmtree(self._path)
        os.mkdir(self._path)
        remote_uri = self.task_descr.remoteUri
        client = storage.Client()
        bucket_name = remote_uri.split('//')[1].split('/')[0]
        blob_name = remote_uri.split('//')[1].split('/')[1]
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(self._path + '/' + 'downloaded.zip')

    def unzip(self):
        zip_ref = zipfile.ZipFile(self._path + '/' + 'downloaded.zip', 'r')
        zip_ref.extractall(self._path)
        os.rename()
        zip_ref.close()

    def run(self):
        p = Process(target=self.execute())

    def execute(self):
        self.download_from_cloud()
        self.unzip()
        print("clone repo")
        '''
        if os.path.isdir(self._path):
            shutil.rmtree(self._path)
        git.Repo.clone_from(self.task_descr.gitUri, self._path)
        '''
        print("done clone")
        '''
        os.system('virtualenv -p ./venv/bin/python ' + self._path + '/venv')
        os.system(' realpath ./venv/lib/python2.7/site-packages >' + self._path + '/venv/lib/python2.7/site-packages/bash_venv.pth')
        '''
        self.setup_environment()
        process = subprocess.Popen([self._path + "/.venv/bin/python", self._path + '/code/run.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        def check_io():
            while True:
                output = process.stdout.readline().decode()
                print(output)
                if output:
                    self.logger.info(output)
                else:
                    break

        # keep checking stdout/stderr until the child exits
        while process.poll() is None:
            check_io()
        print(process.returncode)
        return process.returncode


descr = services_pb2.TaskDescr(taskName='task1', remoteUri='gs://cloudstoragenextmsarty/example-versioning.zip')
task = Task(task_descr=descr)
task.run()
'''

class Worker:
    def __init__(self):
        self.desc = None
        self.gpu = 1;

    def load_hardware(self):
        self.desc = services_pb2.WorkerDesc(ip="127.0.0.1", memory=16000)
        print(platform.machine())

    def remain_resource(self):
        return self.gpu

    def set_id(self, worker_id):
        self.worker_id = worker_id


worker = Worker()
worker.load_hardware()
try:
    zk.create(path="/workers", value="")
    logging.info("znode /workers is created")
except NodeExistsException:
    logging.info("znode /workers is exists")
desc = services_pb2.WorkerDesc(ip="127.0.0.1")

id_d = zk.create(path="/workers/worker-", ephemeral=True, sequence=True, value=worker.desc.SerializeToString()).replace(
    "/workers/", "")
worker.set_id(id_d)
master_desc = services_pb2.MasterDesc()
value, stat = zk.get("/master")
master_desc.ParseFromString(value)
print(master_desc.ip + ":" + str(master_desc.grpcPort))
channel = grpc.insecure_channel(master_desc.ip + ":" + str(master_desc.grpcPort))
stub = services_pb2_grpc.NstmStub(channel)

while True:
    ack = stub.Register(services_pb2.WorkerRegisterRequest(workerId=worker.worker_id))
    if ack.ack == services_pb2.Ack.Value("REGISTER_SUCCESS"):
        logging.info("worker registered successful")
        break;
    time.sleep(1)

respone = stub.PullTask(
    services_pb2.PullTaskRequest(metrics=services_pb2.AvailableResource(gpu=1), workerId=worker.worker_id))
print(services_pb2.Ack.Name(respone.ack))
print(respone.taskDescr)
if respone.ack==services_pb2.PULL_TASK_SUCCESS:
    task = Task(task_descr=respone.taskDescr)
    task.run()

respone_1 = stub.DoneTask(services_pb2.DoneTaskRequest(taskName=respone.taskDescr.taskName, isSuccess=True))


def run_task(task_descr):
    task = Task(task_descr=task_descr)
    task.run()


def take_worker():
    while True:
        if Worker.gpu > 0:
            respone = stub.PullTask(
                services_pb2.PullTaskRequest(metrics=services_pb2.AvailableResource(gpu=1, workerId=worker.worker_id)))
            if respone.ack == services_pb2.PULL_TASK_SUCCESS:
    

'''