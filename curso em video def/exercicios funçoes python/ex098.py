def separar(alinea):
    print("-" * 30)
    print(alinea)
    print("-" * 30)

separar("alínea (a)")

print("Contagem de 1 até 10 de 1 em 1")

def contador(inicio, fim, passo):
    print(inicio, end = " ")
    while inicio < 10:
        inicio += 1
        print(inicio, end = " ")
    print("Fim!")


contador(1,10,1)

separar("alínea (b)")

print("Contagem de 10 até 0 de 2 em 2")

def contador(inicio, fim, passo):
    print(inicio, end = " ")
    while inicio > 0:
        inicio -= 2
        print(inicio, end = " ")
    print("Fim!")


contador(10,0,2)

separar("alínea (c)")

inicio = int(input("inicio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))

print("Contagem de", inicio, "até", fim, "de", passo, "em", passo)

def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1

        if inicio < fim:
                print(inicio, end = " ")
                while inicio < fim:
                    inicio += passo
                    print(inicio, end = " ")
                print("Fim!")


        elif inicio > fim:
                print(inicio, end = " ")
                while inicio > fim:
                    inicio -= passo
                    print(inicio, end = " ")
                print("Fim!")



    if passo != 0:
        if passo > 0:
            if inicio < fim:
                    print(inicio, end = " ")
                    while inicio < fim:
                        inicio += passo
                        print(inicio, end = " ")
                    print("Fim!")


            elif inicio > fim:
                    print(inicio, end = " ")
                    while inicio > fim:
                        inicio -= passo
                        print(inicio, end = " ")
                    print("Fim!")
        elif passo < 0:

            passo = abs(passo)

            if inicio < fim:
                    print(inicio, end = " ")
                    while inicio < fim:
                        inicio += passo
                        print(inicio, end = " ")
                    print("Fim!")


            elif inicio > fim:
                    print(inicio, end = " ")
                    while inicio > fim:
                        inicio -= passo
                        print(inicio, end = " ")
                    print("Fim!")

  
contador(inicio, fim, passo)

print("-" * 30)
print("Fim do exercício!")
print("-" * 30)