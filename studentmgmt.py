from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
from tkinter import filedialog
from fpdf import FPDF
import os
import sqlite3



root=Tk()
root.geometry("1520x790+0+0")
root.title("Student management system")
# root.bind("<Escape>", roo0)

image1=Image.open("IITG1.jpg")
resize_img1=image1.resize((500,200),Image.LANCZOS)
photo1=ImageTk.PhotoImage(resize_img1)
#LANCZOS is used image chota ya bada hone ke phate nhi like maintain aspect ratio
label_photo1=Label(image=photo1)
label_photo1.place(x=0,y=0,width=500,height=200)

image2=Image.open("IITG2.jpg")
resize_img2=image2.resize((500,200),Image.LANCZOS)
photo2=ImageTk.PhotoImage(resize_img2)
label_photo2=Label(image=photo2)
label_photo2.place(x=500,y=0,width=500,height=200)


image3=Image.open("Students.jpeg")
resize_img3=image3.resize((520,200),Image.LANCZOS)
photo3=ImageTk.PhotoImage(resize_img3)
label_photo3=Label(image=photo3)
label_photo3.place(x=1000,y=0,width=520,height=200)

image4=Image.open("IITG1.jpg")
resize_img4=image4.resize((1520,570),Image.LANCZOS)
photo4=ImageTk.PhotoImage(resize_img4)
#LANCZOS is used image chota ya bada hone ke phate nhi like maintain aspect ratio
label_photo4=Label(image=photo4)
label_photo4.place(x=0,y=292,width=1520,height=570)

frame=Frame(root,borderwidth=6,relief=RIDGE,bg='#333333')
frame.place(x=500,y=220)

label_frame=Label(frame,text="Student Management System",fg="Blue",padx=10,pady=12,font="calibri 32 bold underline")
label_frame.pack()

frame2=Frame(root,relief=RIDGE,bg='ALICEBLUE')
frame2.place(x=10,y=300,width=1500,height=450)
left_frame=LabelFrame(frame2,borderwidth=4,relief=RIDGE,bg='white',text="Student Information",font='calibri 14 ',padx=4,pady=4)
left_frame.place(x=10,y=25,width=670,height=415)

right_frame=LabelFrame(frame2,borderwidth=4,relief=RIDGE,bg='white',text="Student Information",font='calibri 14 ',padx=4,pady=4)
right_frame.place(x=720,y=25,width=770,height=415)

student_info=LabelFrame(frame2,borderwidth=4,text="course information",relief=RIDGE,font="Arial 14",bg='white')
student_info.place(x=10,y=30,width=670,height=120)

personal_details=LabelFrame(frame2,text="Student college information",bg='white',borderwidth=4,relief=RIDGE,font="Arial 14 ")
personal_details.place(x=10,y=150,width=670,height=283)

label_department=Label(student_info,text="Department: ",bg="white",font="Calibri 14 bold")
department_combobox=ttk.Combobox(student_info,values=['Bioscience Engineering','Chemical Engineering','Civil Engineering','Computer science Engineering','Electrical Engineering','Mathematics','Mechanical Engineering'])
label_department.grid(row=0,column=0,padx=5,pady=4,sticky=W)
department_combobox.grid(row=0,column=1,sticky=W)

label_course=Label(student_info,text="Course: ",bg="white",font="Calibri 14 bold")
course_combobox=ttk.Combobox(student_info,values=['B.Tech','M.Tech','pHD'])
label_course.grid(row=0,column=2,padx=5,pady=4)
course_combobox.grid(row=0,column=3,sticky=W)

label_year=Label(student_info,text="year: ",bg="white",font="Calibri 14 bold")
year_spinbox=ttk.Spinbox(student_info,from_=2000,to=2050,width=10)
label_year.grid(row=0,column=4,padx=5,pady=4,sticky=W)
year_spinbox.grid(row=0,column=5,sticky=W)

label_semester=Label(student_info,text="Semester: ",bg="white",font="Calibri 14 bold")
semester_combobox=ttk.Combobox(student_info,values=['1st Semester','2nd Semester','3rd Semester','4th Semester','5th Semester','6th Semester','7th Semester','8th Semester'])
label_semester.grid(row=1,column=0,padx=5,pady=4,sticky=W)
semester_combobox.grid(row=1,column=1,sticky=W)

