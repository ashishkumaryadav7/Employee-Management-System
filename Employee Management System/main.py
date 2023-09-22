# main file of the program
# give 3 chance to login into Employee Management System

import authentication1 as a
from button1 import Button as b
n=0
while n<3:
    username=input("Enter the username: ")          # username: ashish
    password=input("Enter the  password: ")         # password: 123

    x = a.authentication(username,password)

    if x.verifcation():
        print("\nLogin successful!\n")
        print("----Employee Information System----")
        b().options()
        break
    else:
       print("Login failed! Try again.")
    n+=1
