a = 1
b = 2
c = 3

while not (a**2 + b**2 == c**2 and a + b + c == 1000):
    c += 1
    
    if a + b + c > 1000:
        b += 1
        c = b + 1
    
    if a + b + c > 1000:
        a += 1
        b = a + 1
        c = b + 1

print(a, b, c)