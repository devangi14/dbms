from tkinter import *
from tkinter import messagebox
from donate import *
from issue import *
import mini

def paym():
    def view_pay():
        list1.delete(0,END)
        for row in mini.payment():
            list1.insert(END,row)

    def search_pay():
        list1.delete(0,END)
        for row in mini.search_pay(memid.get()):
            list1.insert(END,row)

    def pay():
        mini.payd(payid.get())
        messagebox.showinfo("Success","Payment Successfull")

    window=Tk()
    window.minsize(width=400,height=400)
    window.geometry("800x500")

    Canvas1 = Canvas(window)

    Canvas1.config(bg="#517569")
    Canvas1.pack(expand=True,fill=BOTH)
    window.wm_title("Library")

    lb1 = Label(window,text="User ID : ", bg='#517569', fg='white')
    lb1.place(relx=0.1,rely=0.05, relheight=0.08)
                    
    memid = Entry(window)
    memid.place(relx=0.2,rely=0.05, relwidth=0.25, relheight=0.08)

    lb2 = Label(window,text="Payment ID: ", bg='#517569', fg='white')
    lb2.place(relx=0.48,rely=0.05, relheight=0.08)
                    
    payid = Entry(window)
    payid.place(relx=0.6,rely=0.05, relwidth=0.25, relheight=0.08)

    list1=Listbox(window)
    list1.place(relx=0.05,rely=0.25,relwidth=0.5,relheight=0.6)

    sb1=Scrollbar(window)
    sb1.place(relx=0.55,rely=0.25,relwidth=0.03,relheight=0.6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    btn1 = Button(window,text="View Payment details of All",bg='black', fg='white',command=view_pay)
    btn1.place(relx=0.65,rely=0.35, relwidth=0.25,relheight=0.1)

    btn2 = Button(window,text="Search by Id",bg='black', fg='white',command=search_pay)
    btn2.place(relx=0.65,rely=0.50, relwidth=0.25,relheight=0.1)

    btn3 = Button(window,text="Pay Fine",bg='black', fg='white',command=pay)
    btn3.place(relx=0.65,rely=0.65, relwidth=0.25,relheight=0.1)


    window.mainloop()


