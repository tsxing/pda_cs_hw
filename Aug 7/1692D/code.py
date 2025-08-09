t = int(input())
for _ in range(t):
    s, x = input().split()
    x = int(x)
    s = str(s)
    
    def is_pal(total_minutes):
        h = total_minutes // 60
        m = total_minutes % 60
        time_str = f"{h:02d}:{m:02d}"
        return time_str == time_str[::-1]
    
    hh = int(s[:2])
    mm = int(s[3:])
    start = hh * 60 + mm
    
    seen_minutes = set()
    seen_pals = set()
    cur = start
    
    while cur not in seen_minutes:
        seen_minutes.add(cur)
        if is_pal(cur):
            seen_pals.add(cur)
        cur = (cur + x) % 1440
    
    print(len(seen_pals))



