t = int(input())

for _ in range(t):
    w, h = map(int, input().split()) 
    max_area = 0

    for i in range(4):
        line = input().split()
        points = list(map(int, line[1:]))

        length = points[-1]-points[0] 
        if i < 2: # horizontal base
            area = length * h
        else: #vertical base/ base is on "height"
            area = length * w
        if area > max_area:
            max_area = area

    print(max_area)
