from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/phong/Downloads/NextSmarty-75687328ad51.json"
client = storage.Client()
bucket = client.get_bucket('cloudstoragenextmsarty')
remote_uri = 'gs://cloudstoragenextmsarty/classify/26'
bucket_name = remote_uri.split('//')[1].split('/')[0]
print(bucket_name)
#blob = bucket.blob('nstm/example-versioning.zip')
#blob.download_to_filename('example-versioning.zip')

