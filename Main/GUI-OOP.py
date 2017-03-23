from tkinter import *
from tkinter.messagebox import *
import json
root = Tk()

#Функции для окон====================================================== 
def add_address():
	window2 = win_addr()
def win_op():
	window1 = win_d()
def win_ab():
	about = about_message()
def exit():
	ex = exit_yn()


#Загрузка и сохранение истории=========================================
class hystory_proc:
	def save_history(self):
		self.output=open("history.txt", "w")
		json.dump(history, self.output)
		self.output.close()
		print('History has been saved')

	def load_history(self):
		self.input_ = open("history.txt", "r")
		self.hist = json.load(self.input_)
		print('History loaded')
		self.input_.close()
		return self.hist


#Окно добавления нового адреса=========================================
class win_addr:
	def __init__(self):
		self.win1 = Toplevel(root, bd=10, bg="lightblue")
		self.win1.title("Add Address")
		self.win1.minsize(width=200, height=200)

		self.label1 = Label(self.win1, text="Enter an address", font="Arial 18", bg="lightblue")
		self.entry1 = Entry(self.win1,width=20,bd=3)
		self.button1 = Button(self.win1,text="Add",bg="darkblue",fg="white",command=lambda:self.make_address(self.entry1.get()))

		self.label1.pack()
		self.entry1.pack()
		self.button1.pack()

	def make_address(self, address):
		old_addr = listbox_el.lis.get(ACTIVE)
		self.address = [str(address)]
		if history.get(address) is None:
			listbox_el.list_filler(self.address)
			print(self.address)
			message_list = []
			self.temp = {str(address):message_list}
			history.update(self.temp)
			self.temp.clear()
		else:
			print("Такой адрес уже есть TBD")
	

#Окно About и Exit=====================================================
class about_message:
	def __init__(self):
		showinfo('Messanger client', 'Made by Fierrus\nServer made by Sleipnirim')

class exit_yn:
	def __init__(self):
		if askyesno('Exit', 'Confirm'):
			root.destroy()


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
		self.auth_form = [a, b]
		if self.auth_form[0] == '' or self.auth_form[1] == '':
			print("err")
		else:
			print(self.auth_form)

	
#Фреймы================================================================
class frames:
	def __init__(self):
		self.frame1 = Frame(root,width=150,height=500, bd =10)
		self.frame2 = Frame(root,width=400,height=300, bd =5)
		self.frame3 = Frame(root,width=400,height=200, bd =5)
		self.frame1.grid(row=0, column=0, rowspan = 2)
		self.frame2.grid(row=0, column=1)
		self.frame3.grid(row=1, column=1)


#Каскадное меню========================================================
class menus:
	def __init__(self):
		self.m = Menu(root)
		root.config(menu=self.m)
		self.fm = Menu(self.m)
		self.m.add_cascade(label="File",menu=self.fm)
		self.fm.add_command(label="Add address", command = add_address)
		self.fm.add_command(label="Reauthorization", command = win_op)
		self.fm.add_command(label="Exit",command=exit)

		self.hm = Menu(self.m)
		self.m.add_cascade(label="Help",menu=self.hm)
		self.hm.add_command(label="Help")
		self.hm.add_command(label="About", command=win_ab)


#Список адресов + scroll===============================================
class listbox_:
	def __init__(self):
		self.lis = Listbox(frames.frame1,selectmode=SINGLE, height=31)
		self.scr1 = Scrollbar(frames.frame1,command=self.lis.yview)
		self.lis.configure(yscrollcommand=self.scr1.set)

		self.lis.grid(row=0, column=0)
		self.scr1.grid(row=0, column=1,sticky=S+N)

	def list_filler(self, list_):
		for i in list_:
			self.lis.insert(END,i) 


#Поле вывода сообщений + scroll========================================
class text_output:
	def __init__ (self):
		self.tex1 = Text(frames.frame2, width=47, height = 16, font="Verdana 12", wrap=WORD)
		self.scr2 = Scrollbar(frames.frame2,command=self.tex1.yview)
		self.tex1.configure(yscrollcommand=self.scr2.set)

		self.tex1.grid(row=0, column=0)
		self.scr2.grid(row=0, column=1,sticky=S+N)

		global message_list
		message_list = history.get(old_addr)
		self.str1=''.join(message_list)
		self.tex1.insert(END,self.str1)

	def new_message(self, message, flag):
		if flag == 'new':
			message_list.append('Addr:\n'+message + '\n\n')
			self.tex1.config(state=NORMAL)
			self.tex1.insert(END,'Addr:\n'+message + '\n\n')
			self.tex1.config(state=DISABLED)
		elif flag == 'self':
			message_list.append('Self:\n'+message + '\n')
			self.tex1.config(state=NORMAL)
			self.tex1.insert(END,'Self:\n'+message + '\n')
			self.tex1.config(state=DISABLED)
		if len(message_list) > 50:
			message_list.pop(0)


#Поле ввода сообщений + scroll=========================================
class message_input():
	def __init__(self):
		self.tex2 = Text(frames.frame3,width=40, height = 10, font="Verdana 12", wrap=WORD)
		self.scr3 = Scrollbar(frames.frame3,command=self.tex2.yview)
		self.tex2.configure(yscrollcommand=self.scr3.set)

		self.tex2.grid(row=0, column=0)
		self.scr3.grid(row=0, column=1,sticky=S+N)

		self.but1 = Button(frames.frame3,text="Отправить",bg="white",fg="blue", command=self.message_input)
		self.but1.grid(row=0,column = 2, sticky=S+N)

	def message_input(self):
		self.message = self.tex2.get(1.0, END)
		text_output_el.new_message(self.message, 'self')
		self.tex2.delete(1.0, END)


#Кнопка смены адресата=================================================
class addr_change:
	def __init__(self):
		self.but3 = Button(frames.frame1,text='Выбрать',bg="white",fg="blue", command=self.change_addr)
		self.but3.grid(row=1,column=0)

	def change_addr(self):
		global old_addr
		self.addr = listbox_el.lis.get(ACTIVE)
		print("адреса=",old_addr, self.addr)
		if old_addr == self.addr:
			pass
		else:
			global message_list
			text_output_el.tex1.config(state=NORMAL)
			text_output_el.tex1.delete(1.0, END)

			self.temp = {old_addr : message_list}
			print('на сохранение= ',self.temp)
			history.update(self.temp)
			self.temp.clear()

			message_list = history.get(self.addr)
			print('список сообщений= ',message_list)
			self.str1=''.join(message_list)
			print(self.str1)

			text_output_el.tex1.insert(END,self.str1)
			text_output_el.tex1.config(state=DISABLED)
			old_addr = self.addr


#Инициализация бъектов=================================================
hist = hystory_proc()
history = hist.load_history()
frames = frames()
menu_el = menus()
listbox_el = listbox_()
listbox_el.list_filler(history.keys())			#Будет заменено на список получаемый из json по ключу friends
old_addr = listbox_el.lis.get(ACTIVE)
message_list=[]
text_output_el = text_output()
message_input_el = message_input()
change_addr_el = addr_change()

root.mainloop()
print('Величина словаря ',len(history))
hist.save_history()