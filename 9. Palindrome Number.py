class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the input integer is negative
        if x < 0:
            return False
        
        # Convert the integer to a string
        convert = str(x)
        
        # Compare the original string with its reverse to determine if it's a palindrome
        if convert == convert[::-1]:
            return True
