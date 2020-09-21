# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:06:29 2020

@author: Rated R
"""


from datetime import date,datetime
from tkinter import Tk, Canvas

def get_events():
    list_events=[]
    with open('upcoming_events.txt') as file:
        for line in file:
            line=line.rstrip('\n')
            current_event=line.split(',')
            event_date=datetime.strptime(current_event[1],'%d/%m/%y').date()
            current_event[1]=event_date
            list_events.append(current_event)
    return list_events


def days_between_dates(date1,date2):
    time_between=str(date2-date1)
    number_of_days=time_between.split(' ')
    return number_of_days[0]


root=Tk()
c=Canvas(root,width=800,height=800,bg='lightblue')
c.pack()
c.create_text(100,50,anchor='w',fill='darkorange',font='Arial 28 bold underline',
              text='Countdown Calendar')
events=get_events()
today=date.today()
vertical=100
for event in events:
    event_name=event[0]
    days_until=days_between_dates(today,event[1])
    if int(days_until)<=7:
        text_col='red'
    else:
        text_col='green'
    display='It is %s days until %s' %(days_until,event_name)
    c.create_text(100,vertical,anchor='w',fill=text_col,font='Arial 28 bold',
                  text=display)
    vertical+=40



root.mainloop()
