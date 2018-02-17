# dependencies
import os

# storing file path
file_one = 'Resources/paragraph_1.txt'
file_two = 'Resources/paragraph_2.txt'

# declaring & initializing variables
letter_count = 0

# opening file1 // maybe add a loop to account for file2
with open(file_one, 'r') as txtfile:
    # reading file
    paragraph = txtfile.read()

    # finding word count
    word_count = paragraph.count(" ") + 1 # +1 to account for the last word

    # finding sentence count anything that has ".", "!", "?" (ends of sentences)
    sentence_count = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")

    # finding average letter count and use .isalpha()
    for character in paragraph:
        if character.isalpha():
            letter_count += 1 # counting how many characters are letters
    avg_letter_count = letter_count/word_count

    # finding average sentence length
    avg_sentence = word_count/sentence_count

# tests
# print(word_count)
# print(sentence_count)
print(letter_count)
# print(avg_letter_count)
# print(avg_sentence)
