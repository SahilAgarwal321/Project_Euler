'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
def diff(x):
    sum1= 0
    for i in xrange(1,x+1):
        sum1 += i**2
    sum2 += i
    return (sum2**2) - sum1

diff(100)