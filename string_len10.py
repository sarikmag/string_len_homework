def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    a=s[0]
    b=s[1]
    c=s[2]
    z=c+b+a
    if z==s:
        return True
    else:
        return False
    
print(main("asd"))