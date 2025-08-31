import sys
sys.stdin = open("breedflip.in", "r")
sys.stdout = open("breedflip.out", "w")

n = int(input())
A = input().strip()
B = input().strip()

count = 0
for i in range(n):
    if A[i] != B[i] and (i == 0 or A[i-1] == B[i-1]):
        count += 1

print(count)
