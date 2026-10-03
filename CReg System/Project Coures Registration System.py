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
            StdID_list = [row["StdID"] for row in students] #Student ID List
            StdPW_list = {row["StdID"]:row["Password"] for row in students} #Student Password List
            Full_name = {row["StdID"]:f"{row["Fname"]} {row["Lname"]}" for row in students} #Make Username from Show
            '''for row in students:
                print(row)
            print(InStdID), print(StdID_list), print(Full_name),print(StdPW_list) #Check'''
            
            if InStdID in StdID_list: #Check Student ID
                if InPW == StdPW_list[InStdID]: #Check Password
                    print("Password correct")
                    SID_ert_l11.destroy(),bt_l30.destroy(),PW_lab_l20.destroy(),PW_ert_l21.destroy()
                    SID_lab_l10["text"] = ("Student Name: " + Full_name[InStdID].upper()) #New > Line 0 Column 2-4
                    SID_lab_l10["font"] = ("Arial", 8, "bold")
                    SID_lab_l10.grid(row=0,column=2,sticky="w",columnspan=3)
                    MainMenu()
                else:
                    print("Password incorrect")
            else:
                print("Invalid ID")
    
    bt_l30 = Button(gui, text="Confirm", command=SetUser)
    bt_l30.grid(row=3,columnspan=2,pady=5)

def MainMenu():
    gui.geometry("400x160")

    RC_bt_l10 = Button(gui, text="Register Course", command=RegisterCourse) #Line 1 Column 0
    RC_bt_l10.grid(row=1,column=0,padx=10,pady=5,sticky="ew")

    DC_bt_l20 = Button(gui, text="Drop Course", command=DropCourse) #Line 2 Column 0
    DC_bt_l20.grid(row=2,column=0,padx=10,pady=5,sticky="ew")

    IF_bt_l30 = Button(gui, text="Info", command=Info) #Line 3 Column 0
    IF_bt_l30.grid(row=3,column=0,padx=10,pady=5,sticky="ew")

    global Enable_Menu_bt,Disable_Menu_bt
    def Enable_Menu_bt():
        RC_bt_l10["state"] = "normal"
        DC_bt_l20["state"] = "normal"
        IF_bt_l30["state"] = "normal"
    def Disable_Menu_bt():
        RC_bt_l10["state"] = "disabled"
        DC_bt_l20["state"] = "disabled"
        IF_bt_l30["state"] = "disabled"

def RegisterCourse():
    gui.geometry("480x240")
    global wCourse, wCourseID, SelC
    wCourse = [] #With Course From Save
    wCourseID = [] #With Course ID From Save
    SelC = [] #Selected Course Number List From Add
    
    Disable_Menu_bt() #Disable Main Menu Button
    
    with open("./Course.csv","r",encoding="utf-8") as Course_file:
        courses = list(csv.DictReader(Course_file))
        CourseN_list = [row["CourseName"] for row in courses] #Course Name List
        CourseID_list = [row["CourseID"] for row in courses] #Course ID List
        '''for row in courses:
            print(row) #Check
        for i in range(len(CourseN_list)):
            print(f"{i+1}. {CourseN_list[i]} ID: {CourseID_list[i]}") #Check'''
        CList = Listbox(gui, selectmode="single", width=40, height=9)
        CList.insert(END, f"No. | Course Name")
        for i in range(len(CourseN_list)):
            CList.insert(END, f"{i+1}. {CourseN_list[i]}")
        CList.grid(row=1,rowspan=4,column=1,columnspan=3,padx=10,pady=5,sticky="nsew")

        def CheckInGrade():
            with open("./Grade.csv","r",encoding="utf-8") as Grade_file:
                grades = list(csv.DictReader(Grade_file))
                CourseG = [row["CourseName"] for row in grades if row["StdID"] == InStdID] #Filter Student Course Name
            return CourseG

        def AddCourse():
            RegC = RegCourse.get() - 1
            if RegC < 0 or RegC >= len(CourseN_list) or RegC in SelC:
                print(f"|Invalid Course Number (Has 1 to {len(CourseN_list)})|") #Return to Terminal
                Add_ert_l51.config(bg="red")
            elif CourseN_list[RegC] in CheckInGrade():
                print(f"|Course already registered: {CourseN_list[RegC]}|") #Return to Terminal
                Add_ert_l51.config(bg="red")
            else:
                Add_ert_l51.config(bg="lightblue")
                wCourse.append(CourseN_list[RegC])
                wCourseID.append(CourseID_list[RegC])
                SelC.append(RegC)
                print(f"|Added Course: {CourseN_list[RegC]} ID: {CourseID_list[RegC]} Success|") #Confirm in Terminal
        
        def SaveCourse():
            with open("./Grade.csv","a+",encoding="utf-8",newline="") as Grade_file:
                Grade_file.seek(0) #Start Reading From Top
                Grades = list(csv.DictReader(Grade_file))
                Save = csv.DictWriter(Grade_file, fieldnames=["StdID","CourseID","CourseName","Score","Grade"])
                '''for i in range(len(Grades)):
                    print(Grades[i]) #Check'''
                for loop in range(len(wCourse)): #Check if Course Already Registered
                    Ready_Data = {"StdID":InStdID,"CourseID":wCourseID[loop],"CourseName":wCourse[loop],"Score":"None","Grade":"None"}
                    if Ready_Data in Grades: #If Course Already Registered
                        print(f"|Course already registered: {wCourse[loop]}|") #Check
                    else: #If Course Not Registered Yet
                        Save.writerow(Ready_Data)
                        print(f"|Saved successfully: {wCourse[loop]}|   ") #Check
            wCourse.clear(),wCourseID.clear(),SelC.clear() #Reset After Save
            print("===Save Process Complete===") #Confirm in Terminal

        def Back():
            CList.destroy(),Close_bt_l40.destroy(),Save_bt_l50.destroy(),Add_ert_l51.destroy(),Add_bt_l54.destroy()
            gui.geometry("400x160"),Enable_Menu_bt()
            print("===Back to Main Menu===") #Confirm in Terminal
    
    Close_bt_l40 = Button(gui, text="Close", command=Back,bg="red") #Line 4 Column 0
    Close_bt_l40.grid(row=4,column=0,padx=5,pady=5,sticky="ew")

    Save_bt_l50 = Button(gui, text="Save", command=SaveCourse,bg="green") #Line 5 Column 0
    Save_bt_l50.grid(row=5,column=0,padx=5,pady=5,sticky="ew")

    Add_ert_l51 = Entry(gui, textvariable=RegCourse,bg="lightblue") #Line 5 Column 1-3
    Add_ert_l51.grid(row=5,column=1,columnspan=3,padx=5,pady=5,sticky="ew")

    Add_bt_l54 = Button(gui, text="Add Course", command=AddCourse) #Line 5 Column 4
    Add_bt_l54.grid(row=5,column=4,padx=5,pady=5,sticky="ew")

