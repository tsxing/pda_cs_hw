from itertools import permutations

N = int(input())
blocks=[]
for _ in range(4):
    b = list(str(input()))
    blocks.append(b)



# usaco
def solve(word,order):
    for i in range(len(order)):
        if word[i] in blocks[order[i]]:

            continue
        else:
            return False
    return True

for _ in range(N):
    word = str(input())
    positions = list(permutations(range(4), len(word)))

    ans = False
    for pos in positions:

        if solve(word,pos):
            ans = True
            print("YES")
            break
    if ans== False:
        print("NO")

    
    
