# 동아대 22-2 코딩의기초와문제해결(07)팀프로젝트 - 1조:주식 차트와 달력출력
# *파이썬 3.9.13 버전에서 사용!*

# <야후 파이낸스 주가 데이터 가져오기>
# 명령프롬프터'cmd'에서 실행하기
# pip install yfinance
# pip install matplotlib
# pip install tkcalendar

from tkinter import*    # tkinter 모듈 내 모든 클래스와 함수,상수 가져오기
from tkcalendar import* # tkcalendar 모듈 내 모든 클래스와 함수,상수 가져오기

#사용된 패키지
import datetime
import yfinance as yf
import matplotlib.pyplot as plt    # 그래프를 그리도록 도와주는 라이브러리: matplotlib


window = Tk()   # Tk라는 윈도우 객체 생성
window.title("주식 데이터")
window.geometry('500x100')

Label(window,text = "종목 코드").grid(column=0,row=0)
Label(window,text = "확인할 날짜(yyyy-mm-dd)").grid(column=0,row=1)
Label(window,text = "~").grid(column=2,row=1)

stock = Entry(window,width=15)      # 주식 '종목코드' 입력칸 생성
start_day = Entry(window,width=15)  # '시작 날짜' 입력칸 생성
finish_day = Entry(window,width=15) # '끝 날짜' 입력칸 생성
stock.grid(column=1,row=0)      # '종목코드' 1행 0열 위치
start_day.grid(column=1,row=1)  # '시작날짜' 1행 1열 위치
finish_day.grid(column=3,row=1) # '끝 날짜' 3행 1열 위치


def calendar():    # 주가변동 달력 표시함수
    root = Tk()
    root.title("Calendar")
    root.geometry("600x400")
    
    str_date = start_day.get()      #get으로 값 불러오기 
    str_year, str_month, str_day = str_date.split('-')      # -를 기준으로 문자열을 잘라주는 split
    str_date = datetime.date(int(str_year),int(str_month),int(str_day)) #입력한 year,month,day를 int로 문자열에서 정수로 변경 이를 datetime 모듈에 넣기
    
    cal = Calendar(root, selectmode="day", year=str_date.year, month=str_date.month, day=str_date.day)  #달력 생성
    cal.pack(fill = "both", expand = True)
    
    root.mainloop()



def graph():       # 주가 그래프 그리기 함수
    print('특정 기간내의 [주가] 데이터 받아오기')
    company = yf.download(stock.get(), start_day.get(), finish_day.get()) # company: 원하는 회사의 주가 데이터 담기
    print(company)
    plt.plot(company.index, company.Close) # plt.plot으로 그래프를 그리고,
    plt.show() # plt.show로 그 그래프를 화면에 띄운다.


btn_graph=Button(window,text="달력 확인",command=calendar)       # '달력' 확인 버튼 생성
btn_calendar=Button(window,text="그래프 확인",command = graph)  # '차트' 확인 버튼 생성
btn_graph.grid(column = 2, row = 3)
btn_calendar.grid(column = 3, row = 3)
window.mainloop()
