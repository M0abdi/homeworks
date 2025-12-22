


def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

#test
print(is_palindrome("racecar"))  
print(is_palindrome("hello"))    
