import ctypes 
def check_is_number(input_str):
    if input_str.strip().isdigit():
        return True
    else:
        return False

my_information = ["Arman", "Bablumyan", 44, "Ashtarak", "Looking for a new opportunitiy"]
for i in range(len(my_information)):
    print(i, end=" ")
    print(my_information[i])
    
print("Arithmetic operatorations")
v_result = 0
v_first_value = input("First Value ")
if check_is_number(v_first_value) is False:
    ctypes.windll.user32.MessageBoxW(0, "Inputed not a number value", "Wrong Value", 2)
    #print("Inputed not a number value") 
else:
    v_second_value = input("Second Value ")
    if check_is_number(v_second_value) is False:
        ctypes.windll.user32.MessageBoxW(0, "Inputed not a number value", "Wrong Value", 2)
    else:
        c = int(v_first_value) + int(v_second_value)
        print("Addition is equal to " + str(c))
        c = int(v_first_value) - int(v_second_value)
        print("Subtraction is equal to " + str(c))
        c = int(v_first_value) * int(v_second_value)
        print("Multiplication is equal to " + str(c))
        c = int(v_first_value) / int(v_second_value)
        print("Division  is equal to " + str(c))
        c = int(v_first_value) ** int(v_second_value)
        print("Power of second is equal to " + str(c))
        