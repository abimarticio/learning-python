# reading files
# open modes
# "r" is read
# "w" is write
# "a is append"
with open("big.txt", "r") as text_file:
    data = text_file.readlines()
print(data[:5])

numbers = []
for number in range(10):
    numbers.append(number)
# list comprehensions
numbers = [number for number in range(10)]
print(numbers)

sentence = "The quick brown fox jumps over the lazy dog"
sentence = sentence.split()
print([word for word in sentence])

lines = [line.strip("\n") for line in data]
print(lines[:5])