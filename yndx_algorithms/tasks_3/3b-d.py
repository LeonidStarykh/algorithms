n = int(input())
poss = set(range(1, n+1))

s = input().strip()

while s != 'HELP':
    nums = set(map(int, s.split()))
    s = input().strip()
    if s == 'YES':
        poss = poss & nums
    if s == 'NO':
        poss = poss - nums
    s = input().strip()

print(*sorted(poss))