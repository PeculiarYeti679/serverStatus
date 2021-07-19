from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import time
import sys

def checkStatus():
    hostsfile=open("hostList.txt", "r")
    outputfile=open("C:/Users/ECY/Projects/serverOnline/output.csv", "w")


    lines=hostsfile.readlines()

    for line in lines:
        response=os.system("ping -c 1 " + line)
        if (response == 0):
            status = line.rstrip() + ",1"
        else:
            status = line.rstrip() + ",0"
        print(status)
        outputfile.write(status + "\n")
    outputfile.close()

while True:
    checkStatus()
    time.sleep(300)


