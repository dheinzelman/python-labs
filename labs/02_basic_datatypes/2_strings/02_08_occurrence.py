'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
#get user input (sentence)
sentence = str(input("Please enter a sentence: "))
#get user input (symbol)
letter = input("Please enter a letter: ")
#find the index of first occurrence of the user's letter
print("Result: " + str(sentence.find(letter)))