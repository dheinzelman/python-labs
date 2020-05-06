'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
user_word = input("Enter your name: ")

ay = "ay"
first_letter = user_word[0]
first_letter = str(first_letter)
length_of_word = len(user_word)
remove_first_letter = user_word[1:length_of_word]
pig_latin=remove_first_letter+first_letter+ay
print("The name in Pig Latin is:",pig_latin)