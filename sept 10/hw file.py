
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
#didn't understand, but i figure that if a[n] == 0, it can work. Also, if a[1] == 1, then n+1 can get to 1, so it also works. not that sure for the middle though


# this is for reverse engineering
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    inputs = []
    results = []
    for _ in range(m):
        s = input().strip()
        inputs.append(s[:-1])
        results.append(s[-1])
    programs = [i for i in range(m)]
    while True:
        updated = False
        for i in range(n):
            if updated:
                break
            offvals, offinputs, onvals, oninputs = set(), [], set(), []
            for j in programs:
                if inputs[j][i] == '1':
                    onvals.add(results[j])
                    oninputs.append(j)
                else:
                    offvals.add(results[j])
                    offinputs.append(j)
            if len(offvals) <= 1 and len(onvals) <= 1:
                print("OK")
                break
            if len(offvals) == 0 or len(onvals) == 0:
                continue
            if len(offvals) == 2 and len(onvals) == 2:
                continue
            if len(offvals) == 1:
                updated = True
                programs = oninputs
            elif len(onvals) == 1:
                updated = True
                programs = offinputs
            else:
                print("LIE")
                break
        else:
            if not updated:
                print("LIE")
        if len(offvals) <= 1 and len(onvals) <= 1:
            break



