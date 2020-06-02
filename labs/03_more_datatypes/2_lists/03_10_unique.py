'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list1 = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

not_duplicate = [x for x in list1 if list1.count(x) == 1]

print(not_duplicate)