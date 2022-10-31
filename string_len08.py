def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    if len(s)%2==1:
        x=len(s)
        a=x-(x//2)
        return s[a-1]
    if len(s)%2==0:
        x=len(s)
        a=x//2
        b=a+1
        return s[a-1]+s[b-1]
print(main("casdsl"))