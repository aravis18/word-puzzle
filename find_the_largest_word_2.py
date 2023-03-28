import nltk
nltk.download('words')
from nltk.corpus import words

def find_largest_word(letters):
    word_list = words.words()
    largest_word = ""
    for word in word_list:
        if set(word).issubset(set(letters)):
            if len(word) == len(set(word)) and len(word) > len(largest_word):
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
else:
    print("No English word can be formed using the letters", input_letters)
