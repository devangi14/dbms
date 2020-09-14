from tkinter import *
from tkinter import messagebox
from register import *
from indexed import *
import mini

def login():
    if(len(Text1.get())!=0 and len(Text2.get())!=0):
        result=mini.login(Text1.get(),Text2.get()," ")
        if(result[2]==0):
            messagebox.showinfo("Error","Try Again")
        else:
            window.iconify()
            indexed()
    else:
        messagebox.showinfo("Error","All fields should be filled")
def reg():
    window.destroy()
    registers()
        
        


window=Tk()
window.minsize(width=400,height=400)
window.geometry("800x500")

Canvas1 = Canvas(window)
    
Canvas1.config(bg="#517569")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(window,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n DataFlair Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

window.wm_title("Library")

labelFrame = Frame(window,bg='black')
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
# Username
lb1 = Label(labelFrame,text="User ID : ", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.2, relheight=0.08)
            
Text1 = Entry(labelFrame)
Text1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
            
# password
lb2 = Label(labelFrame,text="Password : ", bg='black', fg='white')
lb2.place(relx=0.05,rely=0.35, relheight=0.08)

Text2 = Entry(labelFrame,show="*")
Text2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        


Login= Button(window,text="Login",bg='#d1ccc0', fg='black',command=login)
Login.place(relx=0.3,rely=0.65, relwidth=0.18,relheight=0.08)

Register= Button(window,text="Register",bg='#d1ccc0', fg='black',command=reg)
Register.place(relx=0.5,rely=0.65, relwidth=0.18,relheight=0.08)

window.mainloop()

