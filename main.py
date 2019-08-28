import random


captured=[56,20,30,40]
paid = []
officers = ['nassir','issa']

entry = input("Please Enter captured Entry")

captured.append(entry)



entry_select = input("Enter Entry")


for entry in captured:
    if entry_select in captured:
        captured.pop(entry_select)

        paid.append(entry_select)

        officer = random.choice(officers)

        print("entry" + entry_select + "has been allocated " + officer + "officer")
    else:
       print("does not exist")
        
print(captured)
print(paid)


