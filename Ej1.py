import time
import os 

file = open("entrada.txt","r")
maxima = int(file.readline().strip())
print(maxima)
nitems = int(file.readline().strip())
v = [0 for x in range(nitems)]
w = [0 for x in range(nitems)]
for i in range(nitems):
    w[i], v[i] = [int(x) for x in file.readline().split()]

global pesoMax, valMax
pesoMax = 0
valMax = 0

def FBMochila(n, peso, val):
    global pesoMax, valMax
    if n < nitems:
        FBMochila(n+1, peso+w[n], val+v[n])
        FBMochila(n+1, peso, val)
    if val>valMax and peso < maxima:
        valMax = val
        pesoMax = peso

start= time.time()
FBMochila(0,0,0)
print(pesoMax,valMax)

file2 = open("salida.txt","w")
file2.write("El peso es de: " + str(pesoMax) + " kg"+os.linesep)
file2.write("El valor es de: " + str(valMax) + " soles"+os.linesep)

file2.close()

end = time.time()

print("tiempo: ", end-start," segundos")
