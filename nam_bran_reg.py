#creating account
from tkinter import *
import loginscr
import mark_ent
import json
import fulldb
import info
import sqlite3
thru_log=False

def main():
    #account creating screen
    detscr=Tk(className='Create account')
    detscr.geometry('674x330')
    detscr.iconbitmap('data_files/spectrumlogo.ico')
    #heading

    import tkinter.font as font

    byf=font.Font(family='Brush Script MT',size=15,weight='bold')

    Button(text='i',font=byf,bg='yellow',width=3,height=0,pady=1,command=info.main).grid(row=0,column=7,sticky='ne')


    myf=font.Font(family='Courier',size=20,weight='bold')
    Label(detscr,text='Please enter your details.',font=myf,padx=90,pady=30).grid(row=0,columnspan=2)

    #form creation
    lyf=font.Font(family='Courier',size=15,weight='bold')
    Label(detscr,text='Name:',anchor='e',font=lyf).grid(row=1,column=0,sticky=E)
    name=Entry(detscr,width=30,borderwidth=1)
    name.grid(row=1,column=1,sticky=W,padx=0)

    '''Label(accscr,text='Email:',anchor='e',font=lyf).grid(row=2,column=0,sticky=E)
    email=Entry(accscr,width=30,borderwidth=1)
    email.grid(row=2,column=1,sticky=W,padx=0)'''

    Label(detscr,text='Registeration No.:',anchor='e',font=lyf).grid(row=3,column=0,sticky=E)
    reg=Entry(detscr,width=30,borderwidth=1)
    reg.grid(row=3,column=1,sticky=W,padx=0)

    Label(detscr,text='Branch:',anchor='e',font=lyf).grid(row=4,column=0,sticky=E)
    branch=Entry(detscr,width=30,borderwidth=1)
    branch.grid(row=4,column=1,sticky=W,padx=0)

    '''Label(accscr,text='Date of Birth:',anchor='e',font=lyf).grid(row=5,column=0,sticky=E)
    dob=Entry(accscr,width=30,borderwidth=1)
    dob.grid(row=5,column=1,sticky=W,padx=0)'''

    '''Label(accscr,text='Create Password:',anchor='e',font=lyf).grid(row=6,column=0,sticky=E)
    pas1=Entry(accscr,width=30,borderwidth=1)
    pas1.grid(row=6,column=1,sticky=W,padx=0)

    Label(accscr,text='Confirm Password:',anchor='e',font=lyf).grid(row=7,column=0,sticky=E)
    pas2=Entry(accscr,width=30,borderwidth=1)
    pas2.grid(row=7,column=1,sticky=W,padx=0)
    #all the entry fields are defined'''

    #empty space
    msg=Label(detscr,text='  ',padx=20,pady=10,fg='red')
    msg.grid(columnspan=2,row=8)

    #defining buttons functions.
    def cancel():    
        #cancel button
        detscr.destroy()
        if thru_log:
            loginscr.main()
        else:
            mark_ent.main()

    '''def back():    
        #back button
        detscr.destroy()
        import loginscr
        loginscr.main()
        '''
    #a function to write the files to database
    def writofile(nam,reg,b):
        with open("data_files/currentobj.json",'r') as cf:
            l=json.load(cf)
        l['Name']=nam
        l['Branch']=b
        l['RegID']=reg
        l['pps']=0
        l['math']=0
        l['chem']=0
        with open('data_files/currentobj.json','w') as cf:
            json.dump(l,cf)

    def submit():
            #submit the response
            Name=name.get()
            Regd=reg.get()
            br=branch.get()
            #DOB=dob.get()
            #Email=email.get()
            #cp=pas1.get()
            #cop=pas2.get()
            l=[Name,Regd,br]
            if None in l or "" in l:
                msg['text']='Please fill all the feilds'
            else:
                msg['text']='DATA ADDED'
                detscr.destroy()
                writofile(Name,Regd,br)
                '''with open("data_files/mydb.json",'r') as cof:
                    db=json.load(cof)'''
                cn=sqlite3.connect("data_files/mydata.db")
                c=cn.cursor()

                db=c.execute('''SELECT RegID FROM entries''')

                for r in list(db):
                    if Regd==r[0]:
                        with open("data_files/currentobj.json",'r') as cf:
                            l=json.load(cf)
                            ro=(Regd,)
                        l['pps']=int(list(c.execute('SELECT pps FROM entries WHERE RegID=?',ro))[0][0])
                        l['chem']=int(list(c.execute('SELECT chem FROM entries WHERE RegID=?',ro))[0][0])
                        l['math']=int(list(c.execute('SELECT math FROM entries WHERE RegID=?',ro))[0][0])
                        with open('data_files/currentobj.json','w') as cf:
                            json.dump(l,cf)
                cn.commit()
                cn.close()
                #opening back with new data
                mark_ent.main()

            '''else:
                try:
                    un=Name.replace(" ",'.').lower()+Regd[0:2]+Regd[-4:]
                except ValueError:
                    un=Name.lower()+Regd[0:2]+Regd[-4:]
                    msg['text']='The username assigned to you is {} \n click back button and use credentials to sign in'.format(un)'''
    #defining buttons
    submit=Button(detscr,text='SUBMIT',command=submit,height=3,bg='green',fg='white',padx=7)
    submit.grid(row=9,column=0,padx=10,sticky=E)
    back=Button(detscr,text='BACK',command=cancel,height=3,padx=10,bg='red',fg='white')
    back.grid(row=9,column=1,padx=20,sticky=W)
    Button(detscr,text='   Previous Entries     ',command=fulldb.main,bg='yellow',width=20).grid(row=10,columnspan=3,pady=16,padx=244,sticky='n')
    '''
    cancel=Button(accscr,text='BACK',command=back,height=1)
    cancel.grid(row=10,columnspan=2,pady=30)
    '''
    detscr.mainloop()
