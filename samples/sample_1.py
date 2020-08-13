# input/output
# I/O
print("this is a statement")
#System.out.println();
name = input("What's your name? ")
print("Hello, {}".format(name))
age = input("what's your age? ")
print("you are {} years old".format(age))
print(type(age))
print("Hello, {}. You are {} years old.".format(name, age))
print("hello, {name}. You are {age} years old.".format(age=age, name=name))