def DropCourse():
    gui.geometry("480x240")
    SelC = [] #Selected Course Number List From Delete

    Disable_Menu_bt() #Disable Main Menu Button

    def ListCourse():
        with open("./Grade.csv","r",encoding="utf-8") as Grade_file:
            global Grades, Fil_StdC, CList
            Grades = list(csv.DictReader(Grade_file))
            '''for row in range(len(Grades)):
                print(Grades[row]) #Check'''
            Fil_StdC = [row["CourseName"] for row in Grades if row["StdID"] == InStdID] #Filter Student Course Name
            '''for row in range(len(Fil_StdC)):
                print(f"{row+1}. {Fil_StdC[row]}")''' #Check
            CList = Listbox(gui, selectmode="single", width=40, height=9) #List from Student ID
            CList.insert(END, f"No. | Course Name")
            for row in range(len(Fil_StdC)):
                CList.insert(END, f"{row+1}. {Fil_StdC[row]}")
            CList.grid(row=1,rowspan=4,column=1,columnspan=3,padx=10,pady=5,sticky="nsew")
            print("===Make List Complete===") #Confirm in Terminal

    def DeleteCourse():
        for loop in range(len(SelC)):
            for i in range(len(Grades)):
                if Grades[i]["StdID"] == InStdID and Grades[i]["CourseName"] in SelC:
                    print(f"|Deleted Course: {Grades[i]['CourseName']} Success|") #Check
                    del Grades[i]
                    break
        with open("./Grade.csv","w",encoding="utf-8",newline="") as Grade_file:
            Replace = csv.DictWriter(Grade_file, fieldnames=["StdID","CourseID","CourseName","Score","Grade"])
            Replace.writeheader()
            Replace.writerows(Grades)
        print("---Delete Process Complete---") #Confirm in Terminal
        ListCourse()

    def AddCourse():
        DelC = DopCourse.get() - 1
        if DelC < 0 or DelC >= len(Fil_StdC):
            print(f"It course not registered")
            Add_ert_l51.config(bg="red")
        else:
            Add_ert_l51.config(bg="lightblue")
            SelC.append(Fil_StdC[DelC])
        for i in range(len(SelC)):
            print(f"|Add: {SelC[i]} Success|") #Confirm in Terminal

    def Back():
        CList.destroy(),Close_bt_l40.destroy(),Delete_bt_l50.destroy(),Add_ert_l51.destroy(),Add_bt_l54.destroy()
        gui.geometry("400x160"),Enable_Menu_bt()
        print("===Back to Main Menu===") #Confirm in Terminal

    ListCourse()

    Close_bt_l40 = Button(gui, text="Close", command=Back,bg="red") #Line 4 Column 0
    Close_bt_l40.grid(row=4,column=0,padx=5,pady=5,sticky="ew")

    Delete_bt_l50 = Button(gui, text="Delete", command=DeleteCourse,bg="green") #Line 5 Column 0
    Delete_bt_l50.grid(row=5,column=0,padx=5,pady=5,sticky="ew")

    Add_ert_l51 = Entry(gui, textvariable=DopCourse,bg="lightblue") #Line 5 Column 1-3
    Add_ert_l51.grid(row=5,column=1,columnspan=3,padx=5,pady=5,sticky="ew")

    Add_bt_l54 = Button(gui, text="Add Course", command=AddCourse) #Line 5 Column 4
    Add_bt_l54.grid(row=5,column=4,padx=5,pady=5,sticky="ew")
   
