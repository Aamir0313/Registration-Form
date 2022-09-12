#from cgitb import text
#from re import L
from tkinter import*
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x800")
root.resizable(False, False)
root.title("Floting Mind Infotech")

def aamir():
    fstname = firstname_info.get()
    lstname = lastname_info.get()
    number = mobilenumber_info.get()
    date = dateofbirth_info.get()
    email = email_info.get()
    gender = gender_info.get()
    city = city_info.get()
    state = state_info.get()
    qualification = qualification_info.get()
    course = course_info.get()

    with open("FMI Records.text", "a") as f:
        f.write("First Name: "+fstname+"\n")
        f.write("Last Name: "+lstname+"\n")
        f.write("Mobile No: "+number+"\n")
        f.write("Date of Birth: "+date+"\n")
        f.write("Email: "+email+"\n")
        f.write("Gender: "+gender+"\n")
        f.write("City: "+city+"\n")
        f.write("State: "+state+"\n")
        f.write("Qualification: "+qualification+"\n")
        f.write("Course: "+course+"\n""\n")

    if fstname=="":
        messagebox.showerror("Error", "Please enter your first name")
    elif lstname=="":
        messagebox.showerror("Error", "Please enter your last name")
    elif number=="":
        messagebox.showerror("Error","Please enter your mobile number")
    elif date=="":
        messagebox.showerror("Error","Please enter your date of birth")
    elif email=="":
        messagebox.showerror("Error","Please enter your Email")
    elif gender=="":
        messagebox.showerror("Error", "Please enter your Gender")
    elif city=="":
        messagebox.showerror("Error","Please enter your City")
    elif state=="":
        messagebox.showerror("Error", "Please enter your State")
    elif qualification=="":
        messagebox.showerror("Error", "Please enter your Qualification")
    elif course=="":
        messagebox.showerror("Error", "Please enter the Course")
    else:
        messagebox.showinfo("Success", "Registration Succesfull")


frm = Frame(root, bg="green", width=280, height=30)
frm.place(x=0, y=110)

register = Label(frm, text="Registration Form", bg="green", fg="white", font="Helvitica 15 bold")
register.place(x=50, y=0)

title = Label(root, text="Fill out the form for registration", font="arial 10", pady=5)
title.place(x=40, y=140)

firstname_var = Label(root, text="First Name :")
firstname_var.place(x=10, y=170)
lastname_var = Label(root, text="Last Name :")
lastname_var.place(x=10, y=200)
mobilenumber_var = Label(root, text="Mobile Number :").place(x=0, y=230)
dateofbirth_var = Label(root, text="Date of Birth :").place(x=10, y=260)
email_var = Label(root, text="Email :").place(x=10, y=290)
gender_var = Label(root, text="Gender :").place(x=10, y=320)
city_var = Label(root, text="City :").place(x=10, y=350)
state_var = Label(root, text="State :").place(x=10, y=380)
qualification_var = Label(root, text="Qualification :").place(x=10, y=410)
course_var = Label(root, text="Course :").place(x=10, y=440)

firstname_info = StringVar()
lastname_info = StringVar()
mobilenumber_info = StringVar()
dateofbirth_info = StringVar()
email_info = StringVar()
gender_info = StringVar()
city_info = StringVar()
state_info = StringVar()
qualification_info = StringVar()
course_info = StringVar()

firstname_entry = Entry(root, textvariable=firstname_info, bd=3 ,font="3").place(x=90, y=170)
lastname_entry = Entry(root, textvariable=lastname_info, bd=3 , font="3").place(x=90, y=200)
mobilenumber_entry = Entry(root, textvariable=mobilenumber_info, bd=3, font="3").place(x=90, y=230)
dateofbirth_entry = Entry(root, textvariable=dateofbirth_info, bd=3, font="3").place(x=90, y=260)
email_entry = Entry(root, textvariable=email_info, bd=3, font="3").place(x=90, y=290)
gender_entry = Entry(root, textvariable=gender_info, bd=3, font="3").place(x=90, y=320)
city_entry = Entry(root, textvariable=city_info, bd=3, font="3").place(x=90, y=350)
state_entry = Entry(root, textvariable=state_info, bd=3, font="3").place(x=90, y=380)
qualification_entry = Entry(root, textvariable=qualification_info, bd=3, font="3").place(x=90, y=410)
course_entry = Entry(root, textvariable=course_info, bd=3, font="3").place(x=90, y=440)