if __name__=='__main__':
    main()
#useless shitttt
"""
def top():
    #account creating screen
    detscr=Toplevel()
    detscr.geometry('550x330')
    detscr.title('Enter details')

    #heading

    import tkinter.font as font
    myf=font.Font(family='Courier',size=20,weight='bold')
    Label(detscr,text='Please enter your details.',font=myf,padx=90,pady=30).grid(row=0,columnspan=2)

    #form creation
    lyf=font.Font(family='Courier',size=15,weight='bold')
    Label(detscr,text='Your Name:',anchor='e',font=lyf).grid(row=1,column=0,sticky=E)
    name=Entry(detscr,width=30,borderwidth=1)
    name.grid(row=1,column=1,sticky=W,padx=0)

    '''Label(accscr,text='Email:',anchor='e',font=lyf).grid(row=2,column=0,sticky=E)
    email=Entry(accscr,width=30,borderwidth=1)
    email.grid(row=2,column=1,sticky=W,padx=0)'''

    Label(detscr,text='Registeration No.:',anchor='e',font=lyf).grid(row=3,column=0,sticky=E)
    reg=Entry(detscr,width=30,borderwidth=1)
    reg.grid(row=3,column=1,sticky=W,padx=0)

    Label(detscr,text='Branch:',anchor='e',font=lyf).grid(row=4,column=0,sticky=E)
    branch=Entry(detscr,width=30,borderwidth=1)
    branch.grid(row=4,column=1,sticky=W,padx=0)

    '''Label(accscr,text='Date of Birth:',anchor='e',font=lyf).grid(row=5,column=0,sticky=E)
    dob=Entry(accscr,width=30,borderwidth=1)
    dob.grid(row=5,column=1,sticky=W,padx=0)'''

    '''Label(accscr,text='Create Password:',anchor='e',font=lyf).grid(row=6,column=0,sticky=E)
    pas1=Entry(accscr,width=30,borderwidth=1)
    pas1.grid(row=6,column=1,sticky=W,padx=0)

    Label(accscr,text='Confirm Password:',anchor='e',font=lyf).grid(row=7,column=0,sticky=E)
    pas2=Entry(accscr,width=30,borderwidth=1)
    pas2.grid(row=7,column=1,sticky=W,padx=0)
    #all the entry fields are defined'''

    #empty space
    msg=Label(detscr,text='  ',padx=20,pady=10)
    msg.grid(columnspan=2,row=8)

    #defining buttons functions.
    def cancel():    
        #cancel button
        detscr.destroy()
        import loginscr
        loginscr.main()

    def back():    
        #back button
        detscr.destroy()
        import loginscr
        loginscr.main()


    def submit():
            #submit the response
            Name=name.get()
            #Email=email.get()
            Regd=reg.get()
            #DOB=dob.get()
            br=branch.get()
            #cp=pas1.get()
            #cop=pas2.get()
            l=[Name,Regd,br]
            if None in l or "" in l:
                msg['text']='Please fill all the feilds'
            else:
                msg['text']='DATA ADDED'
            '''else:
                msg['text']='DATA ADDED'
                try:
                    un=Name.replace(" ",'.').lower()+Regd[0:2]+Regd[-4:]
                except ValueError:
                    un=Name.lower()+Regd[0:2]+Regd[-4:]
                    msg['text']='The username assigned to you is {} \n click back button and use credentials to sign in'.format(un)'''

    #defining buttons
    submit=Button(detscr,text='SUBMIT',command=submit,height=3,bg='green',fg='white',padx=7)
    submit.grid(row=9,column=0,padx=10,sticky=E)
    back=Button(detscr,text='BACK',command=cancel,height=3,padx=10,bg='red',fg='white')
    back.grid(row=9,column=1,padx=20,sticky=W)
    '''
    cancel=Button(accscr,text='BACK',command=back,height=1)
    cancel.grid(row=10,columnspan=2,pady=30)
    '''
    detscr.mainloop()

"""
