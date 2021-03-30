import subprocess
import os
import win32api
from functions import *
import json
import threading

FILE_NAME = 'config.json'
with open(FILE_NAME) as f:
    d = json.load(f)
server_url = d['server_url']
driver=d['printer']


def job():
    f = open("status.txt", "r")
    content=f.read()
    if(content!="1"):
        return
    write_file("0")
    print('a')
    if(download_file(server_url)):

        p = subprocess.Popen([r"C:\Program Files\Ghostgum\gsview\gsprint.exe", "file.pdf"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        os.system('C:\Program Files\Ghostgum\gsview\gsprint.exe -printer "{}" "test.pdf"'.format(driver))
        #win32api.ShellExecute('C:\Program Files\Ghostgum\gsview\gsprint.exe -printer "HP LaserJet 3055 PCL6 Class Driver" "test.pdf"')
        win32api.WinExec('C:\Program Files\Ghostgum\gsview\gsprint.exe -printer "{}" "test.pdf"'.format(driver))
        print(stdout)
        print(stderr)
        #delete_file()
    write_file("1")


def printit():
    job()
    threading.Timer(5.0, printit).start()

printit()