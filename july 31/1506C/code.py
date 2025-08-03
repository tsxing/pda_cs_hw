t = int(input())

def sol(a, b):
    max_common = 0
    for i in range(len(a)):
        for j in range(len(b)):
            lens = 0 # how long
            while i+lens<len(a) and j+lens<len(b) and a[i+lens] == b[j+lens]:
                lens += 1
                max_common = max(max_common, lens)
    return len(a) + len(b) - 2 * max_common

for _ in range(t):
    a = str(input())
    b = str(input())
    print(sol(a, b))
