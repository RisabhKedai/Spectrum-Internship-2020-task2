from tkinter import *
import tkinter.font as font
import nam_bran_reg
import json
import info
from datetime import datetime
import sqlite3

def main():
	mainscr=Tk(className='MarkEntry')
	mainscr.geometry('500x550')
	mainscr.iconbitmap('data_files/spectrumlogo.ico')
	head_font=font.Font(family='Corbel',size=20)
	det_font=font.Font(family='Kalinga',size=13,weight='bold')

	byf=font.Font(family='Brush Script MT',size=15,weight='bold')

	Button(text='i',font=byf,bg='yellow',width=3,height=0,pady=1,command=info.main).grid(row=0,columnspan=3,sticky='e')

	#open the current obj file
	with open('data_files/currentobj.json','r') as cf:
			l=json.load(cf)

	#the headings
	Label(text='Welcome. You may enter the marks',fg='red',font=head_font).grid(padx=50,row=0,columnspan=3)
	#the details
	Label(text='Name: {} \n\n Regd No.: {} \n\n Branch: {}'.format(l['Name'],l['RegID'],l['Branch']),font=det_font,padx=30).grid(row=1,columnspan=3,padx=10,pady=40)
	msg=Label(text='Click the button to enter the mark.\n\n',fg='red',font=det_font)
	msg.grid(row=2,columnspan=3)


	#defining button functions
	def clickoe(text):
		import enter_mark
		enter_mark.lab=text
		enter_mark.main()

	def cancel():
		import the_reset
		the_reset.reset()
		mainscr.destroy()
		nam_bran_reg.main()


	def submit():
		'''import calc_scr
		calc_scr.top()'''
		#loading all the details to be added to the database
		with open('data_files/currentobj.json','r') as cf:
			l=json.load(cf)
		if 0 in [l['pps'],l['math'],l['chem']]:
			msg['text']='Please enter all the marks'
		else:
			with open('data_files/currentobj.json','r') as cf:
				l=json.load(cf)
			cn=sqlite3.connect("data_files/mydata.db")
			c=cn.cursor()
			c.execute("INSERT INTO entries VALUES (:username, :Name, :RegID, :Branch, :pps, :math, :chem)",l)

			#temporary db just for beauty 
			with open('data_files/mydb.json','r') as cof:
				db=json.load(cof)
			for k,v in zip(db.keys(),l.values()):	
				db[k].append(v)
			db['Date'].append(str(datetime.date(datetime.now())))
			db['time'].append(str(datetime.time(datetime.now())))
			with open('data_files/mydb.json','w') as cof:
				json.dump(db,cof) 
			cn.commit()
			cn.close()

			#creating an overbox for calculations
			import fulldb
			def call_name():
				mainscr.destroy()
				nam_bran_reg.thru_log=False
				nam_bran_reg.main()

			def cgpa():
				with open('data_files/currentobj.json','r') as cf:
					l=json.load(cf)
				per=l['math']+l['pps']+l['chem']
				per=per/3
				cgpa=per/(9.5)
				val.delete(0,END)
				val.insert(0,cgpa)
			def grad():
				with open('data_files/currentobj.json','r') as cf:
					l=json.load(cf)
				per=l['math']+l['pps']+l['chem']
				per=per/3
				#cgpa=per/(9.5)
				if per<100 and per>=90:
					gra='O'
				elif per<90 and per>=80:
					gra='E'
				elif per<80 and per>=70:
					gra='A'
				elif per<70 and per>=60:
					gra='B'
				elif per<60 and per>=50:
					gra='C'
				elif per<50 and per>=40:
					gra='D'
				elif per<40:
					gra='F'
				val.delete(0,END)
				val.insert(0,gra)
			cac=Toplevel()
			cac.title('CGPA & Grade')
			cac.iconbitmap('data_files/spectrumlogo.ico')
			cac.geometry=('100x100')
			myf=font.Font(family='Courier',size=10,weight='bold')
			# defining the buttons
			Button(cac,text='CGPA',height=5,width=10,bg='yellow',fg='red',font=myf,command=cgpa).grid(row=0,column=0,padx=20,pady=30)
			Button(cac,text='Grade',height=5,width=10,bg='yellow',fg='red',font=myf,command=grad).grid(row=0,column=1,padx=20,pady=30)
			byf=font.Font(family='Brush Script MT',size=10,weight='bold')
			Button(cac,text='i',font=byf,bg='yellow',width=3,height=0,pady=1,command=info.main).grid(row=1,columnspan=2)
			Button(cac,text='Close',height=5,width=10,bg='yellow',fg='red',font=myf,command=sys.exit).grid(row=2,column=1,padx=20,pady=30)
			Button(cac,text='New Entry',height=5,width=10,bg='yellow',fg='red',font=myf,command=call_name).grid(row=2,column=0,padx=20,pady=30)
			#Display box
			val=Entry(cac,borderwidth=6,width=40)
			val.grid(row=3,columnspan=2)
			#the last button
			Button(cac,text='Your Entries',bg='yellow',fg='red',font=myf,width=30,command=fulldb.main).grid(row=4,columnspan=2,pady=5)
			#the top window ends here

	
	#buttons
	math=Button(text='MATH',command=lambda :clickoe('MATH'),font=det_font,fg='green',bg='yellow',height=3,width=10,)
	math.grid(row=3,column=0)
	PPS=Button(text='PPS',command=lambda :clickoe('PPS'),font=det_font,fg='green',bg='yellow',height=3,width=10,)
	PPS.grid(row=3,column=1)
	chem=Button(text='CHEMISTRY',command=lambda :clickoe('CHEMISTRY'),font=det_font,fg='green',bg='yellow',height=3,width=10,)
	chem.grid(row=3,column=2)

	Label(text='\n\n').grid(row=4)
	submit=Button(text='SUBMIT',font=det_font,command=submit)
	submit.grid(row=5,column=0,sticky='e')
	cancel=Button(text='CANCEL',font=det_font,command=cancel)
	cancel.grid(row=5,column=2,sticky='w')


	mainscr.mainloop()

if __name__=="__main__":
	main()



'''

def top():
	
	

if __name__=='__main__':
	top()'''