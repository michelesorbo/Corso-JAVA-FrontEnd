#x = 5
# print(x)

# print("Altro codice importante")

#x = 5



try:
    x = 'a'
    print(int(x))
except NameError:
    print("La variabile non è stata dichiarata")
except ValueError:
    print("Cast non riuscito")
except:
    print("Errore Generico")

print("Altro codice importante")


def dividi(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        result = "Errore hai diviso per 0"
    return result

print(dividi(8,0))

try:
    #x = 45
    print(x)
except NameError:
    print("Errore generale")
finally:
    print("sono finally e sono sempre eseguito")

