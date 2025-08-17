from math import gcd
n = int(input())
coprimes = [x for x in range(1, n) if gcd(x, n) == 1]
prod = 1
for num in coprimes:
    prod = (prod *num)%n

if prod !=1:
    coprimes.remove(prod)

print(len(coprimes))
print(*coprimes)
    
