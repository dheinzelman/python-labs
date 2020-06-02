'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
user_list = []
while True:
    new_num = input("type a number, or 'x' when done: ")
    if new_num.lower() == 'x':
        break
    else:
        user_list.append(new_num)

print(f"Numbers as typed: {user_list}")

sorted_tuple = tuple(sorted(user_list))
new_list = []
print(f'sorted tuple: {sorted_tuple}')

print(new_list)
#distributes list into tuples of 2
print(sorted_tuple[1])

for i in range(len(sorted_tuple)):
        new_list.append(sorted_tuple[i] + sorted_tuple[i+1])

print(new_list)