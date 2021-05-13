import sys
import webbrowser
import requests
import openpyxl

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#엑셀 파일에서 사용할 상수 선언
FULL_DATE=0; YEAR=1; MONTH=2; DAY=3; MONEY=4;

#PyQt5 designer에서 만든 UI 파일 연결하기
form_class = uic.loadUiType("midtestProjectUI.ui")[0]

class WindowClass(QMainWindow, form_class) :#윈도우 클래스 선언
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
    #-----------여기서부터---------------------#
        self.inputBtn.clicked.connect(self.inputBtnClick)    
    def inputBtnClick(self):
        self.colorBackground(self.degreeInput.value())
        
    def loadData(self): #엑셀에 담겨있는 날짜와 원화 데이터 가져오기 
        excel_file = openpyxl.load_workbook('data.xlsx')
        excel_sheet = excel_file.active

        global date_dict
        global dollar_dict
        date_dict={}
        dollar_dict={}

        for row in excel_sheet.rows:
            date_dict[str(row[FULL_DATE].value)]=[int(row[YEAR].value),int(row[MONTH].value),int(row[DAY].value)]            
            dollar_dict[str(row[FULL_DATE].value)]=float(row[MONEY].value)
        
        excel_file.close()

    def colorBackground(self,data):
        for date in date_dict.keys():
            date=str(date)
            if dollar_dict[date] <= data :
                f=QTextCharFormat()
                f.setBackground(QBrush(QColor(Qt.blue)))
            else :
                f=QtGui.QTextCharFormat()
                f.setBackground(QBrush(QColor(Qt.red)))
            a=[]
            for value in date_dict[date]:
                a.append(value)
            date=QDate(a[0],a[1],a[2])
            self.calendar.setDateTextFormat(date, f)
            #---------------여기까지---------------------#
        

if __name__ == "__main__" :#메인 함수 선언
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.loadData()
    myWindow.show()
    app.exec_()

