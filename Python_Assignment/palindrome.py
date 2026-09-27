def check_palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome("madam")  
check_palindrome("hello")  