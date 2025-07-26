
N, S = map(int, input().split())
log = []
for _ in range(N):
    a, b= map(int, input().split())
    log.append([a,b])

line = [False]*N
curr_pos = S-1
curr_dir = 1
curr_pow = 1
next_pos = curr_pos + curr_dir *curr_pow

while (0<=next_pos<=N and 0<=curr_pos<=N):
    if log[curr_pos][0]==0: # jumpad

        curr_pow += log[curr_pos][1]
        curr_dir *= -1;
    elif log[curr_pos][0]==1: #target
     
        if log[curr_pos][1]<=curr_pow and line[curr_pos] == False: #  break it
            line[curr_pos] = True
    curr_pos = curr_pos + curr_dir *curr_pow    


print(line.count(True))
