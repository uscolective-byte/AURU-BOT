from aura.normalizer import AURANormalizer
from core.trinity_core import TrinityCore

def main():
    trinity = TrinityCore()
    normalizer = AURANormalizer()

    print("=== TRINITY SYSTEM ONLINE ===")
    print("Zadajte príkaz (napíšte 'koniec' pre ukončenie):")

    while True:
        try:
            user_input = input("\nAURA > ")
            if user_input.lower() in ["koniec", "exit", "quit"]:
                print("Ukončujem systém TRINITY. Dovidenia.")
                break

            if not user_input.strip():
                continue

            # Krok 1: AURA spracuje a normalizuje vstup
            normalized_command = normalizer.process_input(user_input)

            # Krok 2: Odoslanie do TRINITY CORE
            response = trinity.receive_command(normalized_command)

            # Krok 3: AURA zobrazí výsledok používateľovi
            print(response)

        except KeyboardInterrupt:
            print("\nNúdzové odpojenie systému.")
            break

if __name__ == "__main__":
    main()
