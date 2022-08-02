def customs(n):
    events = []
    for i in range(n):
        first, last = map(int, input().split())
        events.append((first, 1))
        events.append((first + last, -1))
    events.sort()
    app_cnt = 0
    max_cnt = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            app_cnt -= 1
        else:
            app_cnt += 1
            if app_cnt > max_cnt:
                max_cnt = app_cnt
    return max_cnt

N = int(input())
print(customs(N))