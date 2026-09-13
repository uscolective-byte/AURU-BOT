from core.security import SecurityChecker
from core.config import ConfigManager
from modules.system_module import SystemModule

class TrinityCore:
    def __init__(self):
        self.security = SecurityChecker()
        self.config = ConfigManager()  # Inicializácia konfiguračného manažéra
        self.modules = []
        
        # Automatická registrácia modulov
        self.register_modules()

    def register_modules(self):
        self.modules.append(SystemModule())
        print(f"[TRINITY CORE] Úspešne zaregistrovaných modulov: {len(self.modules)}")

    def receive_command(self, command: str):
        print(f"[TRINITY CORE] Prijatý príkaz: {command}")
        
        # 1. Kontrola bezpečnosti
        if not self.security.verify(command):
            return "Chyba: Príkaz bol zablokovaný bezpečnostným protokolom TRINITY."

        # Špeciálny interný príkaz na kontrolu stavu kľúčov/konfigu (bezpečná ukážka)
        if "konfig" in command.lower() or "kluce" in command.lower():
            version = self.config.get("VERSION")
            name = self.config.get("TRINITY_NAME")
            has_gemini = "Nastavený" if self.config.get("API_KEY_GEMINI") else "Chýba"
            return f"TRINITY CORE [Config]: Systém '{name}' (v.{version}). Stav API kľúča Gemini: {has_gemini}."

        # 2. Smerovanie na moduly
        for module in self.modules:
            if module.can_handle(command):
                return module.execute(command)

        # 3. Fallback
        if "ahoj" in command.lower():
            return "TRINITY CORE: Zdravím vás. Systémy sú plne funkčné."
        
        return f"TRINITY CORE: Príkaz '{command}' bol prijatý, ale žiadny aktívny modul nenašiel zhodu."
        return f"TRINITY CORE: Príkaz '{command}' bol prijatý, ale žiadny aktívny modul nenašiel zhodu."
