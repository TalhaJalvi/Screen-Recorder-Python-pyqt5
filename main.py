#This Will Grab image from screen
import datetime
import pyautogui
#Numpy for processing image matrices
import numpy as np
import cv2
from win32api import GetSystemMetrics


#Creating Desktop application usin g pyQt5
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
#For setting Icon
from PyQt5.QtGui import QIcon

#Making class first
class WindowExample(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()

        #Setting height and width of window
        self.setGeometry(800,500,500,200)
        self.setWindowTitle('TAJ Screen Recorder')
        self.setWindowIcon(QIcon('icon.png'))
        self.create_buttons()
        #Now to show window
        self.show()

  #Adding button function
    def create_buttons(self):
        btn1 = QPushButton("Click me",self)
        btn1.setText("Start Recording")
        btn1.setIcon(QIcon('icon.png'))
        btn1.setGeometry(300,100,130,50)
        btn1.clicked.connect(self.button_clicked)

    #On click this function will be activated
    def button_clicked(self):
        print("Button is clicked")

        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)

        #Encodingf we used to save video
        fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

        #For creating multiple files using time stamp
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        file_name=f'{time_stamp}.avi'
        captured_video = cv2.VideoWriter(file_name,fourcc,20.0,(width,height))

        #Loop while something happens or key is pressed record video
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)

            #What we are capturing is RGB so our colors get wrong to correct it
            img_final = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            cv2.imshow('Screen Recorder',img_final)
            captured_video.write(img_final)

            #Now to save captured video
            if cv2.waitKey(10) == ord('q'):
                break



app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())









#