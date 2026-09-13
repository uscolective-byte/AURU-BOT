from core.security import SecurityChecker

class TrinityCore:
    def __init__(self):
        self.security = SecurityChecker()

    def receive_command(self, command: str):
        print(f"[TRINITY CORE] Prijatý príkaz: {command}")
        
        # 1. Kontrola bezpečnosti
        if not self.security.verify(command):
            return "Chyba: Príkaz bol zablokovaný bezpečnostným protokolom TRINITY."

        # 2. Analýza a smerovanie (tu neskôr pribudne logika pre jednotlivé moduly)
        response = self._route_command(command)
        return response

    def _route_command(self, command: str) -> str:
        # Jednoduché smerovanie na základe kľúčových slov
        if "ahoj" in command.lower():
            return "TRINITY CORE: Zdravím vás. Systémy sú plne funkčné."
        elif "stav" in command.lower():
            return "TRINITY CORE: Všetky moduly sú v pohotovosti."
        else:
            return f"TRINITY CORE: Príkaz '{command}' bol úspešne spracovaný, ale zatiaľ nemá priradený špecifický modul."
