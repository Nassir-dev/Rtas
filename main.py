from function import *
from intro import intro_menu

entryPool = []
paidpool =[]

intro_menu()

while True:
    option = input("Enter your choice")

if option == 1:
    entry = input("what entry would you like to capture")

    enter_pool(entry,entryPool)

    

else option == 2:
        separation(entry,entryPool,paidpool)
        print("successfully added to paid pool")



        






