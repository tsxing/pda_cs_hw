# hotelier
N = int(input())
s = list(input()) 
ans = [0] * 10
 
for i in range(N):
    if s[i] == "L":
        ans[ans.index(0)] = 1
    elif s[i] == "R":
        ind = len(ans) - 1 - ans[::-1].index(0)
        ans[ind] = 1
    else:
        ans[int(s[i])] = 0  
 
print("".join(map(str, ans)))
