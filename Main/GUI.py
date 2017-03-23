
from tkinter import *
import json
root = Tk()
#Загрузка и сохранение истории=========================================
def save_history():
	output=open("history.txt", "w")
	json.dump(history, output)
	output.close()
	print('History has been saved')

def load_history():
	input_ = open("history.txt", "r")
	hist = json.load(input_)
	print('History loaded')
	return hist

history = load_history()

#Окно добавления нового адреса=========================================
class win_addr:
	def __init__(self):
		self.win1 = Toplevel(root, bd=10, bg="lightblue")
		self.win1.title("Add Address")
		self.win1.minsize(width=200, height=200)

		self.label1 = Label(self.win1, text="Enter an address", font="Arial 18", bg="lightblue")
		self.entry1 = Entry(self.win1,width=20,bd=3)
		self.button1 = Button(self.win1,text="Add",bg="darkblue",fg="white",command=lambda:self.serch_address(self.entry1.get()))

		self.label1.pack()
		self.entry1.pack()
		self.button1.pack()

	def serch_address(self, address):
		self.address = [str(address)]
		list_filler(self.address)
		print(address)


def add_address():
	window2 = win_addr()



#Окно авторизации======================================================
class win_d:
	def __init__(self):
		self.win = Toplevel(root, bd=10, bg="lightblue")
		self.win.title("Authorization")
		self.win.minsize(width=200, height=200)

		lab1 = Label(self.win, text="Login", font="Arial 18", bg="lightblue")
		lab2 = Label(self.win, text="Pass", font="Arial 18", bg="lightblue")

		ent1 = Entry(self.win,width=20,bd=3)
		ent2 = Entry(self.win,width=20,bd=3)

		c1 = IntVar()
		che1 = Checkbutton(self.win,text="Auto Log in",variable=c1,onvalue=1,offvalue=0,bg="lightblue")

		but2 = Button(self.win,text="Login",bg="darkblue",fg="white", command=lambda: self.auth(ent1.get(),ent2.get()))

		lab1.pack()
		ent1.pack()
		lab2.pack()
		ent2.pack()
		che1.pack()
		but2.pack()

	def auth(self, a, b):
		self.a = a
		self.b = b
		auth_form = [self.a, self.b]
		if auth_form[0] == '' or auth_form[1] == '':
			print("err")
		else:
			print(auth_form)


def win_op():
	window1 = win_d()
	
#Фреймы================================================================
frame1 = Frame(root,width=150,height=500, bd =10)
frame2 = Frame(root,width=400,height=300, bd =5)
frame3 = Frame(root,width=400,height=200, bd =5)
frame1.grid(row=0, column=0, rowspan = 2)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=1)

#Каскадное меню========================================================
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="Add address", command = add_address)
fm.add_command(label="Reauthorization", command = win_op)
fm.add_command(label="Exit")

hm = Menu(m)
m.add_cascade(label="Help",menu=hm)
hm.add_command(label="Help")
hm.add_command(label="About")

#Список адресов + scroll===============================================

def list_filler(list_):		#Заполнитель листа
	for i in list_:
		lis.insert(END,i) 

lis = Listbox(frame1,selectmode=SINGLE, height=31)
scr1 = Scrollbar(frame1,command=lis.yview)
lis.configure(yscrollcommand=scr1.set)

lis.grid(row=0, column=0)
scr1.grid(row=0, column=1,sticky=S+N)

list_filler(history.keys()) #>>>>>>> filler test<<<<<<<

#Поле вывода сообщений + scroll========================================
def list_checker():
	if len(message_list) > 50:
		message_list.pop(0)

message_list=[]
def new_message(message, flag):
	if flag == 'new':
		message_list.append('Addr:\n'+message + '\n\n')
		tex1.config(state=NORMAL)
		tex1.insert(END,'Addr:\n'+message + '\n\n')
		tex1.config(state=DISABLED)
	elif flag == 'self':
		message_list.append('Self:\n'+message + '\n')
		tex1.config(state=NORMAL)
		tex1.insert(END,'Self:\n'+message + '\n')
		tex1.config(state=DISABLED)

	list_checker()

def TEST():										#>>>>>>>Тестирование сообщений
	list_test = ["test1","test2","test3","test4","test5"]
	for i in list_test:
		 new_message(i, 'new')							#<<<<<<<


tex1 = Text(frame2, width=47, height = 16, font="Verdana 12", wrap=WORD)
scr2 = Scrollbar(frame2,command=tex1.yview)
tex1.configure(yscrollcommand=scr2.set)

tex1.grid(row=0, column=0)
scr2.grid(row=0, column=1,sticky=S+N)

TEST()

#Поле ввода сообщений + scroll=========================================
def message_input():
	message = tex2.get(1.0, END)
	new_message(message, 'self')
	tex2.delete(1.0, END)

tex2 = Text(frame3,width=40, height = 10, font="Verdana 12", wrap=WORD)
scr3 = Scrollbar(frame3,command=tex2.yview)
tex2.configure(yscrollcommand=scr3.set)

tex2.grid(row=0, column=0)
scr3.grid(row=0, column=1,sticky=S+N)

#Кнопка отправки сообщения=============================================
but1 = Button(frame3,text="Отправить",bg="white",fg="blue", command=message_input)

but1.grid(row=0,column = 2, sticky=S+N)

#История===============================================================


#history = {'test1': ["test1","test2","test3","test4","test5"],
#'test2': ["test1","test2","test3","test4","test5"],
#'test3': ["test1","test2","test3","test4","test5"],
#'test4': ["test1","test2","test3","test4","test5"],
#'test5': [],}


#Кнопка смены адресата=================================================
old_addr = lis.get(ACTIVE)


def change_addr():
	global old_addr
	addr = lis.get(ACTIVE)
	print("адреса=",old_addr, addr)
	if old_addr == addr:
		pass
	else:
		global message_list
		tex1.config(state=NORMAL)
		tex1.delete(1.0, END)
		temp = {old_addr : message_list}
		print('на сохранение= ',temp)
		history.update(temp)
		temp.clear()
		message_list = history.get(addr)
		print('список сообщений= ',message_list)
		if message_list == None:
			message_list = []
			temp = {addr:message_list}
			history.update(temp)
			temp.clear()
			pass
		else:
			str1=''.join(message_list)
			print(str1)
			tex1.insert(END,str1)
			tex1.config(state=DISABLED)
			old_addr = addr


but3 = Button(frame1,text='Выбрать',bg="white",fg="blue", command=change_addr)
but3.grid(row=1,column=0)


root.mainloop()
print('Величина словаря ',len(history))
save_history()