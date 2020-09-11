from tkinter import *
from tkinter import messagebox
from donate import *
from issue import *
from pay import *
import mini

  

def index():

    def pay():
        mini.fine()
        mini.upd_payid()
        paym()
        
    window=Tk()
    window.minsize(width=400,height=400)
    window.geometry("800x500")

    Canvas1 = Canvas(window)
        
    Canvas1.config(bg="#517569")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(window,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="INDEX!!", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    window.wm_title("Library")

    btn1 = Button(window,text="Issue/Return Book",bg='black', fg='white',command=iss)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(window,text="Donate Books",bg='black', fg='white',command=donate)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(window,text="View Pending Payment",bg='black', fg='white',command=pay)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        
   

    window.mainloop()
