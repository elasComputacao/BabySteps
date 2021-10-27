idade = int(input(''))

anos = idade / 365
meses = (idade % 365) / 30
dias = (idade % 365) % 30

print(f'{int(anos)} ano(s)')
print(f'{int(meses)} mes(es)')
print(f'{int(dias)} dia(s)')
