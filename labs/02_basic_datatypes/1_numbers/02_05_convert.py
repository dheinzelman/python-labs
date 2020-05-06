'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
float(57) #putting any integer in the parentheses will convert it to a float

int(390.8) #putting any float in the parentheses will convert it to a integer

138.93//3 #this would be how to perform floor division with a float and an int

#below is how to use two user inputted values to perform multiplication
hours = input("Enter number of hours worked\n")
hours = int(hours)
rate = input("Enter pay rate per hour\n")
rate = int(rate)
print(hours * rate)