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

def offLine():
    df = pd.read_csv("C:/Users/ECY/Projects/serverOnline/output.csv", names=['IP', "Status"])

    #print(df.head())
    df_filtered = df[(df['Status']==0)]
    print(df_filtered)

    ip_address = df_filtered.iloc[:, :1]

    print("Ip: " + ip_address ) 




while True:
    checkStatus()
    offLine()
    time.sleep(300)


