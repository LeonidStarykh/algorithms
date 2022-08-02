def returnarr(srt=True):
    arr = list(map(int, input().split()))[1:]
    for i in range(len(arr)):
        arr[i] = (arr[i], i)
    if srt:
        arr.sort()
    return arr

s = int(input())
a = returnarr()
b = returnarr()
c = returnarr(False)
c.sort(key=lambda x: (x[0], -x[1]))

flag = False

for aval, apos in a:
    cpos = len(c) - 1
    for bval, bpos in b:
        while cpos >= 0 and (aval + bval + c[cpos][0] > s):
            cpos -= 1
        if (aval + bval + c[cpos][0] == s) and (not flag or (apos, bpos, cpos) < ans):
            ans = apos, bpos, c[cpos][1]
            flag = True

if flag:
    print(*ans)
else:
    print(-1)