from time import sleep
from tkinter import *
from filelock import sys
import mysql.connector
from tkinter import messagebox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import re

my_db =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "formfiller",
    port = 3308
)

print(my_db)
mycursor = my_db.cursor()
sql = "INSERT INTO records (ID, Name, Password, Email, Gender, Number) VALUES (NULL, %s, %s, %s, %s, %s);"


signup_list=[]
global timer
def signup():
    global signup_list
    uname=username_signup.get()
    pwd=password_signup.get()
    email=email_signup.get()
    gender=gender_signup.get()
    number = number_signup.get()
    if uname=='' or pwd=='':
        messagebox.showerror("Error","Enter User Name And Password",parent=signup_screen)
          
    else:
          signup_list.append(uname)
          signup_list.append(pwd)
          signup_list.append(email)
          signup_list.append(gender)
          signup_list.append(number)
          print(signup_list) 
          vals = tuple(signup_list)
          print(vals)
          mycursor.execute(sql,vals)
          my_db.commit()
          print(mycursor.rowcount, "details inserted")
          messagebox.showinfo("success","details Inserted",parent = signup_screen)
    
def signupform():
    global signup_screen
    signup_screen = Tk()
    signup_screen.title("Signup Form")
    signup_screen.geometry("600x450")
    global  message_signup
    global username_signup
    global password_signup
    global email_signup
    global gender_signup
    global number_signup
    username_signup = StringVar()
    password_signup = StringVar()
    email_signup = StringVar()
    gender_signup= StringVar()
    number_signup= StringVar()
    message_signup=StringVar()
    Label(signup_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    Label(signup_screen, text="Username * ",font=("Arial", 15)).place(x=60,y=40)
    Entry(signup_screen, textvariable=username_signup).place(x=300,y=40,width=150,height=30)
    Label(signup_screen, text="Password * ",font=("Arial", 15)).place(x=60,y=90)
    Entry(signup_screen, textvariable=password_signup,show="*").place(x=300,y=90,width=150,height=30)
    Label(signup_screen, text="Email * ",font=("Arial", 15)).place(x=60,y=140)
    Entry(signup_screen, textvariable=email_signup).place(x=300,y=140,width=150,height=30)
    Label(signup_screen, text="Gender * ",font=("Arial", 15)).place(x=60,y=190)
    Entry(signup_screen, textvariable=gender_signup).place(x=300,y=190,width=150,height=30)
    Label(signup_screen, text="Number * ",font=("Arial", 15)).place(x=60,y=240)
    Entry(signup_screen, textvariable=number_signup).place(x=300,y=240,width=150,height=30)
    Label(signup_screen, text="",textvariable=message_signup).place(x=300,y=400)
    Button(signup_screen, text="Signup", width=10, height=1, bg="orange",command=signup).place(x=300,y=300)
    Button(signup_screen, text="login", width=10, height=1, bg="orange",command=signup_screen.destroy).place(x=300,y=350)
    Button(signup_screen, text="exit", width=10, height=1, bg="orange",command=exitsignup).place(x=300,y=370)
    signup_screen.mainloop()
    
    
sql1 = "SELECT * FROM records WHERE Name = %s AND Password = %s;"

login_list=[]

def login():
    
    uname=username_login.get()
    pwd=password_login.get()
    print(uname,pwd)
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      login_list.append(uname)  
      login_list.append(pwd)
      tip = tuple(login_list)
      print(tip)
      mycursor.execute(sql1, tip)
      result = mycursor.fetchone()
      if result == None:
          messagebox.showerror("Error", "Wrong Username or Password", parent=login_screen)
          login_list.clear()
       
      else:
          messagebox.showinfo("Success", "Log in Successful", parent=login_screen)
          login_screen.destroy()
       
def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("300x300")
    global  message
    global username_login
    global password_login
    username_login = StringVar()
    password_login = StringVar()
    message=StringVar()
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    Label(login_screen, text="Username * ").place(x=20,y=40)
    Entry(login_screen, textvariable=username_login).place(x=90,y=42)
    Label(login_screen, text="Password * ").place(x=20,y=80)
    Entry(login_screen, textvariable=password_login,show="*").place(x=90,y=82)
    Label(login_screen, text="",textvariable=message).place(x=105,y=170)
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    Button(login_screen, text="exit", width=10, height=1, bg="orange",command=exitlogin).place(x=105,y=150)
    login_screen.mainloop()
  
    
 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
def check(email):

    if(re.search(regex,email)):
        return 1

    else:
        return 0

def fetchstatement(name):
    name = "'" + name + "'"
    statement = "Select * from records where name = "
    st = statement + name
    return st
   
def googleform_action():
    link=formlink.get()
    uname = username_login.get()

    mycursor.execute(fetchstatement(uname))
    result = mycursor.fetchone()
    print(result)



    driver = webdriver.Edge(executable_path=r"C:\Users\navne\Desktop\Projects\Filler-main\edgedriver_win64\msedgedriver.exe")
    driver.get(link)
    
    wait = WebDriverWait(driver,4)
    textboxes = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "whsOnd.zHQkBf")))
    sleep(2)
    counter = 1
    textcounter = 0
    for i in range(len(textboxes)):
        id = "i"
        id = id + str(counter)
        elements = driver.find_element(By.ID, id)
        if "name" in (str(elements.text)).lower():
            textboxes[textcounter].send_keys(result[1])
        elif "mail" in (str(elements.text)).lower():
            if check(result[3]) == 1:
                textboxes[textcounter].send_keys(result[3])
            else:
                print("E-mail NULL or faulty")
        elif "number" in (str(elements.text)).lower():
            if len(str(result[5])) == 10:
                textboxes[textcounter].send_keys(int(result[5]))
            else:
                print("Phone number NULL or faulty")
        elif "gender" in (str(elements.text)).lower():
            if result[4] == None:
                print("The gender is not defined")
            else:
                textboxes[textcounter].send_keys((result[4]))
            
        counter = counter + 4
        textcounter = textcounter + 1
    a = input("press any key to continue...")
    driver.quit()
    exit()
    sys.exit()
    
    print(link)

def exitform():
    global timer
    googleform_screen.destroy()
    timer=False
    
def exitlogin():
    global timer
    login_screen.destroy()
    timer=False
    
def exitsignup():
    global timer
    signup_screen.destroy()
    timer=False
    
    
    

    
def googleform():
    
    global googleform_screen
    googleform_screen = Tk()
    googleform_screen.title("form Form")
    googleform_screen.geometry("400x400")
    global  formlink
    formlink = StringVar()
    Label(googleform_screen,width="300", text="Please enter the form link", bg="orange",fg="white").pack()
    Label(googleform_screen, text="Link * ",font=("Arial", 15)).place(x=60,y=40)
    Entry(googleform_screen, textvariable=formlink).place(x=130,y=40,width=250,height=30)
    Button(googleform_screen, text="Submit", width=10, height=1, bg="orange",command=googleform_action).place(x=170,y=180)
    Button(googleform_screen, text="logout", width=10, height=1, bg="orange",command=googleform_screen.destroy).place(x=170,y=220)
    Button(googleform_screen, text="exit", width=10, height=1, bg="orange",command=exitform).place(x=170,y=260)
    googleform_screen.mainloop()
    
   
    
timer=True
while(timer==True):
    signupform()
    Loginform()
    googleform()

