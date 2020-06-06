from tkinter import *
import sqlite3
import json 
import info
import tkinter.font as font

def main():
	disp=Toplevel()
	disp.title('Your_Entries'.lower())
	disp.geometry("1200x330")
	byf=font.Font(family='Brush Script MT',size=15,weight='bold')

	Button(disp,text='i',bg='green',width=3,height=0,pady=1,command=info.main,font=byf).grid(row=0,column=9,sticky='ne')
	c=sqlite3.connect('data_files/mydata.db').cursor()
	with open('data_files/currentobj.json','r') as co:
		l=json.load(co)
	myf=font.Font(family='Courier',size=10,weight='bold')
	with open('data_files/mydb.json','r') as cof:
		db=json.load(cof)
	for k in range(len(list(db.keys()))):
		if list(db.keys())[k]!='username':
			Label(disp,text=list(db.keys())[k],padx=20,font=myf).grid(row=0,column=k)

	tbl=list(db.values())
	#print(tbl)
	for r in range(len(tbl[0])):
		if tbl[0][r]==l['username']:
			for c in range(1,len(tbl)):
				Label(disp,text=str(tbl[c][r]),padx=20,font=myf).grid(row=r+1,column=c)
	#disp.mainloop()

if __name__=='__main__':
	main()
