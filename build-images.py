from git import Git
import subprocess
import os
from time  import sleep

repos = [
    "https://github.com/Unkyy/itest-software.git",
    "https://github.com/Unkyy/computer-vision-api.git"
]

for repo in repos:
    reponame = repo.split("/")[-1].split(".")[0]
    sleep(2)
    print(subprocess.run(["pwd"]))
    subprocess.run(["docker build ./"+reponame],shell=True)
    # subprocess.run(["rm "])
    # if os.path.exists(reponame):
    # # removing the file using the os.remove() method
    #     os.remove(reponame)    