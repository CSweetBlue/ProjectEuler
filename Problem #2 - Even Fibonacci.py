t = int(input())

for _ in range(t):
    n = int(input())
    sum = 0
    
    first = 1
    second = 2
    
    while second <= n:
        if second % 2 == 0:
            sum += second
        
        temp = second
        second = first + second
        first = temp
    
    print(sum)
