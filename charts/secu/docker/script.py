#!/usr/bin/python3.9

import os 

# url=os.environ['URL']
url = "http://wordpress:8888"
print(url)
# nmap="nmap -sS -T4 -p- "+ url
wpscan="wpscan --url "+url

# os.system(nmap)
os.system(wpscan)