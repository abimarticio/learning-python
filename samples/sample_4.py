# conditional statements

age = int(input("How old are you? "))

# and, not, or
# and = both conditions must be true
# this lane is for senior citizen and pwd only -- this is wrong
# or = at least one condition is true
# this lane is for sc or pwd only
# not = negation
# not True
if age < 30 and age >=0:
    print("You are less than 30 years old.")
elif age >= 30 and age <= 60:
    print("You are within 30 to 60 years of age")
elif age < 0:
    print("You gave an invalid age.")
else:
    print("You are not within 0 to 60 years old.")

result = "You are less than 30 years old" if age < 30 else\
 "You are not less than 30 years old"
print(result)