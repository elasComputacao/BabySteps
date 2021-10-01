# Questão 1040 em Python

grades = input().split()

n1, n2, n3, n4 = grades

average = (float(n1)*2 + float(n2)*3 + float(n3)*4 + float(n4))/10
print(f'Media: {average:.1f}')

if average >= 7.0:
    print('Aluno aprovado.')
elif average < 5.0:
    print('Aluno reprovado.')
elif 5.0 <= average <= 6.9:
    print('Aluno em exame.')
    exam = float(input())
    print(f'Nota do exame: {exam:.1f}')
    average = (average + exam)/2
    if average >= 5.0:
        print('Aluno aprovado.')
    elif average <= 4.9:
        print('Aluno reprovado.')
    print(f'Media final: {average:.1f}')