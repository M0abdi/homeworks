

#We need to compare characters from start and end until the middle

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example
print(is_palindrome("tenet"))  
print(is_palindrome("hello"))    
print(is_palindrome("a"))       
