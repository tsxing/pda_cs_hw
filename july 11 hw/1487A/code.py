t = int(input())
for _ in range(t):
    ans = int(input())
    a =[int(x) for x in input().split()]
    s = min(a)
    for i in a:
        if i==s:
            ans-=1;
    print(ans)





#you just need to find the amt of non-mininum numbers
