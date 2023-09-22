from DatabaseConnection1 import Connection as c

class deleteData:
    # function that return employee id that the users want to Delete from the database
    def takeIDtoDelete(self):
        try:
            print("\n------Delete data------\n")
            try:
                id = input("Enter Employee ID to delete data: ")
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

    # Function that take Employee id as a parameter and delete that data from the database if data is available
    def delete(self,value):
        try:
            if(value==0):
                print("\nSomething Went Wrong !\n")
            elif(value != None):
                    sql1 = "select * from EmployeeManagementSystem"
                    sql=("delete from EmployeeManagementSystem where Employee_ID="+ str(value))
                    obj = c()
                    connect = obj.conn
                    cursor_show_data = connect.cursor()
                    x = cursor_show_data.execute(sql1)
                    rs = cursor_show_data.fetchall()
                    temptest = 0
                    for d1 in rs:
                        bool1 = False
                        if value in d1:
                            bool1 = True
                            temptest = 1
                        if (bool1):
                            obj.execute_single_query(sql)
                            print(obj.cursor.rowcount," Record Deleted")
                    if(temptest==0):
                        print("Data Not Available !")

        except:
            print("Invalid input!")

