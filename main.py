from tkinter import *
import tkinter as tk
bg_color="green"
FONT_NAME = "Courier"
activ_col="blue"

win=Tk()
win.title("Calculator")
win.config(bg=bg_color,)

screen=Entry(width=80)
screen.grid(row=0,column=0,columnspan=3,padx=10,pady=10,ipady=10)

but1=Button(text="1",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but1.grid(row=3,column=0,padx=10,pady=10,ipady=10,ipadx=40,)

but2=Button(text="2",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but2.grid(row=3,column=1,padx=10,pady=10,ipady=10,ipadx=40)

but3=Button(text="3",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but3.grid(row=3,column=2,padx=10,pady=10,ipady=10,ipadx=40)

but4=Button(text="4",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but4.grid(row=2,column=0,padx=10,pady=10,ipady=10,ipadx=40)

but5=Button(text="5",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but5.grid(row=2,column=1,padx=10,pady=10,ipady=10,ipadx=40)

but6=Button(text="6",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but6.grid(row=2,column=2,padx=10,pady=10,ipady=10,ipadx=40)

but7=Button(text="7",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but7.grid(row=1,column=0,padx=10,pady=10,ipady=10,ipadx=40)

but8=Button(text="8",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but8.grid(row=1,column=1,padx=10,pady=10,ipady=10,ipadx=40)

but9=Button(text="9",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but9.grid(row=1,column=2,padx=10,pady=10,ipady=10,ipadx=40)

but0=Button(text="0",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
but0.grid(row=4,column=0,padx=10,pady=10,ipady=10,ipadx=40)

butp=Button(text="+")
butp.grid(row=4,column=1,padx=10,pady=10,ipady=10,ipadx=40)

buteq=Button(text="=",activebackground=activ_col,font=(FONT_NAME, 12, "bold"))
buteq.grid(row=4,column=2,padx=10,pady=10,ipady=10,ipadx=40)

win.mainloop()