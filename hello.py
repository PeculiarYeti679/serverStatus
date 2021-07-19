import os
import time

def checkStatus():
    hostsfile=open("hostList.txt", "r")
    outputfile=open("output.txt", "w")


    lines=hostsfile.readlines()

    for line in lines:
        response=os.system("ping -c 1 " + line)
        if (response == 0):
            status = line.rstrip() + " is Reachable"
        else:
            status = line + " is Not reachable"
        print(status)
        outputfile.write(status + "\n")
    outputfile.close()

while True:
    checkStatus()
    time.sleep(30)