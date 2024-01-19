import string

def generate_combinations():
    alpha = string.ascii_lowercase
    num =  string.digits
    characters = alpha + num  # Alphanumeric characters (uppercase letters + lowercase letters + digits)
    combinations = []

    for char1 in characters:
        for char2 in characters:
            for char3 in characters:
                for char4 in characters:
                    if((char1 in alpha or char2 in alpha or char3 in alpha or char4 in alpha) and (char1 in num or char2 in num or char3 in num or char4 in num)):
                        combination = char1 + char2 + char3 + char4
                        combinations.append(combination)
    return combinations

def write_to_file(combinations, filename='combinations-4.txt'):
    with open(filename, 'w') as file:
        for combination in combinations:
            file.write(combination + '\n')

# Example usage:
result = generate_combinations()
write_to_file(result)