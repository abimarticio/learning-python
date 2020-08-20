# exercise 4a
# loop through numbers 0 to 30
# print if number is even
# number 2 is even
# print if number is odd
# number 3 is odd

# exercise 4b
# exit loop if the user input is odd number

# exercise 4c
# using loop, get the sum of numbers 0 to 15

# exercise 4d
# word = "incredible"
# print the letter if the index is even
# otherwise do nothing

# exercise 4e
# word = "incredible"
# print letters by batch of 2
# "in", "cr", "ed", "ib", "le"

# exercise 4a
for num in range(0, 31):
    if num % 2 == 0:
        print("number " + str(num) + " is even")
    else:
        print("number " + str(num) + " is odd")

print()

#exercise 4b
input_num = int(input("Enter a number:"))
while(input_num % 2 == 0):
    input_num = int(input("Enter a number:"))
     
print()

#exercise 4c
result = 0
for num in range(0, 16):
    result += num
print(result)
    
print()

#exercise 4d
word = "incredible"
i = 0
x = len(word)-1
while (i < x):
    if i % 2 == 0:
        print(word[i])
    i += 1

print()

# exercise 4e
i = 0
x = len(word)
while (i < x):
    if i % 2 == 1:
        print(word[i - 1:i + 1])
    i += 1