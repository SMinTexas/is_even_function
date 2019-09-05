# Write a function that accepts a number as an argument and returns a Boolean
# value. Return True if the number is even; return False if it is not even.

def is_even(input_number):
    if input_number % 2 == 0:
        return True
    else:
        return False

try:
    num = int(input("Please enter any number "))
    if is_even(num) == True:
        print(f'{num} is an even number!')
    else:
        print(f'{num} is not an even number!')
except ValueError:
    print(f"{num} is not a number.")