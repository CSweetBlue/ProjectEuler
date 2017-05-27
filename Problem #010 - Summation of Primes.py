"""
Find the sum of all the primes not greater than given n.
"""
import bisect

t = int(input().strip())

firstPrime = 2
listOfPrimes = [firstPrime]
sumOfPrimes = [firstPrime]

for _ in range(t):
    n = int(input().strip())
    toReturn = 0
    
    if n < 0:
        print(0)

    else:
        while listOfPrimes[-1] <= n:
            firstPrime += 1
            for ele in listOfPrimes:
                if firstPrime < ele * ele:
                    listOfPrimes.append(firstPrime)
                    sumOfPrimes.append(firstPrime + sumOfPrimes[-1])
                    
                    break

                if firstPrime % ele == 0:
                    break
            
        print(sumOfPrimes[bisect.bisect(listOfPrimes, n) - 1])
