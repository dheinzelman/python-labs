'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
vowels = 'aeiou' # string of vowels

user_str = input("Please enter a sentence: ")

user_str = user_str.casefold() # remove concern about case

count = {}.fromkeys(vowels,0) # make a dictionary with each vowel a key and value 0

# count the vowels
for char in user_str:
   if char in count:
       count[char] += 1

print(count)