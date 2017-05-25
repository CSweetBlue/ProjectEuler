t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    first = sum(range(1, n + 1)) ** 2
    second = 0
    
    for i in range(1, n + 1):
        second += i*i
    
    print(int(first - second))
