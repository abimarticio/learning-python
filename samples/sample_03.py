# primitive data types
# integer, float, string, boolean

x = 10
y = 2.0
word = "quick"
is_lower = False

# outputs a floating point
# due to y being a float
print(f"{x} - {y} = {x - y}")
print(f"{x} / {y} = {x / y}")

# convert int to float
x = float(x)
print(type(x))
print(isinstance(x, float))
print(isinstance(x, str))

# slicing
# q = word[0]
# u = word[1]
# i = word[2]
# c = word[3]
# k = word[4]
print(word[0])
# var[start:stop:step]
print(word[1:])
print(word[1:4])
print(word[1:3])
print(word[4])
print(len(word))
print(word[len(word) - 2])
print(word[-1])
print(word[-2])
print(word[:5])
# print kciuq
print(word[::-1])
print(word[:4][0]) # print "q"

# word = racecar
# word_1 = race
# word_2= care
word = "racecar"
word_1 = (word[0:4]) # "race"
word_2 = (word[4:] + word[3]) # "care"
print(word_1)
print(word_2)

print(word.upper())
print(word.upper().lower())
print(word.lower())
print(word.islower())
print(word.isupper())
print(word.upper().isupper())
is_lower = word.islower()
print(is_lower)

# x = 10, y = 2.0
# follows pemdas
print(x + y * x) # 30

text = "The quick brown fox jumps over the lazy dog"
print(text)
print(text.lower())
words = text.split()
print(words)
print(words[:4])
# [start:stop:step]
print(words[::-1])
print(word.split())