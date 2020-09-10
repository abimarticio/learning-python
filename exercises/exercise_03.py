# ask for a number
# check if the given number
# is odd or even

num = int(input("Enter a number:"))

if num % 2 == 0:
    print("The number you entered is an even number.")
else:
    print("The number you entered is an odd number.")

result = "The number you entered is an even number" if num % 2 == 0 else\
"The number you entered is an odd number"
print(result)