from tkinter import *




def enter(var):
	entry.insert(END,var)
	

def ans():
	v = entry.get()
	try:
		a = eval(str(v))
		entry.delete(0,END)
		entry.insert(END,a)
	except:
		entry.delete(0,END)
		entry.insert(END,"Invalid Syntax")

def clear_all():
	try:
		entry.delete(0,END)
	except:
		pass

def clear():
	r = len(entry.get())
	entry.delete(r-1,END)

root = Tk()
root.maxsize(width = 300,height = 400)
root.minsize(width = 300,height= 400)
entry = Entry(root,font = ("consolas",20),width = 19) 
entry.place(x = 5,y = 10)
entry.focus()
b_1 = Button(root,text = " 1 ",font = ("consolas",15),command = lambda : enter(1))
b_1.place(x = 10 , y = 280)

b_2 = Button(root,text = " 2 ",font = ("consolas",15),command = lambda : enter(2))
b_2.place(x = 90 , y = 280)

b_3 = Button(root,text = " 3 ",font = ("consolas",15),command = lambda : enter(3))
b_3.place(x = 165 , y = 280)

b_4 = Button(root,text = " 4 ",font = ("consolas",15),command = lambda : enter(4))
b_4.place(x = 10 , y = 210)

b_5 = Button(root,text = " 5 ",font = ("consolas",15),command = lambda : enter(5))
b_5.place(x = 90 , y = 210)


b_6 = Button(root,text = " 6 ",font = ("consolas",15),command = lambda : enter(6))
b_6.place(x = 165 , y = 210)

b_7 = Button(root,text = " 7 ",font = ("consolas",15),command = lambda : enter(7))
b_7.place(x = 10 , y = 140)

b_8 = Button(root,text = " 8 ",font = ("consolas",15),command = lambda : enter(8))
b_8.place(x = 90 , y = 140)

b_9 = Button(root,text = " 9 ",font = ("consolas",15),command = lambda : enter(9))
b_9.place(x = 165 , y = 140)

b_0 = Button(root,text = " 0 ",font = ("consolas",15),command = lambda : enter(0))
b_0.place(x = 10 , y = 350)

mul = Button(root,text = " * ",font = ("consolas",15),command = lambda : enter('*'))
mul.place(x = 240 ,y = 210)

div = Button(root,text = ' '+u"\u00F7"+' ',font = ("consolas",15),command = lambda : enter('/'))
div.place(x = 240 ,y = 140)

plus = Button(root,text = " + ",font = ("consolas",15),command = lambda : enter('+'))
plus.place(x = 240,y = 280)

minus = Button(root,text = " - ",font = ("consolas",15),command = lambda : enter('-'))
minus.place(x = 240,y = 350)

dot = Button(root,text = " . ",font = ("consolas",15),command = lambda : enter('.'))
dot.place(x = 90,y = 350)

equal = Button(root,text = " = ",font = ("consolas",15),command = ans)
equal.place(x = 165,y = 350)

clear = Button(root,text =" "+u"\u232B"+" ",font = ("consolas",15),command = clear)
clear.place(x = 230,y = 70)

_clear_all = Button(root,text = " Clear All ",font = ("consolas",15),command = clear_all)
_clear_all.place(x = 10,y = 70)
root.mainloop()
