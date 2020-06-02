'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
list1 = []

for a in range(0,10):
    number = int(input("please enter a number: "))
    list1.append(number)

mul=1
for i in range(0,10):
    mul=mul*list1[i]

print(mul)
