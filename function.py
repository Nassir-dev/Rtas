import random

def enter_pool(name,list):
    list.append(name)

def separation(entry,list, paid_list):
        if entry in list:
                list.remove(entry)
                paid_list.append(entry)
        else:
                print("entry Not captured")
               

