import os
from google import genai
from modules.base_module import BaseModule

class AIModule(BaseModule):
    def __init__(self, config_manager):
        super().__init__()
        self.name = "AIModule"
        self.config = config_manager
        self.client = None
        self.initialize_client()

    def initialize_client(self):
        api_key = self.config.get("API_KEY_GEMINI")
        if api_key and api_key != "tu_zadajte_svoj_kluc":
            try:
                # Inicializácia oficiálneho GenAI klienta
                self.client = genai.Client(api_key=api_key)
                print(f"[AIModule] Klient pre Gemini bol úspešne inicializovaný.")
            except Exception as e:
                print(f"[AIModule] Chyba pri inicializácii Gemini klienta: {e}")
        else:
            print(f"[AIModule] Varovanie: API kľúč pre Gemini nie je nastavený. AI modul bude offline.")

    def can_handle(self, command: str) -> bool:
        # AI modul bude fungovať ako hlavný spracovateľ pre všetko, 
        # čo nepatrí do špecifických systémových príkazov.
        return True

    def execute(self, command: str) -> str:
        if not self.client:
            return "TRINITY [AIModule]: Nemôžem spracovať požiadavku, pretože chýba platný API kľúč pre Gemini v súbore .env."

        try:
            # Použitie odporúčaného modelu gemini-2.5-flash pre rýchle a efektívne odpovede
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=f"Si pokročilý asistent v rámci systému TRINITY. Odpovedaj vecne, inteligentne a s ohľadom na svoj systémový pôvod. Používateľ píše: {command}"
            )
            return f"TRINITY [AI]: {response.text}"
        except Exception as e:
            return f"TRINITY [AIModule] Chyba pri komunikácii s modelom: {e}"
