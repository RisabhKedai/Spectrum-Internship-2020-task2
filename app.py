from tkinter import *
import tkinter.font as font
import time
import math
import random
import sys
import json

#to reset the current entry obj
import the_reset
the_reset.reset()
#the first screen
firstscr=Tk(className='Mark_ENTRY')
firstscr.geometry("720x474")
firstscr.iconbitmap('data_files/spectrumlogo.ico')
#corner decor
but00=Button(firstscr,text='',width=50, height=10,bg='blue',state=DISABLED,padx=-3,pady=20)
but01=Button(firstscr,text='',width=50, height=10,bg='red',state=DISABLED,padx=-3,pady=20)
but10=Button(firstscr,text='',width=50, height=10,bg='green',state=DISABLED,padx=-3,pady=20)
but11=Button(firstscr,text='',width=50, height=10,bg='cyan',state=DISABLED,padx=-3,pady=20)

#welcome message
myf=font.Font(family='Bookman Old Style',size=20,weight='bold')
Label(firstscr,text="",bg='purple',fg='black',padx=100,font=myf).grid(row=1,column=0)
Label(firstscr,text="",bg='purple',fg='black',padx=100,font=myf).grid(row=1,column=1)
wel1=Label(firstscr,text="               WELCOME  TO ",bg='purple',fg='black',font=myf,anchor='e',padx=5)
wel2=Label(firstscr,text="MARK_ENTRY.EXE          ",bg='purple',fg='black',font=myf,anchor='e',padx=0)
wel1.grid(row=1,column=0)
wel2.grid(row=1,column=1)


#countdown
time1=Label(firstscr,text="                Please Wait.....",font=myf,anchor='w')
time2=Label(firstscr,text="{}                         ".format(5),font=myf)
#time uodate function
tim=time.time()
def lab_chng():
	time2['text']="{}s                                   ".format(math.ceil(5-(time.time()-tim)))
	if 5-(time.time()-tim)<=0:
		firstscr.destroy()
		import loginscr
		loginscr.main()
		sys.exit()

	firstscr.after(1000,lab_chng)

#button color changing design
def butt_chng():
	but00['bg']=random.choice(['blue','green','red','cyan','yellow','orange','blue','green','red','cyan','yellow','orange'])
	but11['bg']=random.choice(['blue','green','red','cyan','yellow','orange','blue','green','red','cyan','yellow','orange'])
	but01['bg']=random.choice(['blue','green','red','cyan','yellow','orange','blue','green','red','cyan','yellow','orange'])
	but10['bg']=random.choice(['blue','green','red','cyan','yellow','orange','blue','green','red','cyan','yellow','orange'])
	firstscr.after(70,butt_chng)


#displaying time countdown
time1.grid(row=2,column=0)
time2.grid(row=2,column=1)


#displaying corner decor
but00.grid(row=0,column=0)
but01.grid(row=0,column=1)
but10.grid(row=3,column=0)
but11.grid(row=3,column=1)

butt_chng()
lab_chng()
firstscr.mainloop()
