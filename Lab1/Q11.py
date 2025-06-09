# WAP to ask for a sentence and calculate the frequency of characters in the sentences.

def count_char(sentence):
    for char in set(sentence):
        count = sentence.count(char)
        print(f"'{char}': {count}")

sentence = input("Enter any sentence:\n")

char_count = count_char(sentence)

