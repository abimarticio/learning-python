# combining two lists
list_a = ["a", "b", "c"]
list_b = ["d", "e", "f"]
list_c = list_a + list_b
print(list_c)

# insert a value at index i
# of an array
list_a.insert(1, "2a")
print(list_a)
list_b.insert(2, "2e")
print(list_b)

names = ["Adam", "Bill", "Carl", "David", "Eve"]
# equivalent, in java, .contains()
is_in_list = "Adam" in names # check if "Adam" is in names
print(is_in_list)
not_in_list = "Adam" not in names
print(not_in_list)

names = ["Lara", "Gab", "Keean", "Carlos", "Francis", "Hazel"]
sorted_names = sorted(names)
print(sorted_names)

# the key is the incorrect word
# the value is the correct word
corrections = {"rainning": "raining", "raning": "raining"}
text_input = "rainning"
print(corrections.get("rainning"))

sample_dictionary = {"key_1": "value_1", "key_2": "value_2"}
# declare empty dictionary
result = {}
# result = dict()
for key, value in sample_dictionary.items():
    result[value] = key
print(result)

sample_dictionary = {value: key for key, value in sample_dictionary.items()}
print(sample_dictionary)

corrections = {"raining": ["rainning", "raning"]}
print(corrections)
text_input = "rainning"

# time complexity
# 0(mn)
result = dict()
for key, value in corrections.items():
    for element in value:
        result[element] = key
print(result)
text_output = result.get(text_input)
print(f"{text_input} => {text_output}")

print()

corrections = {"raining": ["rainning", "raning"],
                "the": "teh",
                "brown": ["broown", "brownn"],
                "across": "acriss"}

results = {}
for key, value in corrections.items():
    if isinstance(value, str):
        results[value] = key
    elif isinstance(value, list):
        for element in value:
            results[element] = key

incorrect_words = ["teh", "acriss", "broown", "raning"]
for incorrect_word in incorrect_words:
    correct_word = results.get(incorrect_word)
    print(f"{incorrect_word} => {correct_word}")