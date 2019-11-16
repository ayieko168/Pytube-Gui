from tkinter import *


w = Tk()

# The MenuBar

menubar = Menu(w, tearoff=False)

filemenu = Menu(tearoff=False)
filemenu.add_command(label='New')
filemenu.add_command(label='Open..')

helpmenu = Menu(tearoff=False)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Help..')

menubar.add_cascade(label='File', menu=filemenu, underline=0)
menubar.add_cascade(label='Help', menu=helpmenu, underline=0)

print(w.winfo_screenheight())

w.config(bg='white', menu=menubar)
w.geometry('500x533+200+100')
w.title('Pytube GUI')
w.mainloop()
