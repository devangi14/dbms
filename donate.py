from tkinter import *
from tkinter import messagebox

import mini

def donate():
    def don():
        mini.ins_book(book_nm.get(),amount.get(),author.get())
        messagebox.showinfo("Success","Thank You For Donating")
        
        
    window=Tk()
    window.minsize(width=400,height=400)
    window.geometry("800x500")

    Canvas1 = Canvas(window)
            
    Canvas1.config(bg="#517569")
    Canvas1.pack(expand=True,fill=BOTH)



    headingFrame1 = Frame(window,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Donate Now!!", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    window.wm_title("Library")

    labelFrame = Frame(window,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)
                        

    lb7 = Label(labelFrame,text=" Book Name", bg='black', fg='white')
    lb7.place(relx=0.05,rely=0.25, relheight=0.08)

    book_nm = Entry(labelFrame)
    book_nm.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="Amount", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.4, relheight=0.08)

    amount= Entry(labelFrame)
    amount.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)

    lb5 = Label(labelFrame,text="Author", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.55, relheight=0.08)

    author = Entry(labelFrame)
    author.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)


    donate= Button(window,text="Donate",bg='#d1ccc0', fg='black',command=don)
    donate.place(relx=0.5,rely=0.75, relwidth=0.18,relheight=0.08)

    window.mainloop()
