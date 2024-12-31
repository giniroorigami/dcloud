#!/usr/bin/python3.10
import subprocess

#ホスト名設定
def hostname(name): 
  return ["hostnamectl","set-hostname",name]

#必要パッケージインストール
def install(bin):
  return ["apt","install","-y",bin]
  
#アップデート
def update():
    return ["apt","update","-y"]

#ネットワーク設定
def network():
  return "mv /root/dcloud/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml"
  
#alias設定
def alias():
  return "mv /root/dcloud/.bashrc ~/.bashrc"

if __name__=="__main__":
  subprocess.run(hostname("ubuntu"),text=True) #ホスト名設定
  subprocess.run(update(),text=True) #ローカルリポジトリアップデート
  subprocess.run(install("bind9"),text=True) #bindの追加
  subprocess.run(install("nmap"),text=True) #nmapの追加
  subprocess.run(network(),shell=True,text=True) #netplan設定の移設
  subprocess.run(alias(),shell=True,text=True) #.bashrcの移設
