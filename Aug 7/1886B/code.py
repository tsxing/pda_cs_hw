import math

def dist(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

t = int(input())
for _ in range(t):
    Px, Py = map(int, input().split())
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())

    OA = dist(0, 0, Ax, Ay)
    OB = dist(0, 0, Bx, By)
    PA = dist(Px, Py, Ax, Ay)
    PB = dist(Px, Py, Bx, By)
    AB = dist(Ax, Ay, Bx, By)

    w1 = max(OA, PA)
    w2 = max(OB, PB)
    w3 = max(OA, PB, AB/2)
    w4 = max(OB, PA, AB/2)

    ans = min(w1, w2, w3, w4)
    print(ans)
