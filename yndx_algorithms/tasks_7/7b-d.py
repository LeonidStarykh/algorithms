n, m = map(int, input().split())
a_arr = list(map(int, input().split()))
segs = [(a,0) for a in a_arr]
assert len(a_arr) == n, f'условие нарушено, всего должно быть введено {n} значений'

ans = [0] * m                                                                                              # l, r, cnt_cat

for i in range(m):
    l, r = map(int, input().split())
    segs.append((l, -1, i))
    segs.append((r, 1, i))
segs.sort()

now_cats = 0

for seg in segs:
    if seg[1] == 0:
        now_cats += 1
    if seg[1] == -1:
        ans[seg[2]] = now_cats
    if seg[1] == 1:
        ans[seg[2]] = now_cats - ans[seg[2]]

print(*ans)