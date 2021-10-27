#Deve ser rodado com a versão 3.8 do python ou superior para que funcione a notação de f-string
idade = int(input(''))

anos = idade / 365
meses = (idade % 365) / 30
dias = (idade % 365) % 30

print(f'{int(anos)} ano(s)')
print(f'{int(meses)} mes(es)')
print(f'{int(dias)} dia(s)')
