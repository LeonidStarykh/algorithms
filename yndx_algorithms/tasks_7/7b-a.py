def lineshading(n):
    events = []
    for i in range(n):
        first, last = map(int, input().split())
        events.append((first, -1))
        events.append((last, 1))
    events.sort()
    nowlines = 0
    flag = False
    no_line = 0
    for i in range(len(events)):
        if nowlines == 0 and flag:
            no_line += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            nowlines += 1
            flag = True
        else:
            nowlines -= 1
    return events[-1][0] - events[0][0] - no_line

N = int(input())
print(lineshading(N))