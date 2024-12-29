#!/usr/bin/python3
import subprocess

#hostname
subprocess.run(["hostnamectl","set-hostname","ubuntu"],text=True)

#bininstall
subprocess.run(["apt","update","-y"],text=True)
print("update fin")
subprocess.run(["apt","install","nmap","-y"],text=True)
print("nmap install fin")
subprocess.run(["apt","install","docker.io","-y"],text=True)
print("docker install fin")

#network
subprocess.run("mv","/root/dcloud/50-cloud-init.yaml,"/etc/netplan/50-cloud-init.yaml",shell=True,text=True)
subprocess.run(["netplan","apply"],text=True)

#reload
subprocess.run(["reboot"],text=True)
