import random

def enter_pool(name,list):
    list.append(name)

def separation(entry,list, paid_list):
    end = len(list)
    for i in range(end):
        if list[i] == entry:
           list.pop(i)
           paid_list.append(list[i])

