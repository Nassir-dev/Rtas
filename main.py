captured=[]
paid = []
officers = []

entry = input("Please Enter captured Entry")

captured.append(entry)



entry_select = input("Enter Entry")
entry_status = input("Enter entry Status")
print("1.Paid")

if entry_status == 1:
    if entry_select in captured:
        captured.pop(entry_select)

        paid.append(entry_select)
    else:
       print("does not exist")
        
print(captured)
print(paid)


