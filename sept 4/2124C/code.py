import math
import sys
# we discussed this in class
def lcm(a, b):
    return a//math.gcd(a, b)*b

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    ans = 1
    for i in range(n-1):
        g = math.gcd(b[i], b[i+1])
        ti = b[i] // g
        ans = lcm(ans, ti)
    print(ans)
