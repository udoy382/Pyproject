import time

def fiboIter(n):
    PrevNum = 0
    currentNum = 1
    for i in range(1, n):
        previousNum = PrevNum
        PrevNum = currentNum
        currentNum = PrevNum + previousNum

    return currentNum

def fiboRecur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fiboRecur(n-1) + fiboRecur(n-2)

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    init = time.time()
    print(f"Using recursions value of fib ({num}) is {fiboRecur(num)}")
    # print(f"Using Iter value of fib ({num}) is {fiboIter(num)}")
    print(f"It took {time.time() - init} seconds")