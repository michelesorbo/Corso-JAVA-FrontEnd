x = 3
global nome
nome = "Michele"
# x += 1
# print(x)

def esempio():
    y = 4 #y è visibile solo nella funzione esempio()
    x = 5 #Questa x non è quella dichiarata sopra ma è una x visibile solo nella funzione
    print(nome)

print(f"x prima della funzione 2 {x}")
esempio()

def esempio2():
    global x #Faccio riferimento alla x fuori dalla funzione
    x += 2

esempio2()

print(f"x dopo la funzione 2 {x}")


n1 = 3
n2 = 5

def somma(a,b):
    return a + b

somma(3,9) # somma(a = 2, b = 9)
somma(n1,n2) # somma(a = n1, b = n2)=> somma(a = 3, b = 5)