#uri 1024

n, lista_msgs = int(input()), []
for x in range(n):
    lista_msgs.append(input())

lista = []
for x in lista_msgs:
    l = []
    for y in x:
        l.append(y)
    lista.append(l)


def func1(q):
    q = list(q)
    for x in q:
        if x.isalpha():
            x = chr(ord(x)+3)
    q = q.reverse()

def func2(q):
    q = list(q)
    if len(q)%2==0:
        x = int(len(q)/2)
    else:
        x = int((len(q)+1)/2)
    for y in range(x, len(q)+1):
        y = chr(ord(y)-1)

def func3(q):
    q = list(q)
    s = ""
    for x in q:
        s = "".join(q)

for x in lista:
    x = func3(func2(func1(x)))
    print(x)