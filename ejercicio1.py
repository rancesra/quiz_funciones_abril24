tabla = 0
numeroescrito = int(input("digite numero: "))
rangotabla = [1,2,3,4,5,6,7,8,9,10]

print("TABLA DEL ",numeroescrito)

def calcular_tabla(numeroescrito):
    for i in rangotabla:
        print(f"{numeroescrito}x{i} = ",numeroescrito*i)
        

numeromulti = calcular_tabla(numeroescrito)


