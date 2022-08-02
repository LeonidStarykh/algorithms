n = int(input())
theme_cnt = {}
mess_theme = {}
max_val = 1

for i in range(n):
    mess = int(input())
    if mess == 0:
        theme = input()
        input()                                   # no use
        theme_cnt[theme] = 1
        mess_theme[i+1] = theme

    else:
        input()                                   # no use
        find_theme = mess_theme[mess]
        mess_theme[i+1] = find_theme
        theme_cnt[find_theme] += 1
        if theme_cnt[find_theme] > max_val:
            max_val = theme_cnt[find_theme]

for k,v in theme_cnt.items():
    if v == max_val:
        print(k)
        break