with open("spell-errors.txt", "r") as spell_error_file:
    data = spell_error_file.readlines()

data = [line.strip("\n") for line in data]


lines = [] # lines = list()
for line in data:
    new_line = line.split(":")
    lines.append(new_line)

corrections = {}

for line in lines:
    key = line[0]
    values = line[1]
    values = values.strip()
    # key = "raining"
    # values = "rainning, raning"
    # values = "tigar"
    # conditional for possible lists
    if "," in values:
        # this gives us a list
        # ["rainning", " raning"]
        values = values.split(",")

        # create a variable to
        # store processed values
        # because we want to strip
        # the leading and trailing whitespaces
        new_values = []
        for value in values:
             # rmove whitespaces
            value = value.strip()
            #store the words without whitespaces
            new_values.append(value)
            
            # store the processed words
            # into values
            values = new_values
            corrections[key] = values
    else:
        # for strings only
        corrections[key] = values

results = {}
for key, value in corrections.items():
    if isinstance(value, str):
        results[value] = key
    elif isinstance(value, list):
        for element in value:
            results[element] = key