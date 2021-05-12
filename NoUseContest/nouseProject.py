import time
import random
import sys
import webbrowser

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *

#UI 파일 연결하기
form_class = uic.loadUiType("realTT.ui")[0]

class WindowClass(QMainWindow, form_class) :#윈도우 클래스 선언
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    #-----------여기서부터---------------------#
        self.startBTN.clicked.connect(self.btnClick)
        self.gotoYBTN.clicked.connect(self.gotoYClick)
        
    def loadMusicTxt(self): #랜덤 음악 리스트를 반환하는 함수
        mc=open('./source/music.txt','r', encoding='UTF-8')
        mcLine=mc.readlines()
        for i in range(len(mcLine)):
            mcLine[i]=mcLine[i].strip()
        rdIndex=random.randint(0,len(mcLine)-1)
        return mcLine[rdIndex]

    def loadFoodList(self): #랜덤 음식 리스트를 반환하는 함수
        fc=open('./source/food.txt','r', encoding='UTF-8')
        fcLine=fc.readlines()
        for i in range(len(fcLine)):
            fcLine[i]=fcLine[i].strip()
        
        for i in range(len(fcLine)):
            fcLine[i]=fcLine[i].split('/')
            
        fcIndex=random.randint(0,len(fcLine)-1)
        return fcLine[fcIndex]
    
    def btnClick(self): #버튼을 클릭했을 때 
        self.musicLabel.setText(self.loadMusicTxt())
        theFood=self.loadFoodList()
        self.foodLabel.setText("\""+theFood[0]+"\"")
        
        qPixmapVar=QPixmap('./source/foodP/'+theFood[1]).scaled(201,161)
        self.labelImage.setPixmap(QPixmap(qPixmapVar))

    def gotoYClick(self): #'지금 당장 들으러가기'버튼을 눌렀을 때 해당 노래가 아닌 유튜브 링크를 오픈하는 함수
        webbrowser.open(
                "https://www.youtube.com/results?search_query="
                +self.loadMusicTxt())
     #---------------여기까지---------------------#
        

if __name__ == "__main__" :#메인 함수 선언
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    cin>>A
    app.exec_()
