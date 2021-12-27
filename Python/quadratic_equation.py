import math
import sys

def quadratic_equation(a = 0, b = 0, c = 0):
    if a == 0:
        raise Exception("The provided equation was not a second-degree equation.")

    delta = b**2 - 4*a*c

    if delta < 0:
        raise Exception("Delta was less than 0. There are no solutions to the equation.")
    
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    return x1, x2

def main():
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
    except ValueError:
        print('You input in a wrong manner.')
        console()
        return
    except:
        sys.exit(1)

    soltions = quadratic_equation(a, b, c)
    print("x1: " + str(soltions[0]) + "\nx2: " + str(soltions[1]))


def console():
    try:
        command = str(input('console: '))
        if command == 'e':
            sys.exit(0)
        elif command == 'r':
            main()
        else:
            print(f'{command} is not a command for this script ({__name__}).')
            console()
    except:
        sys.exit(1)



if __name__ == "__main__":
    console()