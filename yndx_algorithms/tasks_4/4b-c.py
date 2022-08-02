dct = {}
with open('input.txt', 'r') as text:
    for line in text:
        arr = line.split()
        for word in arr:
            if not dct.get(word):
                dct[word] = 1
            dct[word] += 1

wordlist = []

for k, v in dct.items():
    wordlist.append((v, k))

wlsort = sorted(wordlist, key=lambda x: (-x[0], x[1]))

for cnt, word in wlsort:
    print(word)