def palindrome(string):
    if string==string[::-1]:
        return True
    else:
        return False
    
print(palindrome('лепсспел'))
print(palindrome('Привет'))