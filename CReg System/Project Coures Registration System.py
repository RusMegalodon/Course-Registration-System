'''
Project | Course Registration System
'''

from tkinter import *
import csv

def Login():
    SID_lab_l10 = Label(gui, text="Student ID: ") #Line 1 Column 0
    SID_lab_l10.grid(row=1,column=0,sticky="w")
    SID_ert_l11 = Entry(gui, textvariable=InStdID_lg) #Line 1 Column 1
    SID_ert_l11.grid(row=1,column=1)
    PW_lab_l20 = Label(gui, text="Password: ") #Line 2 Column 0
    PW_lab_l20.grid(row=2,column=0,sticky="w")
    PW_ert_l21 = Entry(gui, textvariable=InPW_lg, show="*") #Line 2 Column 1
    PW_ert_l21.grid(row=2,column=1)

    def SetUser():
        global InStdID 
        InStdID = InStdID_lg.get()
        InPW = InPW_lg.get()
       
        with open("./Student.csv","r",encoding="utf-8") as Std_file:
            students = list(csv.DictReader(Std_file))
            StdID_list = [row["StdID"] for row in students]
            StdPW_list = {row["StdID"]:row["Password"] for row in students}
            Full_name = {row["StdID"]:f"{row["Fname"]} {row["Lname"]}" for row in students}
            '''for row in students:
                print(row)
            print(InStdID), print(StdID_list), print(Full_name),print(StdPW_list) #Check'''
            
            if InStdID in StdID_list:
                if InPW == StdPW_list[InStdID]:
                    print("Password correct")
                    SID_ert_l11.destroy(),bt_l30.destroy(),PW_lab_l20.destroy(),PW_ert_l21.destroy()
                    SID_lab_l10["text"] = ("Student Name: " + Full_name[InStdID].upper()) #New > Line 0 Column 2-4
                    SID_lab_l10.grid(row=0,column=2,sticky="w",columnspan=3)
                    MainMenu()
                else:
                    print("Password incorrect")
            else:
                print("Invalid ID")
    
    bt_l30 = Button(gui, text="Confirm", command=SetUser)
    bt_l30.grid(row=3,columnspan=2,pady=5)

def MainMenu():
    gui.geometry("360x200")
    RC_bt_l20 = Button(gui, text="Register Course", command=RegisterCourse)
    RC_bt_l20.grid(row=2,column=0,padx=10,pady=5,sticky="ew")

    DC_bt_l30 = Button(gui, text="Drop Course", command=DropCourse)
    DC_bt_l30.grid(row=3,column=0,padx=10,pady=5,sticky="ew")

    IF_bt_l40 = Button(gui, text="Info", command=Info)
    IF_bt_l40.grid(row=4,column=0,padx=10,pady=5,sticky="ew")

def RegisterCourse():
    gui.geometry("480x240")
    wCourse = [] #With Course From Save

    with open("./Course.csv","r",encoding="utf-8") as Course_file:
        courses = list(csv.DictReader(Course_file))
        '''for row in courses:
            print(row) #Check'''
        CourseN_list = [row["CourseName"] for row in courses]
        CourseID_list = [row["CourseID"] for row in courses]
        '''for i in range(len(CourseN_list)):
            print(f"{i+1}. {CourseN_list[i]} ID: {CourseID_list[i]}") #Check'''
        listbox = Listbox(gui, selectmode="single", width=40, height=9)
        listbox.insert(END, f"No. | Course Name")
        for i in range(len(CourseN_list)):
            listbox.insert(END, f"{i+1}. {CourseN_list[i]}")
        listbox.grid(row=1,rowspan=4,column=2,columnspan=3,sticky="nsew")

        def AddCourse():
            RegC = RegCourse.get()
            wCourse.append(RegC)
            print(wCourse)
            RegCourse.set("")
        Add_bt_l55 = Button(gui, text="Add Course", command=AddCourse)
        Add_bt_l55.grid(row=5,column=5,padx=5,pady=5,sticky="ew")
        
        def Back():
            listbox.destroy(),Close_bt.destroy(),gui.geometry("400x200")
    Close_bt = Button(gui, text="Close", command=Back)
    Close_bt.grid(row=6,column=4,padx=5,pady=5,sticky="ew")

def DropCourse():
    print("Test")

def Info():
    print("Test")

if __name__ == "__main__":
    gui = Tk()
    InStdID_lg = StringVar() #Input Student ID
    InPW_lg = StringVar() #Input Password
    RegCourse = StringVar() #With From Save In Grade

    gui.title("Course Registration System")
    gui.geometry("240x120"), gui.resizable(False, False)
    Label(gui, text="CReg System", font=("TH_Sarabun", 16, "bold"), fg="orange").grid(columnspan=2,sticky="w")
    Login()
        
gui.mainloop()