label_hostel=Label(student_info,text="Hostel",font="calibri 14 bold",bg='white')
hostel_combobox=ttk.Combobox(student_info,values=['A','B','C','D','E','F'])
label_hostel.grid(row=1,column=2,sticky=W)
hostel_combobox.grid(row=1,column=3,sticky=W)

label_studentID=Label(personal_details,text="studentID: ",bg='white',font="calibri 14 bold")
label_studentID.grid(row=2,column=0,sticky=W)
studentID_value=StringVar()
studentID_entry=Entry(personal_details,textvariable=studentID_value,width=30)
studentID_entry.grid(row=2,column=1,padx=4,pady=4,sticky=W)

label_firstname=Label(personal_details,text="First Name: ",bg='white',font="calibri 14 bold")
label_firstname.grid(row=3,column=0,sticky=W)
firstname_value=StringVar()
firstname_value_entry=Entry(personal_details,textvariable=firstname_value,width=30)
firstname_value_entry.grid(row=3,column=1,padx=4,pady=4,sticky=W)

label_lastname=Label(personal_details,text="  Last Name: ",bg='white',font="calibri 14 bold")
label_lastname.grid(row=3,column=2,sticky=W)
lastname_value=StringVar()
lastname_entry=Entry(personal_details,textvariable=lastname_value,width=20)
lastname_entry.grid(row=3,column=3,padx=4,pady=4,sticky=W)

label_rollno=Label(personal_details,text="  Roll no: ",bg='white',font="calibri 14 bold")
label_rollno.grid(row=2,column=2,sticky=W)
rollno_value=StringVar()
rollno_entry=Entry(personal_details,textvariable=rollno_value,width=20)
rollno_entry.grid(row=2,column=3,padx=4,pady=4,sticky=W)

dob_label=Label(personal_details,text="DOB:",bg='white',font='calibri 14 bold')
dob_label.grid(row=6,column=0,pady=4,sticky=W)
cal=DateEntry(personal_details,width=30)
cal.grid(row=6,column=1,pady=4,sticky=W)

blood_label=Label(personal_details,text="Blood Group:",bg='white',font="calibri 14 bold")
blood_label.grid(row=6,column=2,pady=4,sticky=W)
blood_combobox=ttk.Combobox(personal_details,values=['A+','B+','AB+','O+','A-','B-','AB-','O-'],width=20)
blood_combobox.grid(row=6,column=3,pady=4,sticky=W)

father_label=Label(personal_details,text="Father Name:",bg='white',font="calibri 14 bold")
father_label.grid(row=4,column=0,pady=4,sticky=W)
father_value=StringVar()
father_entry=Entry(personal_details,textvariable=father_value,width=30)
father_entry.grid(row=4,column=1,pady=4,sticky=W)

state_label=Label(personal_details,text="State:",bg='white',font="calibri 14 bold")
state_combobox=ttk.Combobox(personal_details,values= (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
),width=20)
state_label.grid(row=4,column=2,pady=4,sticky=W)
state_combobox.grid(row=4,column=3,pady=4,sticky=W)

label_phone=Label(personal_details,text="Phone: ",bg='white',font="calibri 14 bold")
label_phone.grid(row=5,column=0,sticky=W)
phone_value=StringVar()
phone_entry=Entry(personal_details,textvariable=phone_value,width=30)
phone_entry.grid(row=5,column=1,padx=4,pady=4,sticky=W)

label_email=Label(personal_details,text=" Email: ",bg='white',font="calibri 14 bold")
label_email.grid(row=5,column=2,sticky=W)
email_value=StringVar()
email_entry=Entry(personal_details,textvariable=email_value,width=20)
email_entry.grid(row=5,column=3,padx=4,pady=4,sticky=W)

label_scholarship=Label(personal_details,text=" Scholarship: ",bg='white',font="calibri 14 bold")
label_scholarship.grid(row=7,column=0,sticky=W)
scholarship_value=StringVar()
scholarship_entry=ttk.Combobox(personal_details,textvariable=scholarship_value,values=['Yes','No'],width=30)
scholarship_entry.grid(row=7,column=1,padx=4,pady=4,sticky=W)

department=department_combobox.get()
course=course_combobox.get()
year=year_spinbox.get()
semester=semester_combobox.get()
hostel=hostel_combobox.get()
studentID=studentID_value.get()
roll_no=rollno_value.get()
firstname=firstname_value.get()
lastname=lastname_value.get()
fathername=father_value.get()
state=state_combobox.get()
phone=phone_value.get()
email=email_value.get()
DOB=cal.get()
blood=blood_combobox.get()
scholarship=scholarship_value.get()

