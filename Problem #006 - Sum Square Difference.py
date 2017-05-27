"""
Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.
"""

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    squareOfSum = sum(range(1, n + 1)) ** 2
    sumOfSquares = 0
    
    for i in range(1, n + 1):
        sumOfSquares += i*i
    
    print(int(squareOfSum - sumOfSquares))
