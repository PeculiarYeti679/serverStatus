from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import time
import sys
import pandas as pd
import array

''' logFile=open("C:/Users/ECY/Projects/serverOnline/output.csv","r") '''


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Status")
        self.show()
        
 
def offLine():
    df = pd.read_csv("C:/Users/ECY/Projects/serverOnline/output.csv", names=['IP', "Status"])

    #print(df.head())
    df_filtered = df[(df['Status']==0)]
    print(df_filtered)

    ip_address = df_filtered.iloc[:, :1]

    print("Ip: " + ip_address ) 

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())



