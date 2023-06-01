rut=input("ingresa tu rut: ")
multiplicadores=[2,3,4,5,6,7]
def calculardv(lista,multi):
    suma=[]
    indice=0
    res=0
    for num in lista:
        multiplicador = multi[indice%len(multi)]
        suma.append(int(num)*multiplicador)
        indice+=1

    for i in suma:
        res+=i
    resto=res//11
    valor=resto*11
    valor_Abs=res-valor
    valor_Abs-=11
    valor_final=abs(valor_Abs)
    
    if valor_final==10:
        valor_final='K'
    elif valor_final==11:
        valor_final=0

    return valor_final

lrut=list(rut)
lrut.reverse()

print(calculardv(lrut,multiplicadores))

     




