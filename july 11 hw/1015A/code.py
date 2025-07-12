n, m = map(int, input().split())

cnt = 0
log = []
ans = []
    
for _ in range(n):
    l, r = map(int, input().split())
    log.append([l,r])
    
for i in range(1,m+1):
    for j in range(n):
        if (log[j][0] <= i and i<= log[j][1]):
            break
    else:
        cnt+=1
        ans.append(i)
       
print(cnt)
for i in range(len(ans)):
    print(ans[i],end=" ")
    

            
        
    
