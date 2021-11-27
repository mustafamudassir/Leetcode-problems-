'''9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome
when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

'''

def palindrome_number(number):
    if number < 0:
        return  False
    convert = str(number)
    if convert.lower() == convert[::-1].lower():
        return True

print(palindrome_number(-121))
