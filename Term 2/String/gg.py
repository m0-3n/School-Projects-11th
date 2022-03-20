lst = eval(input('list'))
freq = {}
for i in lst:
    if i in lst:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
