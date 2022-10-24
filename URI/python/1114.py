senha = 2002
num = int(input())
while senha != num:
    print ("Senha Invalida")
    n = int(input())
    if senha == n:
        print ("Acesso Permitido")
        break
if senha == num:
    print ("Acesso Permitido")
