number = float(input())
percentual = 0
if number >= 0 and number <= 400.00:
    percentual = 15
elif number > 400.00 and number <= 800.00:
    percentual = 12
elif number > 800.00 and number <= 1200.00:
    percentual = 10
elif number > 1200.00 and number <= 2000.00:
    percentual = 7
else:
    percentual = 4
    
reajuste = percentual*number/100

print("Novo salario: {:.2f}".format(number+reajuste))
print("Reajuste ganho: {:.2f}".format(reajuste)) 
print("Em percentual: "+str(percentual)+" %")  
