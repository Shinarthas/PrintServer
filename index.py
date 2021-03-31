import subprocess
import os
import win32api
import  win32print
from functions import *
import json
import threading

FILE_NAME = 'config.json'
with open(FILE_NAME) as f:
    d = json.load(f)
server_url = d['server_url']
driver=d['printer']

GHOSTSCRIPT_PATH = "C:\\ghostscript\\bin\\gswin32.exe"
GSPRINT_PATH = "C:\\gsprint\\gsprint.exe"

def job():
    f = open("status.txt", "r")
    content=f.read()
    if(content!="1"):
        return
    write_file("0")
    print('a')
    if(download_file(server_url)):
        # YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
        currentprinter = win32print.GetDefaultPrinter()

        win32api.ShellExecute(0, 'open', GSPRINT_PATH,
                              '-ghostscript "' + GHOSTSCRIPT_PATH + '" -printer "' + currentprinter + '" "file.pdf"',
                              '.', 0)
        #delete_file()
    write_file("1")


def printit():
    job()
    threading.Timer(5.0, printit).start()

printit()