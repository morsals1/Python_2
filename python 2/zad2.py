def group_characters(input_string):
    characters = input_string.split()

    grouped = {}

    for char in characters:
        if char in grouped:
            grouped[char].append(char)
        else:
            grouped[char] = [char]


    result = list(grouped.values())

    return result

input_string = input()
output = group_characters(input_string)
print(output)