from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
root.title('Login')
root.geometry("950x500+300+200")
root.configure(bg='#fff')
root.iconbitmap('window.ico')
root.resizable(False,False)

# Functional part
def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())
    #if username=='admin' and password=='1234':
    if username in r.keys() and password == r[username]:
        print("Successfully Login")
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg='white')

        Label(screen,text='Congratulations!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

    # elif username!='admin' and password!='1234':
    #     messagebox.showerror("Invalid","Invalid usrname and password")
    # elif password!="1234":
    #     messagebox.showerror("Invalid","Invalid password")
    # elif username!='admin':
    #     messagebox.showerror("Invalid","Invalid username")
    else:
        messagebox.showerror('Invalid','Invalid username or password')


def signup_page():
    root.destroy()
    import signup


img=PhotoImage(file='login.png')
label=Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=500,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light',23,'bold')).place(x=100,y=5)
############_________________________________________
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',bd=0,bg='white',font=('Microsoft YaHei UI light',11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black',).place(x=25,y=107)

##############___________________________________________

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'password')

code=Entry(frame,width=25,border=0,fg='black',bg='white',font=('Microsoft YaHei UI light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black',).place(x=25,y=177)

##################________________________________________________________
signin=Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',bd=0,command=signin).place(x=35,y=204)
Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI light',9)).place(x=75,y=270)

signup=Button(frame,width=6,text='Sign up',bd=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_page)
signup.place(x=215,y=270)

root.mainloop()
