'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
user_input = str(input("Please enter a sentence: "))

words = user_input.split()

def most_frequent(words):
    counter = 0
    num = words[0]

    for i in words:
        curr_frequency = words.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

print(words)
print(most_frequent(words))