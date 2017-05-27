"""
What is the largest prime factor of a given number N?
"""

t = int(input())

for _ in range(t):
    n = int(input())
    
    factorList = []
    current = 2
    
    while n > 1:
        while n % current == 0:
            factorList.append(current)
            n /= current
        current += 1
        
        if current * current > n:
            if n > 1: 
                factorList.append(n)
            break

    print(int(max(factorList)))
