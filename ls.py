#!/usr/bin/python3.10

import subprocess

ls = subprocess.run("ls",shell=True,text=True)
print(ls)
