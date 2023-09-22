import mysql.connector
from DatabaseConnection1 import Connection
class InsertDataInDB:
    # function for inserting data into the EmployeeManagementSystem table
    def InsertData(self):
        # global collect
        insertedData=[]
        while True:
            sql=("Insert into EmployeeManagementSystem(Employee_ID,Employee_name,Phone_Number,Email_id,department_Name,Salary) values(%s,%s,%s,%s,%s,%s)")
            collect = []
            #Take input as employee id
            try:
                while True:
                    id=input("Enter Employee ID: ")
                    if(id.isdigit()):
                        if(len(id)<=5):
                            idTemp=int(id)
                            collect.append(idTemp)
                            break
                        else:
                            print("\nEmployee ID too long!  Try again.\n")
                    else:
                        print("\ninvalid input! Try again.\n")
            except:
                print("Error in ID input")

            # Take input as Employee Name
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
                            collect.append(name)
                            break
                    else:
                        print("\ninvalid input! Try again.\n")
            except:
                print("Error in Employee Name")

            # Take input as phone number
            try:
                while True:
                    Phone_no=input("Enter Phone Number: ")
                    if(len(Phone_no)==10):
                        if(Phone_no.isdigit()):
                            collect.append(Phone_no)
                            break
                        else:
                            print("\ninvalid input! Try again\n")
                    else:
                        print("\ninvalid input! Try again\n")
            except:
                print("Error in Phone n0")

            # to enter email id into database
            try:
                while True:
                    email=input("Enter Email id: ")
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
                                        boolean=False
                                        print("\ninvalid input! Try again\n")
                                        break
                                if (boolean == True):
                                    collect.append(email)
                                    break
                            else:
                                print("\ninvalid input! Try again\n")
                        else:
                            print("\ninvalid input! Try again\n")
                    else:
                        print("\ninvalid input! Try again\n")
            except:
                print("Error in Email ID")

            # Take input as department name
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
                            collect.append(deptname.upper())
                            break
                    else:
                        print("invalid input! Try again.")
            except:
                print("Error in department")

            # Take input as salary
            try:
                while True:
                    salary = input("Enter Salary of Employee: ")
                    if (len(salary) <= 8):
                        if (salary.isdigit()):
                            collect.append(salary)
                            break
                        else:
                            print("invalid input! Try again")
                    else:
                        print("input is too long ! Try again")
            except:
                print("Error in salary")

            boolFinal=False
            try:
                while True:
                    print("Press 1 to add another data")
                    print("Press 0 to Stop")
                    addmore=input("Enter your choice: ")
                    if(int(addmore)==1 or int(addmore)==0):
                        if(int(addmore)==0):
                            boolFinal=True
                            break
                        else:
                            boolFinal=False
                            break
                    else:
                        print("\nInvalid Input! Try again.\n")
            except:
                print("Error in choice to add more data")
            if(boolFinal):
                insertedData.append(tuple(collect))
                print(insertedData)
                try:
                    Connection().execute_multiple_query(sql,insertedData)
                    print(Connection().cursor.rowcount, " Record Added")
                    break
                except mysql.connector.IntegrityError as e:
                    e1=str(e)
                    if("employeemanagementsystem.PRIMARY" in e1):
                        print("\nEmployee Id already exists")
                        print("Data not saved, Try again\n")
                    if("employeemanagementsystem.Phone_Number" in e1):
                        print("\nPhone number already exists")
                        print("Data not saved, Try again\n")
                    if("employeemanagementsystem.Email_id" in e1):
                        print("\nEmail Id already exists")
                        print("Data not saved, Try again\n")

                    break
            else:
                insertedData.append(tuple(collect))
