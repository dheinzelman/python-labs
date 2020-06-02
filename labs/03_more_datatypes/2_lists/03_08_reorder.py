'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
list1 = []

for a in range(0,10):
    number = int(input("please enter a number: "))
    list1.append(number)

print(list1)
print(list1[1], list1[3], list1[5], list1[7], list1[9])
print(list1[8], list1[6], list1[6], list1[4], list1[0], )