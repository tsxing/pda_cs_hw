t = int(input())
for _ in range(t):
    n = int(input())
    s = list(str(input()))
    log = []
    for i in range(n-1):
        log.append(s[i]+ s[i+1])
        
    print(len(set(log)))
        
    
    
