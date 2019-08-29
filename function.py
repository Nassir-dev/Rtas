import random

def enter_pool(name,list):
    list.append(name)

def separation(entry,list, paid_list):
        if entry in list:
                list.remove(entry)
                paid_list.append(entry)
        else:
                print("entry Not captured")
               
def allocation(entry,paid_list,officer_list):
        if entry in paid_list:
                officer = random.choice(officer_list)

                print("Entry" + str(entry) + "has been allocated to" + officer)

        else:
                print("Entry hasnt paid yet ")

