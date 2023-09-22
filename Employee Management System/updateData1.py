# to update the data in database
from DatabaseConnection1 import Connection as c

class UpdateData:
    def takeUpdateValu(self):
        try:
            print("\n------Update data------\n")
            try:
                id = input("Enter Employee ID to update data: ")
                if (id.isdigit()):
                    if (len(id) <= 5):
                        idTemp = int(id)
                        return idTemp
                    else:
                        return id
                else:
                    return id
            except:
                    return 0
        except:
            print("\nInvalid input!\n")

    def idtoUpdate(self,idno):
        sql = "select * from EmployeeManagementSystem"
        obj = c()
        connect = obj.conn
        cursor_show_data = connect.cursor()
        x = cursor_show_data.execute(sql)
        rs = cursor_show_data.fetchall()
        temptest = 0
        for d1 in rs:
            bool1 = False
            if idno in d1:
                bool1 = True
                temptest = 1
            if (bool1):
                print("Press 1 to Update Employee's Name")
                print("Press 2 to Update Employee's Phone number")
                print("Press 3 to Update Employee's Email ID")
                print("Press 4 to Update Employee's Department")
                print("Press 5 to Update Employee's Salary")
                print("Press 0 to go main menu")
                choice=input("Enter your Choice: ")
                if(choice=="1"):
                    try:
                        while True:
                            name = input("Enter name: ")
                            sname = name.split()
                            if (bool(sname)):
                                boolean0 = False
                                for checkname in sname:
                                    if (checkname.isalpha()):
                                        boolean0 = True
                                    else:
                                        boolean0 = False
                                        print("\ninvalid input! Try again.\n")
                                        break
                                if (boolean0):
                                    sql1 = ("update EmployeeManagementSystem set Employee_name=%s where Employee_ID= %s")
                                    para=[(name,idno)]
                                    obj.execute_multiple_query(sql1,para)
                                    if (obj.cursor.rowcount == 0):
                                        print("You have not updated Employee's Name!\n")
                                    else:
                                        print("Employee's Name updated")
                                    break
                            else:
                                print("\ninvalid input! Try again.\n")
                    except Exception as e:
                        print("Error in Employee Name")

                elif(choice=="2"):
                    try:
                        while True:
                            Phone_no = input("Enter Phone Number: ")
                            if (len(Phone_no) == 10):
                                if (Phone_no.isdigit()):
                                    sql1 = ("update EmployeeManagementSystem set Phone_Number=%s where Employee_ID=%s")
                                    para = [(Phone_no, idno)]
                                    obj.execute_multiple_query(sql1, para)
                                    if(obj.cursor.rowcount==0):
                                        print("You have not updated phone number!\n")
                                    else:
                                        print("Employee's Phone Number updated\n")
                                    break
                                else:
                                    print("\ninvalid input! Try again\n")
                            else:
                                print("\ninvalid input! Try again\n")
                    except:
                        print("Phone number already Available")
                elif(choice=="3"):
                    try:
                        while True:
                            email = input("Enter Email id: ")
                            temp = list(email)
                            temp1 = "@gmail.com"
                            if (temp1 in email):
                                n = email.split("@")
                                if ("gmail.com" in n[1]):
                                    temps = n[0]
                                    if any(a.isalpha() for a in temps):
                                        boolean = False
                                        for tempx in temps:
                                            if ((ord(tempx) in range(97, 123)) or (ord(tempx) in range(48, 58))):
                                                boolean = True
                                            else:
                                                boolean = False
                                                print("\ninvalid input! Try again\n")
                                                break
                                        if (boolean == True):
                                            sql1 = ("update EmployeeManagementSystem set Email_id=%s where Employee_ID=%s")
                                            para = [(email, idno)]
                                            obj.execute_multiple_query(sql1, para)
                                            if (obj.cursor.rowcount == 0):
                                                print("You have not updated Employee's Email ID!\n")
                                            else:
                                                print("Employee's Email ID updated\n")
                                            break
                                    else:
                                        print("\ninvalid input! Try again\n")
                                else:
                                    print("\ninvalid input! Try again\n")
                            else:
                                print("\ninvalid input! Try again\n")
                    except:
                        print("Email ID already Available !")
                elif(choice=="4"):
                    try:
                        while True:
                            deptname = input("Enter Department name: ")
                            dname = deptname.split()
                            if (bool(dname)):
                                boolean0 = False
                                for checkdeptname in dname:
                                    if (checkdeptname.isalpha()):
                                        boolean0 = True
                                    else:
                                        boolean0 = False
                                        print("invalid input! Try again.")
                                        break
                                if (boolean0):
                                    sql1 = ("update EmployeeManagementSystem set department_Name=%s where Employee_ID=%s")
                                    para = [(deptname, idno)]
                                    obj.execute_multiple_query(sql1, para)
                                    if (obj.cursor.rowcount == 0):
                                        print("You have not updated Employee's Department!\n")
                                    else:
                                        print("Employee's Department updated\n")
                                    break
                            else:
                                print("invalid input! Try again.")
                    except:
                        print("Error in department")
                elif(choice=="5"):
                    try:
                        while True:
                            salary = input("Enter Salary of Employee: ")
                            if (len(salary) <= 8):
                                if (salary.isdigit()):
                                    sql1 = ("update EmployeeManagementSystem set Salary=%s where Employee_ID=%s")
                                    para = [(salary, idno)]
                                    obj.execute_multiple_query(sql1, para)
                                    if (obj.cursor.rowcount == 0):
                                        print("You have not updated Employee's Salary!\n")
                                    else:
                                        print("Employee's Salary updated\n")
                                    break
                                else:
                                    print("invalid input! Try again")
                            else:
                                print("input is too long ! Try again")
                    except:
                        print("Error in salary")
                elif(choice=="0"):
                    print("\nNo Changes\n")
                    break
                else:
                    print('Invalid input!')
        if (temptest == 0):
            print("\nEmployee's ID NOT FOUND!\n")
