import random
import csv


class VokabelTrainer:
    def __init__(self):
        self.vokabeln = {}
        self.statistiken = {
            "gesamt_vokabeln": 0,
            "anzahl_abfragen": 0,
            "richtig_beantwortet": 0,
            "falsch_beantwortet": 0,
        }
    def vokabel_hinzufuegen(self):
        print("Sie können mehrere Vokabeln hinzufügen. Geben Sie '0' ein, um das Hinzufügen zu beenden.")
        while True:
            deutsch = input("Deutsches Wort (oder '0' zum Beenden): ").strip()
            if deutsch == '0':
                break
            fremdsprache = input("Wort in der Fremdsprache (z. B. Englisch): ").strip()
            self.vokabeln[deutsch] = fremdsprache
            self.statistiken["gesamt_vokabeln"] = len(self.vokabeln)
            print(f"Die Vokabel {deutsch} - {fremdsprache} wurde hinzugefügt.")
    def vokabeln_speichern(self, datei="vokabeln.csv", stats_datei="statistiken.csv"):
            with open(datei, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                for deutsch, fremdsprache in self.vokabeln.items():
                    writer.writerow([deutsch, fremdsprache])
            with open(stats_datei, mode='w', encoding='utf-8', newline='') as stats_file:
                stats_writer = csv.writer(stats_file)
                stats_writer.writerow([
                    self.statistiken["gesamt_vokabeln"],
                    self.statistiken["anzahl_abfragen"],
                    self.statistiken["richtig_beantwortet"],
                    self.statistiken["falsch_beantwortet"],
                ])
            print(f"Vokabeln wurden in der Datei '{datei}' gespeichert.")

    def vokabeln_laden(self, datei="vokabeln.csv", stats_datei="statistiken.csv"):
            try:
                with open(datei, mode='r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    self.vokabeln = {row[0]: row[1] for row in reader}
                try:
                    with open(stats_datei, mode='r', encoding='utf-8') as stats_file:
                        stats_reader = csv.reader(stats_file)
                        stats = next(stats_reader)
                        self.statistiken["gesamt_vokabeln"] = int(stats[0])
                        self.statistiken["anzahl_abfragen"] = int(stats[1])
                        self.statistiken["richtig_beantwortet"] = int(stats[2])
                        self.statistiken["falsch_beantwortet"] = int(stats[3])
                except FileNotFoundError:
                    print(f"Datei '{stats_datei}' nicht gefunden. Es wurden keine Statistiken geladen.")
                print(f"Vokabeln aus '{datei}' wurden geladen.")
            except FileNotFoundError:
                print(f"Datei '{datei}' nicht gefunden. Es wurden keine Vokabeln geladen.")

    def abfrage_starten(self):
        if not self.vokabeln:
            print("Es sind keine Vokabeln zum Abfragen vorhanden!")
            return

        print("Vokabel-Abfrage gestartet!")
        fremdsprachen_worte = list(self.vokabeln.values())
        random.shuffle(fremdsprachen_worte)
        score = 0
        self.statistiken["anzahl_abfragen"] += 1

        for fremdsprache in fremdsprachen_worte:
            deutsch = [key for key, value in self.vokabeln.items() if value == fremdsprache][0]
            antwort = input(f"Was heißt '{fremdsprache}' auf Deutsch? ").strip()
            if antwort.lower() == deutsch.lower():
                print("Korrekt!")
                score += 1
                self.statistiken["richtig_beantwortet"] += 1
            else:
                print(f"Falsch! Die richtige Antwort ist: {deutsch}")
                self.statistiken["falsch_beantwortet"] += 1


            print(f"Abfrage beendet. Ihr Ergebnis: {score}/{len(self.vokabeln)}")



    def menu(self):
        print("7 - Alle Vokabeln anzeigen")
        while True:
            print("\n--- Vokabeltrainer ---")
            print("1 - Vokabeln hinzufügen")
            print("2 - Vokabeln speichern")
            print("3 - Vokabeln laden")
            print("4 - Vokabel-Abfrage starten")
            print("5 - Statistiken anzeigen")
            print("6 - Beenden")

            wahl = input("Wählen Sie eine Option: ").strip()
            if wahl == "1":
                self.vokabel_hinzufuegen()
            elif wahl == "2":
                self.vokabeln_speichern()
            elif wahl == "3":
                self.vokabeln_laden()
            elif wahl == "4":
                self.abfrage_starten()
            elif wahl == "5":
                self.statistiken_anzeigen()
            elif wahl == "6":
                print("Programm beendet.")
                self.vokabeln_speichern()
                break
            elif wahl == "7":
                self.alle_vokabeln_anzeigen()
            else:
                print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

    def statistiken_anzeigen(self):
        gesamt_abfragen = self.statistiken["anzahl_abfragen"]
        if gesamt_abfragen > 0:
            durchschnitt = (self.statistiken["richtig_beantwortet"] / (self.statistiken["richtig_beantwortet"] + self.statistiken["falsch_beantwortet"])) * 100
        else:
            durchschnitt = 0.0

        print("\n--- Statistiken ---")
        print(f"Gesamtzahl der Vokabeln: {self.statistiken['gesamt_vokabeln']}")
        print(f"Durchgeführte Abfragen: {gesamt_abfragen}")
        print(f"Richtig beantwortete Fragen: {self.statistiken['richtig_beantwortet']}")
        print(f"Falsch beantwortete Fragen: {self.statistiken['falsch_beantwortet']}")
        print(f"Durchschnittlich richtig beantwortet: {durchschnitt:.2f}%")

def alle_vokabeln_anzeigen(self):
        if not self.vokabeln:
            print("Es sind keine Vokabeln gespeichert.")
        else:
            print("\n--- Alle gespeicherten Vokabeln ---")
            for deutsch, fremdsprache in self.vokabeln.items():
                print(f"{deutsch} - {fremdsprache}")

# Programm starten
# Programm starten
if __name__ == "__main__":
    trainer = VokabelTrainer()
    trainer.vokabeln_laden()
    trainer.menu()