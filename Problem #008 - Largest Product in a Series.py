"""
Find the greatest product of K consecutive digits in the N digit number.
"""

t = int(input().strip())

for _ in range(t):
    n,k = input().strip().split(' ')
    n,k = int(n), int(k)
    num = input().strip()
    
    digitSplit = [int(x) for x in str(num)]
    
    max = 0
    
    for startIndex in range(n - (k-1)):
        temp = 1
        
        subRange = digitSplit[startIndex:startIndex + k]
        
        for val in subRange:
            temp *= val
            
        if temp > max:
            max = temp
    
    print(max)
