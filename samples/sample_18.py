# recursive function

# 5! = 120
# 5! = 5 * 4 * 3 * 2 * 1
# 4! = 24
# 4! = 4 * 3 * 2 * 1
# 3! = 6
# 3! = 3 * 2 * 1
# 2! = 2
# 2! = 2 * 1
# 1! = 1
# 0! = 1

# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!
# 0! = 1

def factorial(number: int) -> int:
    if number == 0:
        return 1

    else: 
        return number * factorial(number - 1)

        # number = 5
        # 5 * factorial(4)
        # 4 * factorial(3)
        # 3 * factorial(2)
        # 2 * factorial(1)
        # 1 * factorial(0)

print(factorial(5))