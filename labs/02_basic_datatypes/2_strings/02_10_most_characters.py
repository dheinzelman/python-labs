'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
user_str1 = str(input("Please enter a word: "))
user_str2 = str(input("Please enter a another word: "))
user_str3 = str(input("Please enter one last word: "))

print(str(len(user_str1)) + ", " + str(user_str1))
print(str(len(user_str2)) + ", " + str(user_str2))
print(str(len(user_str3)) + ", " + str(user_str3))