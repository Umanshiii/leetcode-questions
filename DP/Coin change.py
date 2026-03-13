'''
Given an amount and the denominations of coins available, determine how many ways
change can be made for amount. There is a limitless supply of each coin type.

Example
n=3
c = [8,3, 1, 2]

There are 3 ways to make change for n = 3: {1, 1, 1}, {1, 2}, and {3}.
'''

def getWays(n, c):
    # Write your code here
    m = [0] * (n + 1)
    m[0] = 1

    for i in c:
        for j in range(i, n + 1):
            m[j] += m[j - i]

    count = m[n]
    return count
