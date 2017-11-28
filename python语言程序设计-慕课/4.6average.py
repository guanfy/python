def ave_1():
    """
    需要用户提供输入个数
    for 循环提供固定的循环次数
    """
    n = eval(input("How many number are there:"))
    sum = 0.0
    for i in range(n):
        x  = eval(input("Enter a number>>>"))
        sum += x
    print("\nThe average is :",sum/n)

def ave_2():
    """
    交互式循环 
    询问是否还有数据需要发送
    """
    sum = 0.0
    count = 0 
    moredata = "yes"

    while(moredata[0] == 'y'):
        x = eval(input("Enter a number>>>"))
        sum += x
        count = count+1
        moredata = input("Do you have more numbers(yes or no)?")
    print("\nThe average is :",sum/count)

def ave_3():
    """
    哨兵 ： 负数，空字符串
    """
    sum = 0.0
    count = 0 

    x = input("Enter a number（<Enter> to quit）>>>")
    while(x != ''):
        x = eval(x)
        sum += x
        count = count+1
        x = input("Enter a number（<Enter> to quit）>>>")
    print("\nThe average is :",sum/count)

def main():
    ave_1() 
    ave_2()   

main()