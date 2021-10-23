import math

def quadratic_equation(a = 0, b = 0, c = 0):
    if a == 0:
        raise Exception("The provided equation was not a second-degree equation.")

    delta = b**2 - 4*a*c

    if delta < 0:
        raise Exception("Delta was less than 0. There are no solutions to the equation.")
    
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    return x1, x2


# add here three nums as arguments
soltions = quadratic_equation()
print("x1: " + str(soltions[0]) + "\nx2: " + str(soltions[1]))