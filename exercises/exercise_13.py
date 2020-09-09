# Random Name Picker
# enter names one by one
# if you entered name/names more than once
# ask user
# Do you want to remove extra name/names that entered more than once?
# if yes, remove the name from the list
# if no, list will remain the same
# generate a winner

import random

def generate_random_int(minimum_value: int, maximum_value: int) -> int:
    return random.randint(minimum_value, maximum_value)

def get_user_input() -> list:   
    name_list = [] 
    while True:
        user_input = input("Enter name: ").upper()
        if user_input != "":
            name_list.append(user_input)
        elif user_input == "":
            break
    return name_list     

def main():
    name_list = get_user_input()
    for name in name_list:
        number_occurrence_name =  name_list.count(name)
        if number_occurrence_name > 1:
            print(f"{name} is entered {number_occurrence_name} times")
            remove_name = input("Do you want to remove extra name/names that entered more than once? ")
            if remove_name.upper() == "YES":
                name_list.remove(name)
            elif remove_name.upper() == "NO":
                print("Other names that might have entered more than once will also remain in the list.")
                break
            
    print(f"The number of names you entered is {len(name_list)}.")
    random = generate_random_int(0, len(name_list) - 1)
    print(f"The winner is {name_list[random]}")

main()