from tkinter import *
import tkinter.font as font
import webbrowser
from PIL import ImageTk,Image
 

def main():
	infoscr=Toplevel()
	infoscr.title("Project info")
	infoscr.geometry('650x500')
	infoscr.iconbitmap('data_files/spectrumlogo.ico')

	spmsg='Do check out our club\'s website!'
	gimsg="Also, follow me on github, and I'll follow you back!!"
	myf=font.Font(family='Kristen ITC',size=15)
	lyf=font.Font(family='Kristen ITC',size=15,underline=1)

	#Label(infoscr,text="                                                    ",font=myf,width=30,height=1).grid(row=0,sticky='n')


	sp=Label(infoscr,text="",font=myf,width=50,height=2)
	sp.grid(row=1,)

	gi=Label(infoscr,text="  ",font=myf,width=50,height=2)
	speimg=ImageTk.PhotoImage(Image.open('data_files/spectra.png'))
	giimg=ImageTk.PhotoImage(Image.open('data_files/git.png'))

	
	def callback(url):
		webbrowser.open_new(url)

	def textdes(t=0):
		if t>=len(spmsg):
			specl=Label(infoscr,text='https://www.spectrumcet.com/index.php',fg='blue',font=lyf)
			specl.grid(row=2,pady=2)
			specl.bind('<Button-1>',lambda e: callback('https://www.spectrumcet.com/index.php'))
			spedis=Label(infoscr,image=speimg)
			spedis.grid(row=3)
			spedis.bind('<Button-1>',lambda e: callback('https://www.spectrumcet.com/index.php'))
			gi.grid(row=4)

		else:
			sp['text']+=spmsg[t]
			infoscr.after(70,lambda : textdes(t+1))


	def textgut(t=0):
		if t>=len(gimsg):
			gigl=Label(infoscr,text='https://github.com/RisabhKedai',fg='blue',font=lyf)
			gigl.grid(row=5)
			gigl.bind('<Button-1>',lambda e: callback('https://github.com/RisabhKedai'))
			gidis=Label(infoscr,image=giimg)
			gidis.grid(row=6)
			gidis.bind('<Button-1>',lambda e: callback('https://github.com/RisabhKedai'))
			return
		else:
			gi['text']+=gimsg[t]
			infoscr.after(70,lambda : textgut(t+1))

	infoscr.after(10,textdes)
	infoscr.after(3000,textgut)

	Button(infoscr,text='Close',height=1,width=7,bg='green',font=myf,command=infoscr.destroy).grid(row=20,pady=10)
	infoscr.mainloop()

if __name__=='__main__':
	main()