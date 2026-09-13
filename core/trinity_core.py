from core.security import SecurityChecker
from core.config import ConfigManager
from modules.system_module import SystemModule
from modules.ai_module import AIModule

class TrinityCore:
    def __init__(self):
        self.security = SecurityChecker()
        self.config = ConfigManager()  # Načítanie konfigurácie a kľúčov
        self.modules = []
        
        # Automatická registrácia modulov
        self.register_modules()

    def register_modules(self):
        # Špecifické moduly idú na začiatok
        self.modules.append(SystemModule())
        
        # AI modul sa registruje s prístupom ku konfigurácii kvôli API kľúču
        ai_mod = AIModule(self.config)
        self.modules.append(ai_mod)
        
        print(f"[TRINITY CORE] Úspešne zaregistrovaných modulov: {len(self.modules)}")

    def receive_command(self, command: str):
        print(f"[TRINITY CORE] Prijatý príkaz: {command}")
        
        # 1. Kontrola bezpečnosti
        if not self.security.verify(command):
            return "Chyba: Príkaz bol zablokovaný bezpečnostným protokolom TRINITY."

        # Interný príkaz na kontrolu konfigurácie
        if "konfig" in command.lower() or "kluce" in command.lower():
            version = self.config.get("VERSION")
            name = self.config.get("TRINITY_NAME")
            has_gemini = "Nastavený" if self.config.get("API_KEY_GEMINI") and self.config.get("API_KEY_GEMINI") != "tu_zadajte_svoj_kluc" else "Chýba"
            return f"TRINITY CORE [Config]: Systém '{name}' (v.{version}). Stav API kľúča Gemini: {has_gemini}."

        # 2. Smerovanie na moduly (prvý, ktorý dokáže príkaz obslúžiť, ho vykona)
        for module in self.modules:
            if module.can_handle(command):
                # Ak narazíme na SystemModule, skontrolujeme či vie príkaz spracovať
                if module.name == "SystemModule":
                    if module.can_handle(command):
                        return module.execute(command)
                else:
                    # Pre AIModule (ktorý vracia True pre can_handle) ho použijeme ako inteligentný fallback
                    return module.execute(command)

        return f"TRINITY CORE: Príkaz '{command}' nemohol byť spracovaný."
