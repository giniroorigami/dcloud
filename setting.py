#!/usr/bin/python3
import subprocess

#hostname
subprocess.run(["hostnamectl","set-hostname","ubuntu"],text=True)

#bininstall
subprocess.run(["apt","update","-y"],text=True)
subprocess.run(["apt","install","nmap","-y"],text=True)
subprocess.run(["apt","install","docker.io","-y"],text=True)

#network
subprocess.run("mv /root/dcloud/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml",shell=True,text=True)
subprocess.run(["netplan","apply"],text=True)

#alias
subprocess.run("mv /root/dcloud/.bashrc ~/.bashrc",shell=True,text=True)

#reload
subprocess.run(["reboot"],text=True)
