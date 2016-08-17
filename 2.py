'''By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
def fibonacci_sum(n):
    fibonaci = [1,1]
    while fibo[-1] <n:
        fibo.append(fibo[-1]+fibo[-2])
    fib = [i for i in fibo if i%2==0 and i<n]
    return sum(fib)

fibonacci_sum(4000000)