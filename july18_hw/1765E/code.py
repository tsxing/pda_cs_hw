from math import ceil
t = int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    
    if a<=b: 
        print(ceil(n/a))
    else: #getting more silver for selling a gold than it costs to buy back that gold.
        print(1)


        