def Info():
    gui.geometry("480x240")

    Disable_Menu_bt() #Disable Main Menu Button

    def StudentInfo():
        gui.geometry("480x240")
        SwitchInfo() #Destroy Listbox Before Show New Listbox

        with open("./Grade.csv","r",encoding="utf-8") as Grade_file:
            global Grade_list, Std_Info
            grades = list(csv.DictReader(Grade_file))
            Grade_list = [row for row in grades if row["StdID"] == InStdID] #Filter by Student ID
            '''for row in range(len(Grade_list)):
                print(Grade_list[row]) #Check'''
            Std_Info = Listbox(gui, selectmode="single", width=50, height=9) #List from Student ID (Grade)
            Std_Info.insert(END, f"No. | Course Name | Score | Grade")
            for i in range(len(Grade_list)):
                Std_Info.insert(END, f"{i+1}. {Grade_list[i]['CourseName']} | {Grade_list[i]['Score']} | {Grade_list[i]['Grade']}")
            Std_Info.grid(row=1,rowspan=4,column=1,columnspan=5,padx=10,pady=5,sticky="nsew")

    def CourseInfo():
        gui.geometry("560x240")
        SwitchInfo() #Destroy Listbox Before Show New Listbox

        with open("./Faculty.csv","r",encoding="utf-8") as Faculty_file:
            fac = list(csv.DictReader(Faculty_file)) #Read Faculty data
        with open("./Department.csv","r",encoding="utf-8") as Dept_file:
            dep = list(csv.DictReader(Dept_file)) #Read Department data
        with open("./Course.csv","r",encoding="utf-8") as Course_file:
            course = list(csv.DictReader(Course_file)) #Read Course data
        global CourseIF_list
        CourseIF_list = Listbox(gui, selectmode="single", width=70, height=9) #List from Student ID (Course Info)
        CourseIF_list.insert(END, f"{"ID":<16} | Name")
        for i in range(len(Grade_list)):
            for c in range(len(course)):
                if Grade_list[i]["CourseID"] == course[c]["CourseID"]:
                    FacID = course[c]["FacID"]
                    FacName = [row["FacName"] for row in fac if row["FacID"] == FacID][0]
                    DeptID = course[c]["DepID"]
                    DeptName = [row["DepName"] for row in dep if row["DepID"] == DeptID][0]
                    CourseID = course[c]["CourseID"]
                    CourseName = course[c]["CourseName"]
            CourseIF_list.insert(END, f"{FacID:<17} | {FacName}")
            CourseIF_list.insert(END, f"{DeptID:<15} | {DeptName}")
            CourseIF_list.insert(END, f"{CourseID} | {CourseName}")
            CourseIF_list.insert(END, "------------------------------------------------------------")
        CourseIF_list.grid(row=1,rowspan=4,column=1,columnspan=7,padx=10,pady=5,sticky="nsew")

    def SwitchInfo():
        try:
            Std_Info.destroy() #Destroy Student Info Listbox
            CourseIF_list.destroy() #Destroy Course Info Listbox
        except Exception as SyntaxError:
            pass

    def Back():
        SwitchInfo(),StdIF_bt_l51.destroy(),CourseIF_bt_l52.destroy(),Back_bt_l40.destroy()
        gui.geometry("400x160"),Enable_Menu_bt()
        print("===Back to Main Menu===") #Confirm in Terminal

    StudentInfo() #Default Show Student Info

    Back_bt_l40 = Button(gui, text="Back", command=Back,bg="red") #Line 4 Column 0
    Back_bt_l40.grid(row=4,column=0,padx=5,pady=5,sticky="ew")

    StdIF_bt_l51 = Button(gui, text="Student Info", command=StudentInfo) #Line 5 Column 1
    StdIF_bt_l51.grid(row=5,column=1,padx=5,pady=5,sticky="ew") 

    CourseIF_bt_l52 = Button(gui, text="Course Info", command=CourseInfo) #Line 5 Column 2
    CourseIF_bt_l52.grid(row=5,column=2,padx=5,pady=5,sticky="ew")

if __name__ == "__main__":
    gui = Tk()
    InStdID_lg = StringVar() #Input Student ID
    InPW_lg = StringVar() #Input Password
    RegCourse = IntVar() #Input Course Name From Add to Grade
    DopCourse = IntVar() #Input Course Name From Delete from Grade

    gui.title("Course Registration System")
    gui.geometry("240x120"), gui.resizable(False, False)
    Label(gui, text="CReg System", font=("TH_Sarabun", 16, "bold"), fg="orange").grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="w")
    Login()
        
    gui.mainloop()