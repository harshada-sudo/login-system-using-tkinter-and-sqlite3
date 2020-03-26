import tkinter as tk,time
import sqlite3

window=tk.Tk()
window.title("Home Page")
window.geometry('300x250')

'''#show information in database
    def show():
    with sqlite3.connect("User_info.db") as db:
        cursor=db.cursor()

    cursor.execute("SELECT * ,oid FROM user_info")
    print(cursor.fetchall())
    db.commit()
'''    

#create login function
def login_user():
    with sqlite3.connect("User_info.db") as db:
        cursor=db.cursor()

        u_name=user_name_login.get()
        pass_=password_login.get()
        
        find_user="""SELECT * FROM user_info WHERE user_name =? and password=?"""
        cursor.execute(find_user,[(u_name),(pass_)])
        record=cursor.fetchall()

        print_str=' '
        if record:
            for i in record:
                print_str +="Welcome "+i[1]
        else:
            display_error=tk.Label(login_wnd,text="Invalid username and password ! ",font=("times new roman",10,"bold"))
            display_error.grid(row=3,column=0)

        user_name_login.delete(0,tk.END)    
        password_login.delete(0,tk.END)

        display=tk.Label(login_wnd,text=print_str,font=("times new roman",10,"bold"))
        display.grid(row=3,column=0)

        db.commit()
           

def login():
    global login_wnd
    login_wnd=tk.Tk()
    login_wnd.title("Login Page")
    login_wnd.geometry('350x400')

    global user_name_login
    global password_login
    #create text boxes
    user_name_login=tk.Entry(login_wnd,width=30)
    user_name_login.grid(row=0,column=1,columnspan=2,padx=10,pady=10)

    password_login=tk.Entry(login_wnd,width=30)
    password_login.grid(row=1,column=1,columnspan=2,padx=10,pady=10)

    #create label for text boxes
    user_name_login_lbl=tk.Label(login_wnd,text="User Name",font=("times new roman",10,"bold"))
    user_name_login_lbl.grid(row=0,column=0)

    password_login_lbl=tk.Label(login_wnd,text="Password",font=("times new roman",10,"bold"))
    password_login_lbl.grid(row=1,column=0)
    
    #create login button
    login_button=tk.Button(login_wnd,text="Login",width=30,command=login_user)
    login_button.grid(row=2,column=0,columnspan=2,ipadx=60)

    login_wnd.mainloop()

#create submit function
def submit():
    with sqlite3.connect("User_info.db") as db:
        cursor=db.cursor()

    cursor.execute("""INSERT INTO user_info VALUES(:user_name,:first_name,:last_name,:phone,:email,:password)""",
    {
        'user_name' :user_name.get(),
        'first_name' : first_name.get(),
        'last_name' : last_name.get(),
        'phone' : phone.get(),
        'email' : email.get(),
        'password' : password.get()
    }
    )
    db.commit()  
    registration_wnd.destroy()  

#create registration function
def registration():
    #create new registration window
    global registration_wnd
    registration_wnd=tk.Tk()
    registration_wnd.title("Registration Page")
    registration_wnd.geometry('350x400')

    global first_name
    global last_name
    global phone
    global email
    global password
    global user_name
    #create text boxes
    user_name=tk.Entry(registration_wnd,width=30)
    user_name.grid(row=0,column=1,columnspan=2,padx=10,pady=10)

    first_name=tk.Entry(registration_wnd,width=30)
    first_name.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
    
    last_name=tk.Entry(registration_wnd,width=30)
    last_name.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

    phone=tk.Entry(registration_wnd,width=30)
    phone.grid(row=3,column=1,columnspan=2,padx=10,pady=10)

    email=tk.Entry(registration_wnd,width=30)
    email.grid(row=4,column=1,columnspan=2,padx=10,pady=10)

    password=tk.Entry(registration_wnd,width=30)
    password.grid(row=5,column=1,columnspan=2,padx=10,pady=10)


    #create labels for text boxes
    user_name_lbl=tk.Label(registration_wnd,text="User Name",font=("times new roman",10,"bold"))
    user_name_lbl.grid(row=0,column=0)

    first_name_lbl=tk.Label(registration_wnd,text="First Name",font=("times new roman",10,"bold"))
    first_name_lbl.grid(row=1,column=0)

    last_name_lbl=tk.Label(registration_wnd,text="Last Name",font=("times new roman",10,"bold"))
    last_name_lbl.grid(row=2,column=0)

    phone_lbl=tk.Label(registration_wnd,text="Phone Number",font=("times new roman",10,"bold"))
    phone_lbl.grid(row=3,column=0)

    email_lbl=tk.Label(registration_wnd,text="Email",font=("times new roman",10,"bold"))
    email_lbl.grid(row=4,column=0)

    password_lbl=tk.Label(registration_wnd,text="Password",font=("times new roman",10,"bold"))
    password_lbl.grid(row=5,column=0)

    #create submit button
    submit_btn=tk.Button(registration_wnd,text="Submit",width=30,command=submit)
    submit_btn.grid(row=7,column=0,columnspan=2,ipadx=60)

    registration_wnd.mainloop()

#create two buttons for login and registration
login_btn=tk.Button(window,text="Login",font=("times new roman",20,"bold"),bg="red",fg="white",command=login)
login_btn.grid(row=0,column=0,padx=10,pady=20,ipadx=80,columnspan=2)

registration_btn=tk.Button(window,text="Registration",font=("times new roman",20,"bold"),bg="red",fg="white",command=registration)
registration_btn.grid(row=1,column=0,padx=10,pady=10,ipadx=40,columnspan=2)

'''show_btn=tk.Button(window,text="Show Data",command=show)
show_btn.grid(row=2,column=0,padx=10,pady=10,ipadx=40,columnspan=2)'''
window.mainloop()