'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def isPalindrome(num):
    return str(num) == str(num)[::-1]

In [98]: def palin3():
    highest = 0
    for i in xrange(999, 100, -1):
        for j in xrange(i, 100, -1):
            x = i*j
            if isPalindrome(x):
                if x>highest : highest = x
    return highest