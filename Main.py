import cmath
from time import time


def is_mandelbrot(x, y):
    """
    Input coordinates of complex number of the form c = x + yi.
    Return True if the number belongs to the set.
    """
    c = x + y*1j
    z = 0 #z is the iterated number
    for i in range(0, 100):
        z = z**2 + c
        if abs(z) > 2: #If z>2, z diverges and does not belong to the set
            return False
    return True


def represent_mandelbrot_text(n):
    """
    Strictly text representation of the mandelbrot set
    """
    for Y in range(n):
        y = (n//2-Y)/(n//2)
        for X in range(n*3):
            x = (X/n)-2.1
            if is_mandelbrot(x, y):
                print("*", end="")
            else:
                print(" ", end="")
        print("")

