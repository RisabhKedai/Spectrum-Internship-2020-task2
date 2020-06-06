#this consists of the main application
from tkinter import *
import tkinter.font as font
import sys
import create_acc
import nam_bran_reg
import mark_ent
import login_msg
import info
import json

def main():
	#function to check correct username
	def check_user():
		us=username.get()
		pa=password.get()
		if us in dat.keys() and dat[us]==pa:
			incorrect['text']="*You're now successfully logged in"
			logscr.after(5000,clr_inc)
			logscr.destroy()
			with open("data_files/currentobj.json",'r') as cf:
				l=json.load(cf)
			l['username']=us
			with open('data_files/currentobj.json','w') as cf:
				json.dump(l,cf)
			nam_bran_reg.thru_log=True
			nam_bran_reg.main()
			sys.exit()
		elif us=="" or pa=="" or us not in dat.keys():
			logscr.destroy()
			login_msg.main()
			#logscr.after(5000,clr_inc)
			sys.exit()
		elif pa!=dat[us]:
			incorrect['text']="*You have entered wrong username or password.\nIf you donot have an account please create one."
			logscr.destroy()
			login_msg.main()
			logscr.after(4000,clr_inc)


		

	#create account button
	def cretacc():
		logscr.destroy()
		create_acc.main()
	

	#the login message should get deleted
	def clr_inc():
		incorrect['text']='  '
	#sample username
	with open('data_files/users.json','r') as mf:
		dat=json.load(mf)
	#creating a login screen
	logscr=Tk(className='please LOGIN'.lower())
	logscr.geometry("300x330")
	logscr.iconbitmap('data_files/spectrumlogo.ico')

	myf=font.Font(family='Courier',size=15,weight='bold')
	byf=font.Font(family='Brush Script MT',size=15,weight='bold')

	Button(text='i',font=byf,bg='yellow',width=3,height=0,pady=1,command=info.main).pack(side='top',anchor='e')

	#Label(logscr,text=' ',pady=5).pack()
	

	Label(logscr,text='USERNAME:',font=myf).pack()
	username=Entry(logscr,width=30,borderwidth=1)
	username.pack()

	Label(logscr,text=' ',pady=5).pack()

	Label(logscr,text='PASSWORD:',font=myf).pack()
	password=Entry(logscr,width=30,borderwidth=1)
	password.pack()


	incorrect=Label(logscr,text=' ',fg='red')
	incorrect.pack( )

	Label(logscr,text=' ',pady=15).pack()


	sub_but=Button(logscr,text='SUBMIT',command=check_user)
	sub_but.pack()
	cre_but=Button(logscr,text='CREATE ACCOUNT',command=cretacc)
	cre_but.pack()
	Label(logscr,text='*Create an account for free ^',fg='red').pack()

	logscr.mainloop()


if __name__=='__main__':
	main()


