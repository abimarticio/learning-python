import sys

# define a function for reading the string from a text file
def load_data(filename: str) -> list:
    with open(filename, "r") as text_file:
        data = text_file.readlines()
    return data
   
# define a function for getting a nested list of strings
# from the load_data() output
# i.e. ["raining", "rainning, raning"]
def get_list(data: list) -> list:
    data = [line.strip("\n") for line in data]
    lines = [] 
    for line in data:
        new_line = line.split(":")
        lines.append(new_line)
    return lines

# define a function for crating a dictionary
# out of the get_list() output
# {"raining": ["rainning", "raning"]}
def create_dictionary(lines: list) -> dict:
    corrections = {}
    for line in lines:
        key = line[0]
        values = line[1]
        values = values.strip()
        if "," in values:
            values = values.split(",")
            new_values = []
            for value in values:
                value = value.strip()
                new_values.append(value)
                values = new_values
                corrections[key] = values
        else:
            corrections[key] = values
    return corrections

# define a function for inverting the dictionary
# { "rainning": "raining", "raning": "raining"}
def invert_dictionary(corrections: dict) -> dict:
    dictionary = {}
    for key, value in corrections.items():
        if isinstance(value, str):
            dictionary[value] = key
        elif isinstance(value, list):
            for element in value:
                dictionary[element] = key
    return dictionary

def get_correction(word: str, dictionary: dict) -> str:
    correct_word = dictionary.get(word)
    return correct_word

def get_batch_correction(words: list, dictionary: dict) -> list:
    correct_words = []
    for word in words:
        correct_word = get_correction(word=word, dictionary=dictionary)
        correct_words.append(correct_word)
    return correct_words

# define a main function that loads
# the spell-errors.txt
# and uses the loaded dictionary
# ["rainning", "raning"]
def main():
    data = load_data("spell-errors.txt")
    data = (data[:50])
    lines = get_list(data=data)
    corrections = create_dictionary(lines=lines)
    dictionary = invert_dictionary(corrections=corrections)
    texts = sys.argv[1:]
    correct_texts = get_batch_correction(words=texts, dictionary=dictionary) 
    for text, correct_text in zip(texts, correct_texts):
        print(f"{text} => {correct_text}")
    # texts = ["rainning", "raning", "writtings", "forer"]
    # correct_texts = get_batch_correction(words=texts, dictionary=dictionary)
    # for text, correct_text in zip(texts, correct_texts):
    #     print(f"{text} => {correct_text}")
    # print(sys.argv)

main()