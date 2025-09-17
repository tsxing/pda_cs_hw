
#https://codeforces.com/problemset/problem/1419/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    if n % 2 == 1:  # odd 
   
        found = any(int(s[i]) % 2 == 1 for i in range(0, n, 2))
        print(1 if found else 2)
        
    else:  # even?
        found = any(int(s[i]) % 2 == 0 for i in range(1, n, 2)) 
        print(2 if found else 1)


#https://codeforces.com/contest/1382/problem/B
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    while k < n and a[k] == 1:
        k += 1
    if ((k == n) ^ (k % 2)):
        print("Second")
    else:
        print("First")


#https://codeforces.com/problemset/problem/1559/C
didn't understand
