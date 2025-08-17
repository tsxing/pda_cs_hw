import math
t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 6:
        print(15)
    elif n <= 8:
        print(20)
    elif n <= 10:
        print(25)
    else:
        # each slice is 2.5 mins
        # 2 slices is 5 mins
        ans = ((n+1)//2) *5
        print(ans)
