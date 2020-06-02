'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
my_dict = {}
items = input (f' how many items would you like to add? ')
for i in range (int(items)):
    my_dict[i+1] = (i+1)*(i+1)

print(my_dict)