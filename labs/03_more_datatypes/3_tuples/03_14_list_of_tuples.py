'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
user_input = str(input("Please enter a sentence: "))

wordsplit = user_input.split()

list_=[]

for word in wordsplit:
    list_.append(tuple(word))

print(list_)