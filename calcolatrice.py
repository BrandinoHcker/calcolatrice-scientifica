import math

def calcolatrice():
    while True:
        print("\n--- SUPER CALCOLATRICE ---")
        print("1. Addizione (+)")
        print("2. Sottrazione (-)")
        print("3. Moltiplicazione (*)")
        print("4. Divisione (/)")
        print("5. Potenza (**)")
        print("6. Radice n-esima (√)")
        print("7. Espressione Libera (es. (2+3)*sqrt(16))")
        print("q. Esci")

        scelta = input("\nInserisci la scelta: ").lower()

        if scelta == 'q':
            print("Chiusura in corso... Arrivederci!")
            break

        try:
            # OPZIONE 7: ESPRESSIONE LIBERA
            if scelta == '7':
                espressione = input("Scrivi l'espressione (usa 'math.sqrt()' per radice): ")
                # math.__dict__ permette di usare funzioni come sqrt, sin, cos direttamente
                risultato = eval(espressione, {"__builtins__": None}, math.__dict__)
                print(f"\n> Risultato: {risultato}")

            # OPZIONE 6: RADICE PERSONALIZZATA
            elif scelta == '6':
                num = float(input("Inserisci il numero (radicando): "))
                indice = float(input("Inserisci l'indice della radice (es. 2 per quadrata): "))
                if num < 0 and indice % 2 == 0:
                    print("Errore: Radice di indice pari non definita per numeri negativi.")
                elif indice == 0:
                    print("Errore: L'indice non può essere zero.")
                else:
                    print(f"\n> Risultato: {num ** (1/indice)}")

            # OPZIONI 1-5: OPERAZIONI STANDARD
            elif scelta in ['1', '2', '3', '4', '5']:
                n1 = float(input("Primo numero: "))
                n2 = float(input("Secondo numero: "))

                if scelta == '1':
                    print(f"\n> Risultato: {n1 + n2}")
                elif scelta == '2':
                    print(f"\n> Risultato: {n1 - n2}")
                elif scelta == '3':
                    print(f"\n> Risultato: {n1 * n2}")
                elif scelta == '4':
                    if n2 != 0:
                        print(f"\n> Risultato: {n1 / n2}")
                    else:
                        print("Errore: Divisione per zero!")
                elif scelta == '5':
                    print(f"\n> Risultato: {n1 ** n2}")
            
            else:
                print("Scelta non valida, riprova.")

        except Exception as e:
            print(f"Errore durante il calcolo: {e}")

# Avvia il programma
calcolatrice()

