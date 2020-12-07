from tkinter import *
import back

def view_command():
    list1.delete(0,END)
    for row in back.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in back.search(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()):
        list1.insert(END,row)

def add_command():
    back.insert(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
    list1.delete(0,END)
    list1.insert(END,(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()))

window=Tk()
window.title("Audio Book")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l1=Label(window,text="Author")
l1.grid(row=0,column=2)

l1=Label(window,text="Year")
l1.grid(row=1,column=0)

l1=Label(window,text="ISBN")
l1.grid(row=1,column=2)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

e2_val=StringVar()
e1=Entry(window,textvariable=e2_val)
e1.grid(row=0,column=3)

e3_val=StringVar()
e1=Entry(window,textvariable=e3_val)
e1.grid(row=1,column=1)

e4_val=StringVar()
e1=Entry(window,textvariable=e4_val)
e1.grid(row=1,column=3)

list1=Listbox(window,height=15,width=40)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All",width=14,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search",width=14,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=14,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=14)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=14)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=14)
b6.grid(row=7,column=3)

window.mainloop()
