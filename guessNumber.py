### QUINTO ESERICZIO ### 19-12-2024
# GUESS THE NUMBER #

# l'utente deve cercare di indovinare un numero random tra 1 e 100
# se sbaglia il programma deve digli se il numero segreto è più grande o più piccolo del numero_segreto
# comando per importare un numero a caso
import random
numero_segreto = random.randint(1, 100)
#print(numero_segreto)

print("GUESS THE NUMBER")
print("Ciao! Prova ad indovinare il numero segreto")
print("""Puoi scegliere la difficoltà:
FACILE = puoi tentare quante volte vuoi finch non indovini.
MEDIA = hai a disposizione 12 tentativi.
DIFFICILE = hai a disposizione solo 7 tentativi.
""")
diff = input("Inserisci la difficoltà: ").strip().lower()
# print(f"Hai scelto la versione {diff}")
n = input("Inserisci il numero: ")
n_verificato = n.isdigit()
i = 1
if n_verificato == True and diff == "facile":
    while int(n) != numero_segreto:
        print("Sbagliato!")
        if int(n) <= numero_segreto:
            print(f"Il numero segreto è più grande di {n}")
        elif int(n) >= numero_segreto:
            print(f"Il numero segreto è più piccolo di {n}")
        i += 1
        n = int(input("Ritenta. Inserisci un nuovo numero: "))
    print("COMPLIMENTI! HAI INDOVINATO!")
    print(f"Hai impiegato {i} tentativi per indovinare.")
elif n_verificato == True and diff == "media":
    while int(n) != numero_segreto and i <12:
        print("Sbagliato!")
        if int(n) <= numero_segreto:
            print(f"Il numero segreto è più grande di {n}. Hai ancora {12 - i} tentativi.")
        elif int(n) >= numero_segreto:
            print(f"Il numero segreto è più piccolo di {n}. Hai ancora {12 - i} tentativi.")
        elif int(n) == numero_segreto:
            print("COMPLIMENTI! HAI INDOVINATO!")
            print(f"Hai impiegato {i} tentativi per indovinare.")
        i += 1
        n = int(input("Ritenta. Inserisci un nuovo numero: "))
    print("MI DISPAICE! Hai raggiunto il numero massimo di tentativi")
elif n_verificato == True and diff == "difficile":
    while int(n) != numero_segreto and i < 7:
        print("Sbagliato!")
        if int(n) <= numero_segreto:
            print(f"Il numero segreto è più grande di {n}. Hai ancora {7 - i} tentativi.")
        elif int(n) >= numero_segreto:
            print(f"Il numero segreto è più piccolo di {n}. Hai ancora {7 - i} tentativi.")
        elif int(n) == numero_segreto:
            print("COMPLIMENTI! HAI INDOVINATO!")
            print(f"Hai impiegato {i} tentativi per indovinare.")
        i += 1
        n = int(input("Ritenta. Inserisci un nuovo numero: "))
    print("MI DISPIACE! Hai raggiunto il numero massimo di tentativi")
    print(f"Il numero segreto era: {numero_segreto}")
else:
    print("Non è stato inserito correttamente il numero o la difficoltà.")
