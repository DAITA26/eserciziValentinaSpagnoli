### Fizz3Buzz5 ###09/01/2025
#stampare i numero ma al posto dei multipli di tre deve stampare Fizz
#e al posto dei multipli di 5 deve stampare Buzz

### VERSIONE SEMPLICE (senza variabili)
'''for n in range(1, (m+1)):
    if ((n % 3) == 0) and ((n % 5) == 0): #oppure if (n % 15) == 0:
        print("Fizz&Buzz")
    elif (n % 3) == 0 :
        print("Fizz")
    elif (n % 5) == 0:
        print("Buzz")
    else:
        print(n)'''

m = int(input("Fino a che numero vuoi giocare?: ").strip()) # m=massimo

def printFizz():
    print("Fizz!")
def printBuzz():
    print("Buzz!")
def printFizzBuzz():
    print("Fizz&Buzz!")
def printNumero(b):
    print(b)
def stampa(parametro):
    print(parametro)

for n in range(1, (m+1)):
    if ((n % 3) == 0) and ((n % 5) == 0): #oppure if (n % 15) == 0:
        stampa("Fizz&Buzz!")
        #printFizzBuzz()
    elif (n % 3) == 0 :
        #printFizz()
        stampa("Fizz!")
    elif (n % 5) == 0:
        #printBuzz()
        stampa("Buzz!")
    else:
        #printNumero(n)
        stampa(n)