checkbox = IntVar()
checkbox = Checkbutton(root, text="I agree to the Terms of Use", variable=checkbox)
checkbox.place(x=30, y=470)


button = Button(text="Submit",font="arial 10 bold", borderwidth=7, width=15, height=1, command=aamir)
button.place(x=90, y=500)

image1 = Image.open("Static/FMI01.jpg")
image1 = image1.resize((300,100))
photo = ImageTk.PhotoImage(image1)
var_label = Label(image=photo)
var_label.place(x=0, y=0)


Label(root, text="GET YOUR DREAM JOB\n IN JUST 90 DAYS", bg="Dark turquoise", fg="white", font=("Lucida",20,font.BOLD), width="30", height="3",).pack(side=RIGHT, anchor="n")

title1= Label(root, text=">>>>>>>  OUR COURSES  <<<<<<<", font="arial 22 bold", fg="green")
title1.place(x=300, y=110)

f1 = Frame(root, bg="Dark turquoise", highlightbackground="green", highlightthickness=2, borderwidth=5, relief=SUNKEN, width=330, height=360)
f1.place(x=297, y=160)

course1 = Label(f1, text="Digital Marketing Course",font="Arial 18 bold", bg="Dark turquoise", fg="white")
course1.place(x=10, y=20)
Label(f1, text="HR Training Course",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=50)
Label(f1, text="JAVA",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=80)
Label(f1, text="C/C++",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=110)
Label(f1, text="Python",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=140)
Label(f1, text="Software Testing",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=170)
Label(f1, text="Salesforce",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=200)
Label(f1, text="Data Science",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=230)
Label(f1, text="Spoken English",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=260)
Label(f1, text="Personality Development",font="Arial 18 bold", bg="Dark turquoise", fg="white").place(x=10, y=290)

image2 = Image.open("Static/img01.jpg")
image2 = image2.resize((170,110))
img01 = ImageTk.PhotoImage(image2)
var = Label(image=img01)
var.place(x=630, y=160)

image3 = Image.open("Static/img02.jpg")
image3 = image3.resize((170,110))
img02 = ImageTk.PhotoImage(image3)
var = Label(image=img02)
var.place(x=630, y=283)

image4 = Image.open("Static/img03.jpg")
image4 = image4.resize((170,110))
img03 = ImageTk.PhotoImage(image4)
var = Label(image=img03)
var.place(x=630, y=407)


f2 = Frame(root, bg="Dark turquoise", width=800, height=50)
f2.place(x=0, y=570)

Label(f2, text="100% Practical\nTraining",font="Arial 13 bold", bg="Dark turquoise", fg="white").place(x=50, y=2)
Label(f2, text="100% Placement\nAssistance",font="Arial 13 bold", bg="Dark turquoise", fg="white").place(x=330, y=2)
Label(f2, text="Internship\nCertificate",font="Arial 13 bold", bg="Dark turquoise", fg="white").place(x=650, y=2)


Label(root, text="The Only Company, Who Will Not Leave You,",font="Arial 12").place(x=210, y=620)
Label(root, text="Until You Get Your Dream Job.",font="Arial 22 bold",fg="Dark turquoise").place(x=150, y=650)

Label(root, text='''ADDRESS: City Plaza building, 2nd floor above Crystal Optics, Pune - Solapur Rd,
            \n Near HDFC Bank Hadapsar, Pune, Maharashtra 411028.'''
                ,font="Arial 12 ").place(x=10, y=690)

Label(root, text="Contact No:",font="Arial 15 bold").place(x=640, y=650)
Label(root, text="+91 8766966433\n +91 9511804321",font="Arial 18 bold").place(x=600, y=680)

f3 = Frame(root, bg="Dark turquoise", width=800, height=30)
f3.place(x=0, y=770)

Label(f3, text='''Our Branches:    Hadapsar   |   Karve Nagar   |   Sangli   |   Baramati   |   Nashik   |   Belgam    |    Goa'''
                , font="Arial 12", bg="Dark turquoise", fg="white" ).place(x=50, y=5)


root.mainloop()
