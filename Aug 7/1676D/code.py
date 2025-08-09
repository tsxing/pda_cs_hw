
t = int(input())

for _ in range(t):
    board = []
    n, m = map(int, input().split())
    for _ in range(n):
        line = [int(x) for x in input().split()]
        board.append(line)

    main_diag = [0] * (n+m-1)  
    anti_diag = [0] * (n+m-1) 

    for i in range(n):
        for j in range(m):
            main_diag[i-j + m-1] += board[i][j]
            anti_diag[i+j] += board[i][j]

    best_sum = 0
    for i in range(n):
        for j in range(m):
            total = main_diag[i-j + m-1] + anti_diag[i + j] - board[i][j]
            if total > best_sum:
                best_sum = total

    print(best_sum)
