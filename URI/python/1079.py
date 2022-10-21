#1079

num_entrada = int(input())
lista_media = []


for i in range(num_entrada):
  valores = input().split()
  media = (((float(valores[0]) * 2) + (float(valores[1]) * 3) + (float(valores[2]) * 5)) / 10)
  lista_media.append(media)

for i in range(len(lista_media)):
  print(f"{lista_media[i]:.1f}")
