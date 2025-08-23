t = int(input())

def get_divisors(total):
    divisors = []
    for i in range(1, int(total**0.5) + 1):
        if total % i == 0:
            divisors.append(i)
            if i != total // i:  
                divisors.append(total // i)
    return sorted(divisors)


def solve(a):
    # if all elements are same then print 0
    if len(set(a))==1:
        return 0
    tot = sum(a)
    divisors = get_divisors(sum(a))
    ans = 0
    for i in range(len(divisors)):
        target_sum = tot//divisors[i]
        curr_sum=0
        cnt =0
        for j in range(len(a)):
            curr_sum+= a[j]
            if curr_sum == target_sum:
                cnt+=1
                curr_sum=0
            if curr_sum > target_sum:
                break
        if cnt ==divisors[i]:
            ans = max(ans,cnt)
    return len(a)-ans
                
            
    
    
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(a))
    
