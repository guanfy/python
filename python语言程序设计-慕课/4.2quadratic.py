# usr/bin/python
import math 

def quadratic_v1():
    print("This program find the real solutions to a quadratic!")
    a,b,c = eval(input("Please enter the coefficients(a,b,c):\n"))
    if a == 0:
        if b == 0:
            print("Wrong arg!\n")
        else:
            root = c/b
            print("\nThe solution is:",root)
    else:
        delta = b**2-4*a*c
        if delta > 0:
            delta = math.sqrt(delta)
            root1 = (-b + delta)/(2*a)
            root2 = (-b - delta)/(2*a)
            print("\nThe solutions are:",root1,root2)
        elif delta == 0:
            root = -b/(2*a)
            print("\nThis is a double root:",root)
        else:
            print("\nNo real roots!")
def main():
    '''
    quadratic_v1()
    exit(0)
    '''
    print("This program find the real solutions to a quadratic!")
    try:
        a,b,c = eval(input("Please enter the coefficients(a,b,c):\n"))
        delta = math.sqrt(b**2-4*a*c)
        if delta == 0:
            root = root = -b/(2*a)
            print("\nThis is a double root:",root)
        else:
            root1 = (-b + delta)/(2*a)
            root2 = (-b - delta)/(2*a)
            print("\nThe solutions are:",root1,root2)
    except ValueError as excObj:
        if str(excObj) == "math domian error":
            print("No real roots!")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError:
        print("You didn't enter three numbers.")
    except TypeError:
        print("\nYour inputs were not all number.")
    except SyntaxError:
        print("\nYour input was not in correct form.Miss Comma?")
    except:
        print("\nSomething went wrong,sorry!")


main()