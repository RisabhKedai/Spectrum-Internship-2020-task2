#creating account
from tkinter import *
import tkinter.font as font
import info
#import sqlite3
import json

def main():
	#account creating screen
	accscr=Tk(className='Create account')
	accscr.geometry('600x490')
	accscr.iconbitmap('data_files/spectrumlogo.ico')


	byf=font.Font(family='Brush Script MT',size=15,weight='bold')

	Button(text='i',font=byf,bg='yellow',width=3,height=0,pady=1,command=info.main).grid(row=0,columnspan=2,sticky='e')
	#heading

	
	myf=font.Font(family='Courier',size=20,weight='bold')
	Label(accscr,text='Please enter your details.',font=myf,padx=90,pady=30).grid(row=1,columnspan=2)

	#form creation
	lyf=font.Font(family='Courier',size=15,weight='bold')
	Label(accscr,text='Your Name:',anchor='e',font=lyf).grid(row=2,column=0,sticky=E)
	name=Entry(accscr,width=30,borderwidth=1)
	name.grid(row=2,column=1,sticky=W,padx=0)

	'''Label(accscr,text='Email:',anchor='e',font=lyf).grid(row=2,column=0,sticky=E)
	email=Entry(accscr,width=30,borderwidth=1)
	email.grid(row=2,column=1,sticky=W,padx=0)'''

	Label(accscr,text='Registeration No.:',anchor='e',font=lyf).grid(row=3,column=0,sticky=E)
	reg=Entry(accscr,width=30,borderwidth=1)
	reg.grid(row=3,column=1,sticky=W,padx=0)

	Label(accscr,text='Branch:',anchor='e',font=lyf).grid(row=4,column=0,sticky=E)
	branch=Entry(accscr,width=30,borderwidth=1)
	branch.grid(row=4,column=1,sticky=W,padx=0)

	'''Label(accscr,text='Date of Birth:',anchor='e',font=lyf).grid(row=5,column=0,sticky=E)
	dob=Entry(accscr,width=30,borderwidth=1)
	dob.grid(row=5,column=1,sticky=W,padx=0)'''

	Label(accscr,text='Create Password:',anchor='e',font=lyf).grid(row=6,column=0,sticky=E)
	pas1=Entry(accscr,width=30,borderwidth=1)
	pas1.grid(row=6,column=1,sticky=W,padx=0)

	Label(accscr,text='Confirm Password:',anchor='e',font=lyf).grid(row=7,column=0,sticky=E)
	pas2=Entry(accscr,width=30,borderwidth=1)
	pas2.grid(row=7,column=1,sticky=W,padx=0)
	#all the entry fields are defined

	#empty space
	msg=Label(accscr,text='  ',padx=20,pady=10)
	msg.grid(columnspan=2,row=8)

	#defining buttons functions.
	def cancel():    
		#cancel button
		accscr.destroy()
		import loginscr
		loginscr.main()

	def back():    
		#back button
		accscr.destroy()
		import loginscr
		loginscr.main()


	def submit():
		    #submit the response
                Name=name.get()
                #Email=email.get()
                Regd=reg.get()
                #DOB=dob.get()
                br=branch.get()
                cp=pas1.get()
                cop=pas2.get()
                l=[Name,Regd,br,cp,cop]
                if None in l or "" in l:
                        msg['text']='Please fill all the feilds'
                elif cp!=cop:
                        msg['text']='Passwords donot match'
                else:
                        try:
                        	un=Name.replace(" ",'.').lower()+Regd[-4:]
                        except ValueError:
                        	un=Name.lower()+Regd[-4:]
                        #loading data
                        with open('data_files/users.json','r') as mf:
                        	k=json.load(mf)
                        #storing data
                        k[un]=cop
                        with open('data_files/users.json','w') as mf:
                        	json.dump(k,mf)
                        msg['text']='The username assigned to you is {} \n click back button and use credentials to sign in'.format(un)


	#defining buttons
	submit=Button(accscr,text='SUBMIT',command=submit,height=3)
	submit.grid(row=9,column=0,padx=10,sticky=E)
	cancel=Button(accscr,text='CANCEL',command=cancel,height=3)
	cancel.grid(row=9,column=1,padx=20,sticky=W)
	back=Button(accscr,text='BACK',command=back,height=1)
	back.grid(row=10,columnspan=2,pady=30)

	accscr.mainloop()


if __name__=='__main__':
	main()