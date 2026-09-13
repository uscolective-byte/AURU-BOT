from core.security import SecurityChecker
from modules.system_module import SystemModule

class TrinityCore:
    def __init__(self):
        self.security = SecurityChecker()
        self.modules = []
        
        # Automatická registrácia modulov
        self.register_modules()

    def register_modules(self):
        # Sem budeme postupne pridávať nové moduly
        self.modules.append(SystemModule())
        print(f"[TRINITY CORE] Úspešne zaregistrovaných modulov: {len(self.modules)}")

    def receive_command(self, command: str):
        print(f"[TRINITY CORE] Prijatý príkaz: {command}")
        
        # 1. Kontrola bezpečnosti
        if not self.security.verify(command):
            return "Chyba: Príkaz bol zablokovaný bezpečnostným protokolom TRINITY."

        # 2. Smerovanie na moduly
        response = self._route_command(command)
        return response

    def _route_command(self, command: str) -> str:
        # Prejdeme všetky zaregistrované moduly a zistíme, ktorý vie príkaz spracovať
        for module in self.modules:
            if module.can_handle(command):
                return module.execute(command)

        # Základná fallback odpoveď, ak žiaden modul príkaz nepoznal
        if "ahoj" in command.lower():
            return "TRINITY CORE: Zdravím vás. Systémy sú plne funkčné."
        
        return f"TRINITY CORE: Príkaz '{command}' bol prijatý, ale žiadny aktívny modul nenašiel zhodu."
