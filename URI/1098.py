txt = []
for i in range(0, 21, 2):
    el = 'I='
    if (i > 0): el += str(i/10).rstrip("0").rstrip(".") + ' '
    else:       el += '0 '
    for j in range(1,4):
        elj = el + 'J='
        if (j > 0): elj += str(i/10 + j).rstrip("0").rstrip(".")
        else:       elj += '0'
        txt.append(elj)

for ln in txt:
    print(ln)
