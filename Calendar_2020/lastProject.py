import tkinter as tk
from tkinter import ttk#for combobox
import time

window=tk.Tk()
window.title('내가 만든 캘린더')
window.geometry('800x650+200+50')

#window 창을 나누는 함수
for i1 in range(14):
    window.columnconfigure(i1,weight=1)
for i2 in range(10):
    window.rowconfigure(i2,weight=1)
    
#요일 먼저 나열
week=['일','월','화','수','목','금','토']
for i in range(7):
    if i==0 or i==6:
        label=tk.Label(window,text=week[i],
                       font='고딕',bg='white',fg='red')
        label.grid(row=2,column=i, sticky='nswe')
    else:
        label=tk.Label(window,text=week[i],
                       font='고딕',bg='white',fg='gray')
        label.grid(row=2,column=i, sticky='nswe')

#캘린더의 달을 입력하는 콤보박스 생성
monthMenu=["1월","2월","3월","4월","5월","6월",
           "7월","8월","9월","10월","11월","12월",]
monthCombo=ttk.Combobox(window,value=monthMenu,
                   font=('고딕',20))
monthCombo.grid(row=1,column=0, columnspan=7)


#오늘의 날짜
monthMenuE=['Jan','Feb','Mar','Apr','May',
            'Jun','Jul','Aug','Sep','Oct','Nov','Dec']
weekE=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
tTime=time.ctime()
tTime=tTime.split()
for w1 in range(12):
    if tTime[1]==monthMenuE[w1]:
        cMonth=monthMenu[w1]+' '
        break

monthCombo.current(w1)
cDay=tTime[2]+'일'
cYear=tTime[4]+'년 '

#오늘의 날짜를 바로 표시하는 라벨
sLabel=tk.Label(window,text=cYear+cMonth+cDay)
sLabel.grid(row=1, column=9,sticky='sewn')

#캘린더 제목 제일 위 부분
label=tk.Label(window,text='Calendar',
               font=('고딕',30),
               bg='gray', fg='white')
label.grid(row=0,column=0,columnspan=14, sticky='nswe')

#날짜에 해당하는 정보 불러오기
def loadDayInfo():
    global tdDate,tdFir,tdSec,tdThi,firC,secC,thiC,theD,tdLine
    td=open('./notes/todo.txt','r',encoding='cp949')
    tdLine=td.readlines()
    tdLines=[]
    for i in range(len(tdLine)):
        tdLines.append(tdLine[i].split('/'))

    tdDate,tdFir,tdSec,tdThi=[],[],[],[]
    firC,secC,thiC=[],[],[]
    for i in range(len(tdLine)):
        if i%4==0:
            tdDate.append(tdLines[i][0].strip())
        elif i%4==1:
            tdFir.append(tdLines[i][0].strip())
            firC.append(tdLines[i][1].strip())
        elif i%4==2:
            tdSec.append(tdLines[i][0].strip())
            secC.append(tdLines[i][1].strip())
        else:
            tdThi.append(tdLines[i][0].strip())
            thiC.append(tdLines[i][1].strip())
                
    date=sLabel.cget('text')
                
    for d in range(0,len(tdDate)):
        if date==tdDate[d]:
            theD=d
            firEn.insert(0,tdFir[theD])
            secEn.insert(0,tdSec[theD])
            thiEn.insert(0,tdThi[theD])
                        
            if firC[theD]=='O':
                chk_var1.set(True)
            else:
                chk_var1.set(False)
            if secC[theD]=='O':
                chk_var2.set(True)
            else:
                chk_var2.set(False)
            if thiC[theD]=='O':
                chk_var3.set(True)
            else:
                chk_var3.set(False)
                            
            break
        else:
            pass

#일정관련 칸을 리셋하는 함수
def deleteDayInfo():
    firEn.delete(0,'end')
    secEn.delete(0,'end')
    thiEn.delete(0,'end')
    chk_var1.set(False)
    chk_var2.set(False)
    chk_var3.set(False)

