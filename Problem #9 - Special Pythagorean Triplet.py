t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    max = -1
    
    for a in range(1, (n//3) + 1):
        
        b = int(((a ** 2) - ((a - n) ** 2))/(2 * (a-n)))
        c = n - a - b
        
        product = (a*b*c)

        if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == n) and (product > max) and (product != 0):
            max = product
    
    print(max)
