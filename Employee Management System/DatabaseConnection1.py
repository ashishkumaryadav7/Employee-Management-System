from mysql.connector import connect as c
class Connection:
    # Accessing database
    def __init__(self):
        self.conn= c(
            host="localhost",
            user="root",
            password="1122"
        )
        # creating database is it is created then use it
        try:
            # creating cursor
            self.cursor = self.conn.cursor()
            sql = "create database Employee_Management_System"
            self.cursor.execute(sql)
        except:
            self.conn = c(
                host="localhost",
                user="root",
                password="1122",
                database="Employee_Management_System"

            )
            self.cursor = self.conn.cursor()

    # Creating table EmployeeManagementSystem in Employee_Management_System database
    def createTable(self):
        try:
            sql="Create table EmployeeManagementSystem(Employee_ID int Primary key, Employee_name varchar(35) not null,Phone_Number varchar(10) Unique,Email_id varchar(50),department_Name varchar(30),Salary int)"
            self.cursor.execute(sql)
        except:
            pass

    # function for executing multiple query
    def execute_multiple_query(self, q,v):
        self.cursor.executemany(q,v)
        self.conn.commit()

    # function for executing single query
    def execute_single_query(self,q):
        self.cursor.execute(q)
        self.conn.commit()

    # function for closing the connection from the database
    def close_connection(self):
        self.conn.close()

t=Connection()
t.createTable()