#달을 선택하면 관련정보를 불러오는 함수 실행
def monthSelect():
    deleteDayInfo()
    mC=monthCombo.get()
    #mC는 사용자가 선택한 달
    for i in range(12):
        if mC==monthMenu[i]:
            monthi=i+1
            break
    a=open('./month/'+str(monthi)+'.txt','r')
    monthFile=a.readlines()

    aboutMonth=monthFile[0]
    aboutMonth=aboutMonth.rstrip()
    aboutMonth=aboutMonth.split(' ')

    #aboutHoliday는 달에 대한 휴일 정보
    aboutHoliday=[]
    for i in monthFile[1:]:
        aboutHoliday.append(i.strip())

    #iday aboutMonth[1]을 이용한 달 시작 요일 인덱스번호
    realN=0
    
    for i in range(len(week)):
        if str(i)==aboutMonth[1]:
            iday=i
            break

    beforeN=int(aboutMonth[2]) 
    currentN=int(aboutMonth[0]) 
    global currentDay
    currentDay=1
    numberT=[]
          
    
    for tt in range(42):#반복문으로 해보자!!'
        
        numberT.append(tt+1)
        
        def click(t=numberT[tt]):
            global tday
            tday=t-iday
            if 0<tday<=currentN:
                
                #날짜 바꾸기
                sLabel.configure(text =cYear+mC+' '+str(tday)+'일', fg ='black')
                deleteDayInfo()
                
                #날짜에 해당하는 정보 불러오기
                loadDayInfo()                     

            else:
                sLabel.configure(text = '잘못된 선택입니다', fg ='red')

        
            
        #이전달 채우기
        if tt<iday:
            beforeDay=beforeN-iday+tt+1
            dbt=tk.Button(window,text=beforeDay,command=click,
                           font='고딕',bg='white',fg='gray')
            dbt.grid(row=((tt)//7)+3,column=(tt)%7, sticky='we')
        
        #이번달 채우기
        elif iday<=tt<currentN+iday:
                if str(currentDay) in aboutHoliday or tt%7==0:
                    dbt=tk.Button(window,text=currentDay,command=click,
                               font='고딕',bg='white',fg='red')
                    dbt.grid(row=((tt)//7)+3,column=(tt)%7, sticky='we')
                    
                else:
                    dbt=tk.Button(window,text=currentDay, command=click,
                               font='고딕',bg='white',fg='black')
                    dbt.grid(row=((tt)//7)+3,column=(tt)%7, sticky='we')
                currentDay+=1
                    

        
        #다음달 채우기
        elif tt>=currentN+iday:
            nextDay=tt-(currentDay+iday)+2
            dbt=tk.Button(window,text=nextDay, command=click,
                           font='고딕',bg='white',fg='gray')
            dbt.grid(row=((tt)//7)+3,column=(tt)%7, sticky='we')
        
    
#캘린더 달 콤보박스 옆 선택 버튼
monthBt=tk.Button(window,text='선택',font='고딕'
             ,command=monthSelect)
monthBt.grid(row=1,column=8)


#할 일을 표시하는 라벨과 체크박스
chk_var1=tk.BooleanVar()
firEn=tk.Entry(window)
firEn.grid(row=3,column=8,columnspan=2,sticky='we')
firChk=tk.Checkbutton(var=chk_var1)
firChk.grid(row=3,column=11)

chk_var2=tk.BooleanVar()
secEn=tk.Entry(window)
secEn.grid(row=5,column=8,columnspan=2,sticky='we')
secChk=tk.Checkbutton(var=chk_var2)
secChk.grid(row=5,column=11)

chk_var3=tk.BooleanVar()
thiEn=tk.Entry(window)
thiEn.grid(row=7,column=8,columnspan=2,sticky='we')
thiChk=tk.Checkbutton(var=chk_var3)
thiChk.grid(row=7,column=11)

#할일 저장 함수#같은 날짜를 두번 연속해서 저장할 경우 두번 반복됨
def todoSave():
    firE=firEn.get()
    secE=secEn.get()
    thiE=thiEn.get()
    date=sLabel.cget('text')
    
    if chk_var1.get()==False:
        firChkk='X'
    else:
        firChkk='O'
        
    if chk_var2.get()==False:
        secChkk='X'
    else:
        secChkk='O'
        
    if chk_var3.get()==False:
        thiChkk='X'
    else:
        thiChkk='O'

    date=sLabel.cget('text')
                
    for d in range(0,len(tdDate)):
        if date==tdDate[d]:
            theD=d
    
    if date in tdDate:
        print(0)
        #이미 정보가 저장되어있는 날짜일 경우 저장되어 있는 정보를
        #지운 리스트로 새로 작성한뒤 수정된 정보를 다시 저장#
        for rv in [tdDate,tdFir,tdSec,tdThi,firC,secC,thiC]:
            rv.remove(rv[theD])
        c=open('./notes/todo.txt','w',encoding='cp949')
        for tdtd in range(len(tdDate)):
            c.write(tdDate[tdtd])
            c.write('\n')
            c.write(tdFir[tdtd]+'/'+firC[tdtd])
            c.write('\n')
            c.write(tdSec[tdtd]+'/'+secC[tdtd])
            c.write('\n')
            c.write(tdThi[tdtd]+'/'+thiC[tdtd])
            c.write('\n')
                
    c=open('./notes/todo.txt','a',encoding='cp949')
    c.write(date)
    c.write('\n')
    c.write(str(firE)+'/'+firChkk)
    c.write('\n')
    c.write(str(secE)+'/'+secChkk)
    c.write('\n')
    c.write(str(thiE)+'/'+thiChkk)
    c.write('\n')
        
#할 일 저장하기
todoBt=tk.Button(window,text='저장하기',font='고딕'
             ,command=todoSave)
todoBt.grid(row=9,column=8, columnspan=3)


            
#초기값을 ctime에서 불러온 오늘의 cMonth(달)로 설정했으므로
#바로 작동시키면 기본값을 mC로 가진 함수가 실행됨
monthSelect();#현재 날짜 불러오기
loadDayInfo();#날짜에 해당하는 정보 불러오기
window.mainloop()#무한히 반복하는 메인루프 생성
