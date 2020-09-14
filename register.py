from tkinter import *
from tkinter import messagebox
from indexed import *
import mini


    

def registers():

    def reg():
        if(len(Text6.get())!=0 and len(Text7.get())!=0 and len(Text4.get())!=0 and len(Text5.get())!=0 ):
            mini.ins_mem(Text6.get(),Text7.get(),Text4.get(),Text5.get())
            window.destroy()
            indexed()
        else:
             messagebox.showinfo("Error","All fields should be filled")
    
    window=Tk()
    window.minsize(width=400,height=400)
    window.geometry("800x500")

    Canvas1 = Canvas(window)
        
    Canvas1.config(bg="#517569")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(window,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Register Now!!", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    window.wm_title("Library")

    labelFrame = Frame(window,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)
    
                
    # password
    lb6 = Label(labelFrame,text="Date: ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.1, relheight=0.08)

    Text6 = Entry(labelFrame)
    Text6.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)

    lb7 = Label(labelFrame,text="Name", bg='black', fg='white')
    lb7.place(relx=0.05,rely=0.25, relheight=0.08)

    Text7 = Entry(labelFrame)
    Text7.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="Phone no.", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.4, relheight=0.08)

    Text4 = Entry(labelFrame)
    Text4.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)

    lb5 = Label(labelFrame,text="Password:", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.55, relheight=0.08)

    Text5 = Entry(labelFrame)
    Text5.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)


    Register= Button(window,text="Register",bg='#d1ccc0', fg='black',command=reg)
    Register.place(relx=0.5,rely=0.75, relwidth=0.18,relheight=0.08)

    window.mainloop()


