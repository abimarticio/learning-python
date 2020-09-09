# Decision Maker
# ask user a question
# ask user to give options 
# remove option that might have entered more than once
# generate answer through the given options

import random

def generate_random_int(minimum_value: int, maximum_value: int) -> int:
    return random.randint(minimum_value, maximum_value)

def get_options():
    options_list = []
    while True:
        options = input("Enter options: ").upper()
        if options != "":
            options_list.append(options)
        elif options == "":
            break

    for option in options_list:
        number_occurrence_option =  options_list.count(option)
        if number_occurrence_option > 1:
            options_list.remove(option)

    return options_list

def main():
    while True:
        input_question = input("Enter question: ").upper()
        if input_question == "":
            print("Please enter your quetion!")
        elif input_question != "":
            break

    options = get_options()
    random_generator = generate_random_int(0, len(options))
    print(input_question)
    print(options[random_generator])

main()