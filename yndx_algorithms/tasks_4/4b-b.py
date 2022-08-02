dict = {}
with open('input.txt', 'r') as elec:
    for line in elec:
        pres, value = line.split()
        if dict.get(pres):
            dict[pres] += int(value)
        else:
            dict[pres] = int(value)

sort_dict = sorted(dict.items(), key=lambda x: x[0])
for par in sort_dict:
    print(*par)
