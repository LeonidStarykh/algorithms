m = int(input())
wtns = []
for _ in range(m):
    wtns.append(set(input().strip()))

n = int(input())

nums = []
maxcnt = 0
for i in range(n):
    num = input().strip()
    numset = set(num)
    setcnt = 0
    for wtn in wtns:
        if wtn <= numset:
            setcnt += 1
    nums.append((num, setcnt))
    maxcnt = max(maxcnt, setcnt)

ans = []
for num in nums:
    if num[1] == maxcnt:
        ans.append(num[0])
print('\n'.join(ans))