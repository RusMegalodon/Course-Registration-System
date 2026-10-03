# CReg System

ระบบลงทะเบียนเรียน
Course Registration System

## ภาษาไทย

### เกี่ยวกับโปรเจกต์

โปรเจกต์นี้เป็นระบบสำหรับลงทะเบียนเรียน ถอนวิชา และตรวจสอบข้อมูล

### จุดประสงค์

โปรเจกต์นี้ทำขึ้นเพื่อเป็น Final Project ของวิชา Computer Programming 1
และมีวัตถุประสงค์ในการเผยแพร่ เพื่อเป็นไอเดียสำหรับผู้ที่กำลังทำโปรเจกต์
สามารถนำไปศึกษา ทดลอง ปรับปรุง และต่อยอดได้ หากพบข้อผิดพลาด สามารถใช้เป็น
กรณีศึกษาเพื่อช่วยพัฒนาโปรเจกต์ให้ดีขึ้น :>

### ฟีเจอร์

- Login ด้วย Student ID และ Password
- แสดงชื่อผู้ใช้งานหลัง Login สำเร็จ
- แสดงรายวิชาที่เปิดให้ลงทะเบียน
- ลงทะเบียนรายวิชา
- ป้องกันการลงทะเบียนรายวิชาซ้ำ
- ถอนรายวิชา
- แสดงรายวิชา คะแนน และเกรดของนักศึกษา
- แสดงข้อมูล Faculty, Department และ Course
- จัดเก็บข้อมูลด้วยไฟล์ CSV

### เปิดโปรแกรมจาก VS Code

1. เปิดโฟลเดอร์ `CReg System` ด้วย VS Code
2. เปิดไฟล์ `Project Coures Registration System.py`
3. ตรวจสอบว่าเลือก Python interpreter ที่ติดตั้ง Python 3.x แล้ว
4. กดปุ่ม **Run Python File** หรือคลิกขวาในไฟล์แล้วเลือก **Run Python File in Terminal**

หากใช้การรันผ่าน Terminal ของ VS Code ให้ตรวจสอบว่า Current Working Directory
เป็นโฟลเดอร์ `CReg System` ซึ่งเป็นโฟลเดอร์เดียวกับไฟล์ CSV

นอกจากนี้ สามารถคลิกขวาที่ไฟล์ `.py` ในแถบ Explorer ของ VS Code แล้วเลือก
**Run Python File in Terminal** ได้เช่นกัน

### เปิดโปรแกรมจาก IDLE

1. เปิด IDLE ที่ติดตั้งมาพร้อมกับ Python
2. เลือก **File > Open...**
3. เปิดไฟล์ `Project Coures Registration System.py`
4. เลือก **Run > Run Module** หรือกด `F5`
5. หน้าต่างโปรแกรมจะเปิดขึ้นมา

สามารถคลิกขวาที่ไฟล์ `.py` แล้วเลือก **Edit with IDLE** จากนั้นกด `F5`
เพื่อรันโปรแกรมได้เช่นกัน

ควรเปิดไฟล์จากโฟลเดอร์โปรเจกต์ หรือกำหนดโฟลเดอร์โปรเจกต์เป็น Current
Working Directory ก่อนกด `F5` เพื่อให้โปรแกรมค้นหาไฟล์ CSV ได้ถูกต้อง

### บัญชีสำหรับทดสอบ

| Student ID | Password |
|---|---|
| `69101001` | `Test@1001` |

สามารถดูเพิ่มเติมได้ที่ Student.csv ส่วนของ StdID กับ Password

### ข้อมูลผู้จัดทำ

- **ผู้จัดทำ:** Russian Megalodon (Megalodon)
- **สถานะ:** นักศึกษา
- **มหาวิทยาลัย:** มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ (KMUTNB)
- **คณะ:** คณะวิทยาศาสตร์ประยุกต์
- **ภาควิชา:** วิทยาการคอมพิวเตอร์และสารสนเทศ (CIS)
- **สาขา:** วิทยาการคอมพิวเตอร์ (สองภาษา)

## English

### About the Project

This project is a system for registering courses, dropping courses, and checking
student information.

### Purpose

I made this project as my Final Project for Computer Programming 1.
I share it as an idea for people who are making their own projects.
You can study it, try it, improve it, and use it to get new ideas.
If you find any problems, you can use them as examples to improve your project :>

### Features

- Login with Student ID and password
- Show the student's name after login
- Show available courses
- Register for a course
- Check duplicate registration
- Drop a registered course
- Show courses, scores, and grades
- Show faculty, department, and course information
- Save data in CSV files

### Run from VS Code

1. Open the `CReg System` folder in VS Code.
2. Open `Project Coures Registration System.py`.
3. Choose a Python 3.x interpreter.
4. Click **Run Python File**, or right-click the file and choose
   **Run Python File in Terminal**.

The Current Working Directory should be the `CReg System` folder.
This is the same folder that contains the CSV files.

### Run from IDLE

1. Open IDLE.
2. Choose **File > Open...**.
3. Open `Project Coures Registration System.py`.
4. Choose **Run > Run Module** or press `F5`.
5. The program window should open.

You can also right-click the `.py` file and choose **Edit with IDLE**.
Then press `F5` to run the program.

The project folder should be the Current Working Directory so the program
can find the CSV files.

### Test Account

| Student ID | Password |
|---|---|
| `69101001` | `Test@1001` |

You can find more account information in `Student.csv`, under `StdID` and
`Password`.

### About the Creator

- **Creator:** Russian Megalodon (Megalodon)
- **Status:** Student
- **University:** King Mongkut's University of Technology North Bangkok (KMUTNB)
- **Faculty:** Faculty of Applied Science
- **Department:** Computer and Information Science (CIS)
- **Program:** Computer Science (Bilingual Program)
