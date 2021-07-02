#exe_3 from telegrem 28.06
"""
guest_list=["Armen","Ashot","Karen",]
for guest in guest_list:    #For other collections it will be the following: for i in guest_list:
    print("Dear " + guest + ", you are inveted to the party.\n")
"""

def cycle_throw_list(guest_list):
    res = ""
    for guest in range(len(guest_list)): 
        res= res + ("Dear " + guest_list[guest] + ", you are inveted to the party.\n")
    return res

g_list = ["Armen","Anahit","Karen",]
print(cycle_throw_list(g_list))
g_list[1] = "Vardan"
print(cycle_throw_list(g_list))

print("The list of guest are growing.")

g_list.insert(0,"Gegam")

g_list.append("Karine")
print(g_list)

print("To the party are welcome only 2 person from " + str(len(g_list)))

while len(g_list)> 2:
    print(f"We are very sorry Mr/Miss {g_list[0]} announce you , that you have excluded from the invited persons lists. " )
    g_list.pop(0)   #or del g_list

g_list.pop()    #REMOVE LAST ELEMENT FROM THE LIST
print(g_list)
g_list.pop()
print(g_list)