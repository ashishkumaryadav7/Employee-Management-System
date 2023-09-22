from DatabaseConnection1 import Connection as c
class searchData:
    #Function that return the value that user wants to search
    def finddata(self):
        try:
            print("\n------Search data------\n")
            print("Press 1 to Search by Employee ID")
            print("Press 2 to Search by Name")
            print("Press 3 to Search by Phone Number")
            print("Press 4 to Search by Department Name")
            choice=input("Enter your choice: ")
            if(choice=="1"):
                try:
                    id = input("Enter Employee ID: ")
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

            elif(choice=="2"):
                try:
                    name = input("Enter name: ")
                    sname = name.split()
                    if (bool(sname)):
                        for checkname in sname:
                            if (checkname.isalpha()):
                                return name
                            else:
                                return name
                    else:
                        return name
                except:
                    return 0
            elif(choice=="3"):
                try:

                    Phone_no = input("Enter Phone Number: ")
                    if (len(Phone_no) == 10):
                        if (Phone_no.isdigit()):
                            return Phone_no
                        else:
                            return Phone_no
                    else:
                        return Phone_no
                except:
                    return 0
            elif(choice=="4"):
                try:
                    deptname = input("Enter Department name: ")
                    dname = deptname.split()
                    if (bool(dname)):
                        boolean0 = False
                        for checkdeptname in dname:
                            if (checkdeptname.isalpha()):
                                return deptname.upper()
                            else:
                                return deptname
                        else:
                            return deptname
                except:
                    return 0
            else:
                print("\nInvalid input!\n")
        except:
            print("\nInvalid input!\n")

    # function takes a value as a parameter and shows the result if data is present in the database
    def dataretrive(self,value):
        try:
            if(value==0):
                print("\nSomething Went Wrong !\n")
            elif(value != None):
                sql = "select * from EmployeeManagementSystem"
                obj = c()
                connect = obj.conn
                cursor_show_data = connect.cursor()
                x = cursor_show_data.execute(sql)
                rs = cursor_show_data.fetchall()
                temptest=0
                print(
                    "\n------------------------------------------------Searched Data-------------------------------------------------")
                print(
                    "\n--------------------------------------------------------------------------------------------------------------")
                print(
                    "|  {:<8} | {:20} | {:<11} | {:<25} | {:<15} | {}      |".format("ID", "Name", "Phone No.",
                                                                                     "Email ID",
                                                                                     "Department", "Salary"))
                print(
                    "--------------------------------------------------------------------------------------------------------------")
                for d1 in rs:
                    bool1=False
                    if value in d1:
                        bool1=True
                        temptest=1
                    if(bool1):

                        print("|  {:<8} | {:<20} | {:<11} | {:<25} | {:<15} | {:<10}  |".format(d1[0], d1[1], d1[2],
                                                                                                    d1[3], d1[4], d1[5]))
                        print("--------------------------------------------------------------------------------------------------------------\n")
                if(temptest==0):
                    print("|                                             DATA NOT FOUND !                                               |")
                    print("--------------------------------------------------------------------------------------------------------------\n")
        except:
            pass


