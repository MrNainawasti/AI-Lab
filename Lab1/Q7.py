# WAP to ask for a sentence and count the number of words.

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter any sentence:\n")
word_count = count_words(sentence)
print(word_count)