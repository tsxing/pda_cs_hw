
n = int(input())
c = list(map(int, input().split()))

c.sort(reverse=True)
best_rev = -1
best_p = 0

for i, p in enumerate(c):
    rev = p*(i + 1)
    if rev > best_rev or (rev == best_rev and p < best_p):
        best_rev= rev
        best_p= p

print(best_rev, best_p)
