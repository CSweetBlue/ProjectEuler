t = int(input().strip())

firstPrime = 2
listOfPrimes = [firstPrime]

for _ in range(t):
    n = int(input().strip())

    while len(listOfPrimes) < n:
        firstPrime += 1
        for ele in listOfPrimes:
            if firstPrime < ele * ele:
                listOfPrimes.append(firstPrime)
                break
            if firstPrime % ele == 0:
                break
          
    print(listOfPrimes[n-1])
