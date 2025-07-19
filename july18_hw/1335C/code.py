from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)

    distinct = len(freq)
    max_freq = max(freq.values())

    if distinct == max_freq:
        print(distinct - 1)
    else:
        print(min(distinct, max_freq))
