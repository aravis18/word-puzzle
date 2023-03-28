import nltk
nltk.download('words')
nltk.download('wordnet')
from nltk.corpus import words, wordnet

def find_largest_word(letters):
    word_list = words.words()
    largest_word = ""
    for word in word_list:
        is_possible_word = True
        for letter in set(word):
            if word.count(letter) > letters.count(letter):
                is_possible_word = False
                break
        if is_possible_word and len(word) > len(largest_word):
            largest_word = word
    return largest_word

# Ask the user to input the letters
input_letters = input("Enter a list of letters: ")

# Remove any spaces and convert to lowercase
input_letters = input_letters.replace(" ", "").lower()

# Call the function to find the largest word
largest_word = find_largest_word(input_letters)

if largest_word:
    print("The largest English word that can be formed using the letters", input_letters, "is", largest_word)
    synsets = wordnet.synsets(largest_word)
    if synsets:
        print("Meaning:", synsets[0].definition())
    else:
        print("Meaning: No definition found.")
else:
    print("No English word can be formed using the letters", input_letters)
