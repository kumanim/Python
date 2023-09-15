'''
Task2
Create a python function to take three numbers as input, comapre them with each other.
If a number matches with another, display number1 matches with number 2 and similar for other comparison
'''
def compare_numbers(num1, num2, num3):
    if num1 == num2:
        print("num1 matches num2")
    if num1 == num3:
        print("num1 matches num3")
    if num2 == num3:
        print("num2 matches num3")
num1 = 90
num2 = 85
num3 = 90
compare_numbers(num1, num2, num3)