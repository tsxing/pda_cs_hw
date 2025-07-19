from collections import Counter
n =int(input())
s = list(str(input()))

    
freq = Counter(s)
cnt0 = freq["z"]
cnt1 = freq["n"]
for i in range(cnt1):
    print(1,end=" ")
for i in range(cnt0):
    print(0,end=" ")
