#!/usr/bin/env python3

from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from random import randint

ActiveP=1
p1=[]
p2=[]

root=Tk()
root.title("Tic Tac Game player1")
style=ttk.Style()
style.theme_use('classic')
style.configure('TButton',background='white',font=('Courier',18),foreground='purple')

b1=ttk.Button(root,text=" ")
b1.grid(row=0,column=0,sticky='snew',ipadx=20,ipady=20)
b1.config(command= lambda : Buclick(1))

b2=ttk.Button(root,text=" ")
b2.grid(row=0,column=1,sticky='snew',ipadx=20,ipady=20)
b2.config(command=lambda : Buclick(2))

b3=ttk.Button(root,text=" ")
b3.grid(row=0,column=2,sticky='snew',ipadx=20,ipady=20)
b3.config(command=lambda : Buclick(3))

b4=ttk.Button(root,text=" ")
b4.grid(row=1,column=0,sticky='snew',ipadx=20,ipady=20)
b4.config(command=lambda : Buclick(4))

b5=ttk.Button(root,text=" ")
b5.grid(row=1,column=1,sticky='snew',ipadx=20,ipady=20)
b5.config(command=lambda : Buclick(5))

b6=ttk.Button(root,text=" ")
b6.grid(row=1,column=2,sticky='snew',ipadx=20,ipady=20)
b6.config(command=lambda : Buclick(6))

b7=ttk.Button(root,text=" ")
b7.grid(row=2,column=0,sticky='snew',ipadx=20,ipady=20)
b7.config(command=lambda : Buclick(7))

b8=ttk.Button(root,text=" ")
b8.grid(row=2,column=1,sticky='snew',ipadx=20,ipady=20)
b8.config(command=lambda : Buclick(8))

b9=ttk.Button(root,text=" ")
b9.grid(row=2,column=2,sticky='snew',ipadx=20,ipady=20)
b9.config(command=lambda : Buclick(9))

def Buclick(id):
	global ActiveP
	global p1
	global p2
	if(ActiveP==1):
		setL(id,'X')
		p1.append(id)
		root.title('Player 2')
		ActiveP=2
		AutoPlay()
		#print('P1',p1)
	elif(ActiveP==2):
		setL(id,'O')
		p2.append(id)
		root.title('Player 1')
		ActiveP=1
		#print('P2',p2)
	checkWiner()
	
def setL(id,text):
	if (id==1):
		b1.config(text=text)
		b1.state(['disabled'])
	elif (id==2):
		b2.config(text=text)
		b2.state(['disabled'])
	elif (id==3):
		b3.config(text=text)
		b3.state(['disabled'])
	elif (id==4):
		b4.config(text=text)
		b4.state(['disabled'])
	elif (id==5):
		b5.config(text=text)
		b5.state(['disabled'])
	elif (id==6):
		b6.config(text=text)
		b6.state(['disabled'])
	elif (id==7):
		b7.config(text=text)
		b7.state(['disabled'])
	elif (id==8):
		b8.config(text=text)
		b8.state(['disabled'])
	elif (id==9):
		b9.config(text=text)
		b9.state(['disabled'])


def checkWiner():
	Winer=-1
	# the lines in rows
	if (1 in p1 and 2 in p1 and 3 in p1):
		Winer=1
	if (1 in p2 and 2 in p2 and 3 in p2):
		Winer=2
		
	if (4 in p1 and 5 in p1 and 6 in p1):
		Winer=1
	if (4 in p2 and 5 in p2 and 6 in p2):
		Winer=2
		
	if (7 in p1 and 8 in p1 and 9 in p1):
		Winer=1
	if (7 in p2 and 8 in p2 and 9 in p2):
		Winer=2
		
	# the lines in columns
	if (1 in p1 and 4 in p1 and 7 in p1):
		Winer=1
	if (1 in p2 and 4 in p2 and 7 in p2):
		Winer=2
	
	if (2 in p1 and 5 in p1 and 8 in p1):
		Winer=1
	if (2 in p2 and 5 in p2 and 8 in p2):
		Winer=2
		
	if (3 in p1 and 6 in p1 and 9 in p1):
		Winer=1
	if (3 in p2 and 6 in p2 and 9 in p2):
		Winer=2
		
	#The lines in Diameters
	if (1 in p1 and 5 in p1 and 9 in p1):
		Winer=1
	if (1 in p2 and 5 in p2 and 9 in p2):
		Winer=2
		
	if (3 in p1 and 5 in p1 and 7 in p1):
		Winer=1
	if (3 in p2 and 5 in p2 and 7 in p2):
		Winer=2
	
	if (Winer==1):
		messagebox.showinfo(title='Cong.',message='Player 1 is winer')
	if (Winer==2):
		messagebox.showinfo(title='Cong.',message='Player 2 is winer')
	
	
def AutoPlay():
	global p1
	global p2
	Emptycell=[]
	for cell in range(9):
		if (not ((cell+1 in p1) or (cell+1 in p2)) ):
			Emptycell.append(cell+1)
	RandIndex=randint(0, len(Emptycell)-1)
	Buclick(Emptycell[RandIndex])
		
		
		

root.mainloop()
