def least_difference(a, b, c):
    """
    Returns a smallest difference between any two numbers among a, b, and c
    
    Input: Three integers
    
    Output: Minimum difference between three integers
    
    >>> least_difference(5, 6, 7)
    2
    """
    diff1 = a - b
    diff2 = b - c
    diff3 = a - c
    return abs(min(diff1, diff2, diff3))

print(
      least_difference(100, 50, 101),
      least_difference(1, 10, 10),
      least_difference(5, 6, 7)
      )


