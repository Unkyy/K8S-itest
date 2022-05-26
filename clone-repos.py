from git import Git
import subprocess
import os
from time  import sleep

repos = [
    "https://github.com/Unkyy/itest-software.git",
    "https://github.com/Unkyy/computer-vision-api.git"
]

for repo in repos:
    Git().clone(repo)
