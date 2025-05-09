la = float(input("largura: "))
comp = float(input("comprimento: "))
def Area(la, comp):
    print("Controle de terrenos")
    print("-" * 30)
    s = la * comp
    print("A área de um terreno", la, "*", comp, "é de", s)

Area(la, comp)