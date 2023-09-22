import DatabaseConnection1 as d
from InsertDataIntoTable1 import InsertDataInDB as insert
from showData1 import ShowallData as data
from searchData1 import searchData as s
from deleteData1 import deleteData as delete
from updateData1 import UpdateData as update
class Button:
    def options(self):

        while True:

            try:
                print("\n------HOME PAGE------\n")
                print("Press 1 to insert data")
                print("Press 2 to Show all data")
                print("Press 3 to delete data")
                print("Press 4 to Search data")
                print("Press 5 to update data")
                print("Press 0 to exit")
                inp=input("Enter your choice: ")
                database = d.Connection()
                if(inp=="1"):
                    insert().InsertData()
                    database.close_connection()
                elif(inp=="2"):
                    data()
                    database.close_connection()
                elif(inp=="3"):
                    dele=delete().takeIDtoDelete()
                    delete().delete(dele)
                    database.close_connection()
                elif(inp=="4"):
                    search=s()
                    ob= search.finddata()
                    search.dataretrive(ob)
                    database.close_connection()
                elif(inp=="5"):
                    ob=update().takeUpdateValu()
                    update().idtoUpdate(ob)
                elif(inp=="0"):
                    break
                else:
                    print("\ninvalid input! Try again.\n")
            except Exception as e:
                print(e)
                print("\ninvalid input! Try again1.\n")
