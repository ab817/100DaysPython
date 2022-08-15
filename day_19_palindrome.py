#check if the string is palindrome

def is_palindrome(phrase):
    return phrase == phrase [::-1]

str = input("Enter the phrase to check if string is palindrome")

print(is_palindrome(str))

#True or False