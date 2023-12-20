import tkinter as tk
from tkinter import messagebox, Scale
import pickle
import warnings
warnings.filterwarnings("ignore")

# login and forgot pwd
def usr_signin():
    usr_name = var_name.get()
    usr_pwd = var_pwd.get()
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usr_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usr_info = {'admin':'admin'}
            pickle.dump(usr_info, usr_file)
    if usr_name in usr_info:
        if usr_pwd == usr_info[usr_name]:
            tk.messagebox.showinfo('Hello','Welcome Back!')
        else:
            forget_pwd = tk.messagebox.askyesno('Error','Incorrect Password!\nForget Password?')
            if forget_pwd:
                usr_forget()
    else:
        sign_up = tk.messagebox.askyesno('Error','User name not found. Sign up today?')
        if sign_up:
            usr_signup()
        
# signup page
def usr_signup():
    # new user check
    def new_usr():
        np = usr_pwd.get()
        npf = usr_pwd_cfm.get()
        nn = usr_name.get()
        with open('usr_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error','Passwords must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error','The user has existed!')
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome','You have successfully signed up!')
            window_signup.destroy()
            
    window_signup = tk.Toplevel(window)
    window_signup.geometry('450x300')
    window_signup.title('Sign Up')
    
    #pic
    global signup_canvas
    signup_canvas =tk.Canvas(window_signup, height=450, width=300)
    image_file = tk.PhotoImage(file='like.gif')
    img = signup_canvas.create_image(50,50, anchor='nw', image=image_file)
    signup_canvas.img = image_file
    signup_canvas.pack(side='top')
    
    #info
    global signup_name
    signup_name = tk.StringVar()
    signup_name.set('name@example.com')
    tk.Label(window_signup, text='User Name:').place(x=10,y=10)
    usr_name = tk.Entry(window_signup, textvariable=signup_name)
    usr_name.place(x=150, y=10)

    global signup_pwd
    signup_pwd = tk.StringVar()
    tk.Label(window_signup, text='Password:').place(x=10,y=50)
    usr_pwd = tk.Entry(window_signup, textvariable=signup_pwd, show='*')
    usr_pwd.place(x=150, y=50)
    
    signup_pwd_cfm = tk.StringVar()
    tk.Label(window_signup, text='Confirm Password:').place(x=10,y=90)
    usr_pwd_cfm = tk.Entry(window_signup, textvariable=signup_pwd_cfm, show='*')
    usr_pwd_cfm.place(x=150, y=90)
    
    #checkbox
    global c2
    c2 = tk.Checkbutton(window_signup, text='I have read and agree to the terms and conditions', onvalue=1, offvalue=0)
    c2.place(x=50, y=170)
    
    #slidebar
    global signup_slider
    tk.Label(window_signup, text="Satisfaction Level").place(x=50, y=280)
    signup_slider = Scale(window_signup, from_=0, to=100, orient=tk.HORIZONTAL)  
    signup_slider.place(x=50, y=240)
    
    #button
    btn_signup_cfm = tk.Button(window_signup, text='Sign Up', command=new_usr)
    btn_signup_cfm.place(x=150, y=130)
    
# reset password page
def usr_forget():
    window_forget = tk.Toplevel(window)
    window_forget.geometry('450x300')
    window_forget.title('Forget Password')
    
    #pic
    global forget_canvas
    forget_canvas =tk.Canvas(window_forget, height=450, width=300)
    image_file = tk.PhotoImage(file='question.gif')
    img = forget_canvas.create_image(50,50, anchor='nw', image=image_file)
    forget_canvas.img = image_file
    forget_canvas.pack(side='top')
    
    # info
    global forget_name
    forget_name = tk.StringVar()
    forget_name.set('name@example.com')
    tk.Label(window_forget, text='Email Address:').place(x=10,y=10)
    usr_name = tk.Entry(window_forget, textvariable=forget_name)
    usr_name.place(x=150, y=10)

    forget_name_cfm = tk.StringVar()
    tk.Label(window_forget, text='Confirm Email Address:').place(x=10,y=50)
    usr_name_cfm = tk.Entry(window_forget, textvariable=forget_name_cfm)
    usr_name_cfm.place(x=150, y=50)
    
    # code 
    global otp_code
    otp_code = tk.StringVar()
    tk.Label(window_forget, text='One Time Code:').place(x=10,y=120)
    entry_code = tk.Entry(window_forget, textvariable=otp_code)
    entry_code.place(x=150, y=120)
    
    #checkbox
    global c3
    c3 = tk.Checkbutton(window_forget, text='I have read and agree to the terms and conditions', onvalue=1, offvalue=0)
    c3.place(x=50, y=180)
    
    #slidebar
    global forget_slider
    tk.Label(window_forget, text="Satisfaction Level").place(x=50, y=280)
    forget_slider = Scale(window_forget, from_=0, to=100, orient=tk.HORIZONTAL)  
    forget_slider.place(x=50, y=240)
    
    # button
    btn_get_code = tk.Button(window_forget, text='Get Code')
    btn_get_code.place(x=150, y=80)
    btn_rest_pwd = tk.Button(window_forget, text='Rest Password')
    btn_rest_pwd.place(x=150, y=150)

window = tk.Tk()
window.title("Sign In Page")
window.geometry("450x300")

# welcome image
canvas =tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User Name:').place(x=50, y = 150)
tk.Label(window, text='Password:').place(x=50, y = 190)

var_name = tk.StringVar()
var_name.set('name@example.com')
usr_name = tk.Entry(window, textvariable=var_name)
usr_name.place(x=160, y=150)

var_pwd = tk.StringVar()
usr_pwd = tk.Entry(window, textvariable=var_pwd, show='*')
usr_pwd.place(x=160, y=190)

# checkbox
c1 = tk.Checkbutton(window, text='I have read and agree to the terms and conditions', onvalue=1, offvalue=0)
c1.place(x=50, y=220)

# Slider from age 10 to 100
tk.Label(window, text="Satisfaction Level").place(x=50, y=280)
sat_slider = Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)  
sat_slider.place(x=50, y=240)

# button
btn_login = tk.Button(window, text='Sign In', command = usr_signin)
btn_login.place(x=170, y = 250)

btn_signup = tk.Button(window, text='Sign Up', command = usr_signup)
btn_signup.place(x=270, y = 250)

if __name__ == '__main__':
    window.mainloop()