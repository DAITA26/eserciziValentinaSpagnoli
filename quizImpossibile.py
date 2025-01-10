### QUIZ IMPOSSIBILE ### 09/01/2025
##dobbiamo fare 3 o 5 domande, ciascuna con 4 opzioni di risposta
##le domande vanno salvate in una tupla
##le opzioni vanno salvate in un dizionario
#per ogni domanda la macchina sceglie a caso una risposta giusta,
#e si salva la risposta in una lista
#per ogni domanda viene richiesto all'utente di scegliere una risposta
#e quella risposta viene salvata in una lista
#per ogni domanda bisogna fare il confronto tra le due risposte comunicando giusto o sbagliato
#alla fine bisogna far vedere il punteggio

import random
domande = ("A che colore sto pensando?", "A quale città sto pensando?",
           "A quale frutto sto pensando?", "A quale animale sto pensando?",
           "A quale professione sto pensando?")
##colore = {"A": "Magenta", "B": "Vinaccia", "C": "Bordeaux", "D": "Cremisi"}
#citta = {"A": "Milano", "B": "Roma", "C": "Bari", "D": "Catania"}
#frutto = {"A": "Mango", "B": "Cocco", "C": "Mela", "D": "Pera"}
#animale = {"A": "Elefante", "B": "Volpe", "C": "Leone", "D": "Tigre"}
#professione = {"A": "Idraulico", "B": "Cameriere", "C": "Manager", "D": "Avvocato"}
opzioni = {
    0: ["A: Magenta", "B: Vinaccia", "C: Bordeaux", "D: Cremisi"],
    1: ["A: Milano", "B: Roma", "C: Bari", "D: Catania"],
    2: ["A: Mango", "B: Cocco", "C: Mela", "D: Pera"],
    3: ["A: Elefante", "B: Volpe", "C: Leone", "D: Tigre"],
    4: ["A: Idraulico", "B: Cameriere", "C: Manager", "D: Avvocato"]
}
risposte_corrette = []
risposte_utente = []
#punteggio iniziale = 0
punteggio = 0

for i, domanda in enumerate(domande):
    print("---------------------------------")
    print(f"Domanda {i + 1}: {domanda}")

    for j, opzione in enumerate(opzioni[i]):
        print(f"{opzione}")

    #risposta casuale del computer
    ris_pc = random.randint(0, 3)
    y = ("A", "B", "C", "D")
    cpu = (y[ris_pc])
    risposte_corrette.append(cpu)
    #print(risposte_corrette)
    ris = input("Inserisci la tua risposta: ").strip().upper()
    if ris == cpu:
        print("BRAVO! Hai indovinato!")
        punteggio += 1
        risposte_utente.append(ris)
    elif ris != "A" and ris != "B" and ris != "C" and ris != "D":
        print("La risposta che hai scelto non è tra le opzioni")
        ris = "-"
        risposte_utente.append(ris)
    else:
        print(f"Sbagliato. La risposta corretta era: {cpu}")
        risposte_utente.append(ris)
print(f"Le risposte corrette erano: {risposte_corrette}")
print(f"Le risposte che hai dato erano: {risposte_utente}")
print(f"Il tuo punteggio è di : {punteggio}")

#calcolo percentuale risposte corrette
def perc():
    print(f"La tua percentuale di vincita è del: {(punteggio/5)*100}")

perc()
