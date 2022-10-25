entrada = int(input())

horas = entrada//3600
minutos = (entrada - (horas*3600)) // 60
segundos = entrada % 60

print("{}:{}:{}".format(horas, minutos, segundos))
