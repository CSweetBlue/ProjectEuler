"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to N?
"""

t = int(input())

for _ in range(t):
    n = int(input())
    
    #If n wasn't such a restricted range, I'd implement a prime factor function.
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    toReturn = 1
    
    for i in primes:
        if i <= n:
            temp = i
            while temp*i <= n:
                temp *= i
            
            toReturn *= temp
        
        #For large prime lists, this would reduce check time.
        else:
            break

    print(toReturn)
