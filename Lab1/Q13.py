# You are given a string and your task is to swap cases. In other words, convert all lowercase letters 
# to uppercase letters and vice versa.

def swap_case(string):
    strings = []
    for char in string:
        if char == char.lower():
            new_char = char.upper()
            strings.append(new_char)
        elif char == char.upper():
            new_char = char.lower()
            strings.append(new_char)
        else:
           strings.append(char) 
    swapped_strings = "".join(strings)
    return swapped_strings

user_word = input("Enter any string: " )
case_swapped = swap_case(user_word)
print(case_swapped)