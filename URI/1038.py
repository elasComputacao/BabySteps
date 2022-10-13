entrada = input().split()
code = int(entrada[0])
quantidade = float(entrada[1])

if code == 1:
    price = 4.0
elif code == 2:
    price = 4.5
elif code == 3:
    price = 5.0
elif code == 4:
    price = 2.0
elif code == 5:
    price = 1.5
    
print(f'Total: R$ {(price * quantidade):.2f}')