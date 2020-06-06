#login success
from tkinter import *
import tkinter.font
import sys
import create_acc

def main():
	msg_scr=Tk(className='Error!!')
	msg_scr.geometry('350x100')
	msg_scr.iconbitmap('data_files/spectrumlogo.ico')
	Label(msg_scr,text='*You have entered wrong username \nor password.\nIf you donot have an account\n please create one.'.upper(),fg='red').pack()
	def close():
		msg_scr.destroy()
		create_acc.main()
		#sys.exit()
	Button(text='OK',command=close).pack()
	msg_scr.after(5000,close)
	#msg_scr.after(1,create_acc.main)
	msg_scr.mainloop()
	

if __name__=='__main__':
	main()
