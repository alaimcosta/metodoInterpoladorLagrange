
from sys import float_repr_style
import numpy as np
import matplotlib.pyplot as plt

def interpLagrange(xPonto,x,y,n): #xPonto ponto a ser avaliado
  yPonto = 0
  for k in range(0,n+1): #a loop for vai de 0 até n+1
    p = 1
    for j in range(0,n+1):
      if k != j:
        p = p*(xPonto - x[j])/(x[k] - x[j])

    yPonto = yPonto + p * y[k]

  return yPonto

#Pontos da interpolação
x = [0, 0.2, 0.4, 0.5]
y = [0, 2.008, 4.064, 5.125]

#x = [0, 3, 7, 10]
#y = [0, 5, 9, 11]

n  = 2 #grau da interpolação

xPonto = float(input("Entre com um ponto a ser avaliado: "))
yPonto = interpLagrange(xPonto,x,y,n) #Ponto yPonto desejo encontrar, dados um xPonto
t  = np.arange(-2.0,2.0,0.1) #cria o gráfico
yt = []

for i in t:
  yt.append(interpLagrange(i,x,y,n)) #adiciono o ponto encontrado na lista


print("Ponto y encontrado: ", yPonto)

plt.plot(t,yt,'b-', label='Reta da interpolação')
plt.plot(x,y,'ro', label='Pontos conhecidos')
plt.plot(xPonto,yPonto,'g*', label='Ponto avaliado')
plt.legend()
plt.show()
