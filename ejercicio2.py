# 2. Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

numeroescrito = int(input("digite numero: "))

def ultimo_numero(numeroescrito):
    ultimos2 = numeroescrito%100
    ultimo = ultimos2%10
    if (ultimo==4):
        print("el ultimo numero es 4")
    else:
        print("el ultimo numero no es 4")

numeromulti = ultimo_numero(numeroescrito)
