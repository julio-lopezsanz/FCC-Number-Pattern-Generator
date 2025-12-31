"""
In this lab you will practice the basics
of Python by building a small app that 
creates a number pattern.
"""

def number_pattern(n):
    """
    creates a number pattern
    """
    numbers = []
    if not isinstance(n,int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    for i in range(1,n+1):
        numbers.append(i)
    union = " ".join(map(str, numbers))
    return union

print(number_pattern(12))
