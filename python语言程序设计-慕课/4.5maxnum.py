# usr/bin/python

def main():
    """
    N者最大值: python内置函数max()
    """
    n = eval(input("How many number are there:"))
    max = eval(input("Enter a number>>>"))
    for i in range(n-1):
        x = eval(input("Enter a number>>>"))
        if x > max:
            max = x
    print("The large value is ",max)


