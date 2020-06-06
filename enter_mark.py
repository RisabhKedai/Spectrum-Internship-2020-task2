#this is the window where uses enters the marks
from tkinter import *
import tkinter.font as font
import json
import info
lab='    '

def main():
	entscr=Tk(className='enter marks')
	entscr.geometry('250x120')
	entscr.iconbitmap('data_files/spectrumlogo.ico')

	f=font.Font(family='Calibri',weight='bold',size=17)
	#subject heading
	Label(entscr,text=lab,font=f).pack()
	#entry box
	mark=Entry(entscr,borderwidth=2,width=20)
	mark.pack(pady=6)
	#button function
	def toDatabase():
		with open('data_files/currentobj.json','r') as cf:
			l=json.load(cf)
		if lab=='PPS':
			l['pps']=int(mark.get())
		elif lab=='MATH':
			l['math']=int((mark.get()))
		elif lab=='CHEMISTRY':
			l['chem']=int(mark.get())
		with open('data_files/currentobj.json','w') as cf:
			json.dump(l,cf)
		
		entscr.destroy()
	#checking the prexistence of mark
	with open('data_files/currentobj.json','r') as cf:
		l=json.load(cf)
	if lab=='PPS':
		if l['pps']!=0:
			mark.delete(0,END)
			mark.insert(0,l['pps'])
	elif lab=='MATH':
		if l['math']!=0:
			mark.delete(0,END)
			mark.insert(0,l['math'])
	elif lab=='CHEMISTRY':
		if l['chem']!=0:
			mark.delete(0,END)
			mark.insert(0,l['chem'])

	#submit button
	sub=Button(entscr,text='SUBMIT',command=toDatabase)
	sub.pack(pady=15)
	entscr.mainloop()

if __name__=='__main__':
	main()