'''
Create a python function to display the squareroot of a given number.
'''
import math
def square_root(number):
    if number >= 0:
        result = math.sqrt(number)
        print("Square root of",number, 'is:',result)
    else:
        print("Cannot show the square root of a negative number.")

square_root(121)