from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title('Signup')
window.geometry("950x500+300+200")
window.configure(bg='#fff')
window.iconbitmap('window.ico')
window.resizable(False,False)

def signup():
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()

    if password==confirm_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.twindowcate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo('signup','successfully sign up')

        except:
            file=open('datasheet.txt','w')
            pp=str({username:password})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid',"Both password should match")

def sign_in():
    window=Toplevel()
    window.destroy()

#################_____________________________________________________
img = PhotoImage(file='Signup.png')
Label(window,image=img,border=0,bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg='white')
frame.place(x=480, y=50)

heading = Label(frame,text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI light',23,'bold')).place(x=50, y=5)
############_________________________________________
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame, width=25, fg='black',border=0, bg='white',font=('Microsoft YaHei UI light',11))
user.place(x=30, y=80)
user.insert(0,'username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295, height=2, bg='black',).place(x=25,y=107)

##############___________________________________________

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'password')

code = Entry(frame, width=25,border=0,fg='black',bg='white',font=('Microsoft YaHei UI light',11))
code.place(x=30, y=150)
code.insert(0,'password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=295, height=2, bg='black',).place(x=25, y=177)

##################________________________________________________________
def on_enter(e):
    confirm_code.delete(0,'end')
def on_leave(e):
    name=confirm_code.get()
    if name=='':
        confirm_code.insert(0,'confirm password')

confirm_code = Entry(frame, width=25, fg='black',border=0, bg='white',font=('Microsoft YaHei UI light',11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0,'confirm password')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)


Frame(frame,width=295, height=2, bg='black',).place(x=25,y=247)


######################______________________________________________________
Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="I have an account",fg='blue',bg='white',font=('Microsoft YaHei UI light',9))
label.place(x=90, y=350)

sign_in = Button(frame, width=6, text='Sign in',border=2,bg='white',cursor='hand2',fg='#57a1f8',command=sign_in).place(x=200,y=350)

window.mainloop()