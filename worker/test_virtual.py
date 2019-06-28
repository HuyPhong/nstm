import virtualenv
from pip._internal import main as pipmain
import os

# create and activate the virtual environment
venv_dir = os.path.join(os.path.expanduser("~/Downloads"), ".venvtest")
virtualenv.create_environment(venv_dir)
execfile(os.path.join(venv_dir, "bin", "activate_this.py"))

# pip install a package using the venv as a prefix
pipmain(["install", "--prefix", venv_dir, "cassandra-driver"])

