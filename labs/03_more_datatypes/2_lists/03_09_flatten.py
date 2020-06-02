'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = []

for i in range(len(starting_list)):
  for j in range (len(starting_list[i])):
    flattened_list.append(starting_list[i][j])

print("Original List:",starting_list)
print("Flattened List:",flattened_list)