def add():
    
    department=department_combobox.get()
    course=course_combobox.get()
    year=year_spinbox.get()
    semester=semester_combobox.get()
    hostel=hostel_combobox.get()
    studentID=studentID_value.get()
    roll_no=rollno_value.get()
    firstname=firstname_value.get()
    lastname=lastname_value.get()
    fathername=father_value.get()
    state=state_combobox.get()
    phone=phone_value.get()
    email=email_value.get()
    DOB=cal.get()
    blood=blood_combobox.get()
    scholarship=scholarship_value.get()
    

    tmsg.showinfo("added","Data added successfully")
    conn=sqlite3.connect("studentdata.db")
    table_query='''CREATE TABLE IF NOT EXISTS Student_data(department TEXT, course TEXT,year INT,semester TEXT,hostel TEXT,studentID INT,roll_no INT,firstname TEXT,lastname TEXT,fathername TEXT,state TEXT,phone INT,email TEXT,DOB DATE,blood TEXT,scholarship TEXT)'''
    conn.execute(table_query)

    data_entry='''INSERT INTO Student_data (department , course ,year ,semester ,hostel ,studentID ,roll_no ,firstname ,lastname ,fathername ,state ,phone ,email ,DOB ,blood,scholarship  ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    data_entry_tuples=(department , course ,year ,semester ,hostel ,studentID ,roll_no ,firstname ,lastname ,fathername ,state ,phone ,email ,DOB ,blood,scholarship  ) 
    cur=conn.cursor()
    cur.execute(data_entry,data_entry_tuples)
    conn.commit()
    fetch_data() #call the function to show datas table on screen
    conn.close()
##function to fetch data from backend to show on screen
def fetch_data():
    conn=sqlite3.connect("studentdata.db")
    cur=conn.cursor()
    cur.execute("select * from Student_data")
    data=cur.fetchall()
    if len(data)!=0:
        student_table.delete(*student_table.get_children())
        for i in data:
            student_table.insert("",END,values=i)
        conn.commit()
    conn.close()

#GET CURSOR FUNCTION TO CLICK ON DATA AND ALL DATA WILL BE FILLED IN BOX



def upload():
    global img
    file_types = [('Jpg Files', '*.jpg'),("png File",'*.png')]
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image",filetypes=file_types)
    tmsg.showinfo("Uploaded","Photo Uploaded Successfully")




def reset():
    for widget in personal_details.winfo_children():
        if isinstance (widget,Entry):
            widget.delete(0,'end')
        if isinstance (widget,ttk.Combobox):
            widget.delete(0,'end')
        if isinstance (widget,ttk.Spinbox):
            widget.delete(0,'end')
    for widget in student_info.winfo_children():
        if isinstance (widget,Entry):
            widget.delete(0,'end')
        if isinstance (widget,ttk.Combobox):
            widget.delete(0,'end')
        if isinstance (widget,ttk.Spinbox):
            widget.delete(0,'end')


def CSV():
    department=department_combobox.get()
    course=course_combobox.get()
    year=year_spinbox.get()
    semester=semester_combobox.get()
    hostel=hostel_combobox.get()
    studentID=studentID_value.get()
    roll_no=rollno_value.get()
    firstname=firstname_value.get()
    lastname=lastname_value.get()
    fathername=father_value.get()
    state=state_combobox.get()
    phone=phone_value.get()
    email=email_value.get()
    DOB=cal.get()
    blood=blood_combobox.get()
    scholarship=scholarship_value.get()
    
   
    f=open('Student_data.csv','a')
    f.write(f"{department,course ,year ,semester ,hostel ,studentID ,roll_no ,firstname ,lastname ,fathername ,state ,phone ,email ,DOB ,blood,scholarship}\n")
    
    f.close()
    tmsg.showinfo("Success","Converted into CSV format ")

def delete():

    # #else:
    #     #try:
    delete=tmsg.askyesno("Delete","Are you sure to delete this student")
    if delete>0:
        conn=sqlite3.connect("studentdata.db")
        
        #cur=conn.cursor()
        sql='''DELETE FROM Student_data where studentID='''
        VALUE=(studentID,)
        cur=conn.cursor()
        cur.execute(sql,VALUE)
    else:
        if not delete:
            return
    conn.commit()
    fetch_data()
    conn.close()
    tmsg.showinfo("Deleted"," data is Deleted")  
    #     # except:
    #     #     tmsg.showerror("erroer","error")

















def save():
    pass
Button(personal_details,text="ADD",bg="#7fff00",command=add,width=15,font="calibri  8  bold").grid(row=10,column=0)
Button(personal_details,text="Update",bg="Blue",command=save,width=15,font="calibri  8 bold").grid(row=10,column=1)
Button(personal_details,text="Delete",bg="yellow",command=delete,width=15,font="calibri 8  bold").grid(row=10,column=2)
Button(personal_details,text="Gmail",bg="#00ffff",command=save,width=15,font="calibri 8  bold").grid(row=12,column=0,pady=8,padx=10)
Button(personal_details,text="Reset",bg="red",command=reset,width=15,font="calibri 8  bold").grid(row=10,column=3)
Button(personal_details,text="Upload",bg="#fce6c9",command=upload,width=15,font="calibri  8 bold").grid(row=12,column=1,pady=8,padx=10)
Button(personal_details,text="Exit",bg="#cd2626",command=quit,width=15,font="calibri  8 bold").grid(row=12,column=3,pady=8,padx=10)
Button(personal_details,text="Convert to .csv",bg="#eee8cd",command=CSV,width=15,font="calibri 8  bold").grid(row=12,column=2,pady=8,padx=10)

search_frame=LabelFrame(right_frame,borderwidth=4,bg='white',relief=RIDGE,text="Search Student Information",font="calibri 14 bold")
search_frame.place(x=0,y=0,width=750,height=70)
search_by=Label(search_frame,text="Search by:",fg='blue',bg='white',font="calibri 14 bold")
search_by.grid(row=0,column=0,sticky=W,padx=4,pady=6)

search_by_combobox=ttk.Combobox(search_frame,values=['Roll no','phone','studentID'])
search_by_combobox.grid(row=0,column=2,padx=2,pady=4)

text_search=Entry(search_frame,font="calibri 14 bold")
text_search.grid(row=0,column=3,padx=4)


Button(search_frame,text="Search",bg="#00ffff",font=("calibri 14 bold")).grid(row=0 ,column=5,padx=8)
Button(search_frame,text="Show All",bg="#00ffff",font=("calibri 14 bold")).grid(row=0 ,column=6,padx=8)


table_frame=Frame(right_frame,borderwidth=4,relief=RIDGE,bg="white")
table_frame.place(x=0,y=80,width=790,height=300)

Scrollbar_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scrollbar_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

student_table=ttk.Treeview(table_frame,column=('department','course' ,'year' ,'semester' ,'hostel' ,'studentID' ,'roll_no' ,'firstname' ,'lastname' ,'fathername' ,'state' ,'phone' ,'email' ,'DOB' ,'blood','scholarship' ),xscrollcommand=Scrollbar_x.set,yscrollcommand=scrollbar_y.set)
Scrollbar_x.pack(side=BOTTOM,fill=X)
scrollbar_y.pack(side=RIGHT,fill=Y)


Scrollbar_x.config(command=student_table.xview)
scrollbar_y.config(command=student_table.yview)

student_table.heading("department",text="department")
student_table.heading("course",text="course")
student_table.heading("year",text="year")
student_table.heading("semester",text="semester")
student_table.heading("hostel",text="hostel")
student_table.heading("studentID",text="studentID")
student_table.heading("roll_no",text="roll_no")
student_table.heading("firstname",text="firstname")
student_table.heading("lastname",text="lastname")
student_table.heading("fathername",text="fathername")
student_table.heading("state",text="state")
student_table.heading("phone",text="phone")
student_table.heading("email",text="email")
student_table.heading("DOB",text="DOB")
student_table.heading("blood",text="blood")
student_table.heading("scholarship",text="scholarship")

student_table["show"]="headings"
student_table.column("department",width=100)
student_table.column("course",width=100)
student_table.column("year",width=100)
student_table.column("semester",width=100)
student_table.column("hostel",width=100)
student_table.column("studentID",width=100)
student_table.column("roll_no",width=100)
student_table.column("firstname",width=100)
student_table.column("lastname",width=100)
student_table.column("fathername",width=100)
student_table.column("state",width=100)
student_table.column("phone",width=100)
student_table.column("email",width=100)
student_table.column("DOB",width=100)
student_table.column("blood",width=100)
student_table.column("scholarship",width=100)

student_table.pack(fill=BOTH,expand=1)
fetch_data() #call function to show datas table on screen



root.mainloop()