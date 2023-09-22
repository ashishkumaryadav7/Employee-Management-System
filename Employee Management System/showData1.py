from DatabaseConnection1 import Connection as c

# class that show the search result
class ShowallData:
    def __init__(self):
        sql="select * from EmployeeManagementSystem"
        obj=c()
        connect=obj.conn
        cursor_show_data=connect.cursor()
        x=cursor_show_data.execute(sql)
        rs=cursor_show_data.fetchall()
        print("\n-------------------------------------------------All data-----------------------------------------------------")
        print("\n--------------------------------------------------------------------------------------------------------------")
        print("|  {:<8} | {:20} | {:<11} | {:<25} | {:<15} | {}      |".format("ID","Name","Phone No.","Email ID","Department","Salary"))
        print("--------------------------------------------------------------------------------------------------------------")
        if (len(rs)!=0):
            for data in rs:
                print("|  {:<8} | {:<20} | {:<11} | {:<25} | {:<15} | {:<10}  |".format(data[0],data[1],data[2],data[3],data[4],data[5]))
            print("--------------------------------------------------------------------------------------------------------------")
        else:
            print("|                                             DATA NOT AVAILABLE !                                           |")
            print("--------------------------------------------------------------------------------------------------------------\n")
