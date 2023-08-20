def palindrome_number(number):
    """
    Check if an integer is a palindrome.

    Args:
        number (int): The integer to be checked.

    Returns:
        bool: True if the integer is a palindrome, False otherwise.
    """
    if number < 0:
        return False

    # Convert the integer to a string and compare it with its reverse.
    # Using case-insensitive comparison to handle both upper and lower case letters.
    if str(number).lower() == str(number)[::-1].lower():
        return True

print(palindrome_number(-121))  # Output: True

