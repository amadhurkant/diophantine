import sys

def pRed(string):
    """Fancy - prints text in red"""
    print("\033[91m {}\033[00m" .format(string))

def pGreen(string):
    """Fancy - prints text in green""" 
    print("\033[92m {}\033[00m" .format(string))

def gcd(a:int, b:int) -> int:
    """
    Given two integers returns the integer
    Greatest Common Divisor (GCD) of them.
    
    To get gcd of more than two numbers use `gcd_mult`
    """
    while b:
        a, b = b, a % b
    return abs(a)

def gcd_mult(*args:int) -> int:
    """
    Returns the Greatest Common Divisor (GCD) of more 
    than two integers.
    
    To get gcd of two numbers use `gcd`
    """
    if not args:
        raise ValueError("At least one number is required")
    
    result = abs(args[0])
    for num in args[1:]:
        result = gcd(result, abs(num))
        if result == 1:
            return 1
    return result

def is_integral_sol_exist(a:int, b:int, c:int) -> bool:
    """
    This function returns `True` if there exist integral
    solution to a diophantine equation in two variables
    else returns `False`.
    
    For a diophantine equation `ax+by = c` integral solution
    exists if `gcd(a, b)|c`
    """
    return c % gcd(a, b) == 0

def get_bezout(a:int, b:int, d:int) -> tuple:
    """Given two integers `a` and `b` and their gcd `d`
    finds integers `s` and `t` such that `a*s + b*t = d`
    
    These coefficients are called Bezout's coefficients."""
    
    assert gcd(a, b) == d, 'Incorrect GCD'
    
    # Extended Euclidean Algorithm to find Bezout coefficients
    a, b, s1, s2, t1, t2 = abs(a), abs(b), 1, 0, 0, 1
    while b:
        q, r = divmod(a, b)
        a, b, s1, s2, t1, t2 = b, r, s2, s1 - q * s2, t2, t1 - q * t2
    
    # Adjust signs based on original gcd value
    return (s1 if d == abs(d) else -s1, t1 if d == abs(d) else -t1)

def particular_solution(a:int, b:int, c:int) -> tuple:
    """
    Return a pair particular solution (x0, y0) 
    to a linear diophantine in two variables.
    
    A. Checks if solution exists
        a. Exits the program if no solution exists
    
    B. Get Bezout coefficient
    
    C. Calculate particular solutions, return as `tuple`
    """
    
    if not is_integral_sol_exist(a, b, c):
        pRed("Fatal: Linear Diophantine has no integral solution")
        sys.exit(1) #!imp: Re-consider later
    
    d = gcd(a, b)
    s, t = get_bezout(a, b, d)
    m = c // d
    x0, y0 = s * m, t * m
    
    # Assertion to ensure correctness of the computed particular solution
    assert (a * x0) + (b * y0) == c
    
    return x0, y0

def general_solution(a:int, b:int, c:int, invert_solution=False, prnt=False) -> list:
    """
    Return the general solution to a linear 
    diophantine in two variables
    as tuple inside list `[[x0, b/d], [y0, -a/d]]` 
    where `d` is gcd of `a` and `b`
    and `x0`, `y0` are particular solutions.
    
    A user can derive any solution by multiplying
    arbitrary integer `t` to `b/d` or `-a/d` 
    then adding `x0` and `y0` as the case may be.
    """
    d = gcd(a, b)
    sol = particular_solution(a, b, c)
    if sol is False:
        return []
    x0, y0 = sol
    xm, ym = b // d, -a // d
    
    # Assertion to verify correctness of general solution pattern
    assert a * (x0 + xm) + b * (y0 + ym) == c

    if prnt:
        print("General Solutions are: ")
        pGreen(f"x = {x0} + {xm}t, y = {y0} {ym}t")
    
    return [(x0, -xm), (y0, -ym)] if invert_solution else [(x0, xm), (y0, ym)]