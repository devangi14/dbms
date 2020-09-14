import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from donate import *
from indexed import *

import mini

def iss():

    def view_command():
        list1.delete(0,END)
        for row in mini.book():
            list1.insert(END,row)

    def back():
        window.destroy()
        index()

    def issue():
        if(len(bookid.get())!=0 and len(memid.get())!=0 and len(date.get())!=0 ):
            res=mini.avail(bookid.get()," ")
            if(res[1]==0):
                mini.ins_issue(memid.get(),bookid.get(),date.get())
                result=mini.ret_date(date.get()," ")
                mini.ins_return(bookid.get(),memid.get(),result[1],1)
                messagebox.showinfo("Success","book Issued")
            else:
                messagebox.showinfo("Error","Book Already issued by someone")
        else:
            messagebox.showinfo("Error","All 3 field must be filled")

    def ret():
        if(len(bookid.get())!=0 and len(memid.get())!=0 ):
            mini.ret_bk(memid.get(),bookid.get())
            messagebox.showinfo("Success","book Returned")
        else:
            messagebox.showinfo("Error","Member id and book id are not to be left empty")

    def search():
        list1.delete(0,END)
        row=mini.search(name.get())
        print(len(row))
        if(len(row)!=0):
            for rows in row:
                list1.insert(END,rows)
        else:
            messagebox.showinfo("Error","Book not found")

    window=Tk()
    window.minsize(width=400,height=400)
    window.geometry("800x500")

    Canvas1 = Canvas(window)
                
    Canvas1.config(bg="#517569")
    Canvas1.pack(expand=True,fill=BOTH)
    window.wm_title("Library")

    lb1 = Label(window,text="User ID : ", bg='#517569', fg='white')
    lb1.place(relx=0.05,rely=0.05, relheight=0.08)
                    
    memid = Entry(window)
    memid.place(relx=0.12,rely=0.05, relwidth=0.15, relheight=0.08)

    lb2 = Label(window,text="Book ID : ", bg='#517569', fg='white')
    lb2.place(relx=0.3,rely=0.05, relheight=0.08)
                    
    bookid = Entry(window)
    bookid.place(relx=0.4,rely=0.05, relwidth=0.15, relheight=0.08)

    lb3 = Label(window,text="Issue Date : ", bg='#517569', fg='white')
    lb3.place(relx=0.6,rely=0.05, relheight=0.08)
                    
    date= Entry(window)
    date.place(relx=0.7,rely=0.05, relwidth=0.15, relheight=0.08)

    #tree = ttk.Treeview(window, columns=('#0','#1','#2'))
    #tree.place(relx=0.05,rely=0.25,relwidth=0.5,relheight=0.6)

    #tree.heading('#0', text='Item')
    #tree.heading('#1', text='Name')
    #tree.heading('#2', text='ID')
   

    list1=Listbox(window)
    list1.place(relx=0.05,rely=0.25,relwidth=0.5,relheight=0.6)

    sb1=Scrollbar(window)
    sb1.place(relx=0.55,rely=0.25,relwidth=0.03,relheight=0.6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    btn1 = Button(window,text="View Books",bg='black', fg='white',command=view_command)
    btn1.place(relx=0.65,rely=0.25, relwidth=0.25,relheight=0.1)

    btn2 = Button(window,text="Issue",bg='black', fg='white',command=issue)
    btn2.place(relx=0.65,rely=0.40, relwidth=0.25,relheight=0.1)

    btn3 = Button(window,text="Return",bg='black', fg='white',command=ret)
    btn3.place(relx=0.65,rely=0.55, relwidth=0.25,relheight=0.1)

    btn4 = Button(window,text="Search",bg='black', fg='white',command=search)
    btn4.place(relx=0.63,rely=0.72, relwidth=0.12,relheight=0.1)

    name = Entry(window)
    name.place(relx=0.77,rely=0.72, relwidth=0.15, relheight=0.1)
    window.mainloop()
        
