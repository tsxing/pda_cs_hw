t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    b = s.count('B')
    if b == k:
        print(0)
    else:
        if b<k:
            c="A"
        else:
            c = "B"
        cnt = abs(k - b)
        ind = 0

        for i in range(len(s)):
            if s[i] == c:
                cnt -= 1
                if cnt == 0:
                    ind = i
                    break

        print(1)
        if c=="A":
            print(ind+1, "B")
        else:
            print(ind+1,"A")
