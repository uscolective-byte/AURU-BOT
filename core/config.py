import os

class ConfigManager:
    def __init__(self):
        # Základné predvolené hodnoty, ak by .env neexistoval
        self.config_data = {
            "TRINITY_NAME": "TRINITY CORE",
            "VERSION": "1.0.0",
            "MASTER_KEY": "default_key",
            "API_KEY_GEMINI": ""
        }
        self.load_config()

    def load_config(self):
        # Jednoduché čítanie zo súboru .env bez nutnosti externých knižníc
        try:
            if os.path.exists(".env"):
                with open(".env", "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#") and "=" in line:
                            key, value = line.split("=", 1)
                            self.config_data[key.strip()] = value.strip()
                print(f"[ConfigManager] Konfiguračné premenné a kľúče úspešne načítané.")
            else:
                print(f"[ConfigManager] Varovanie: Sbor .env nebol nájdený. Používajú sa predvolené hodnoty.")
        except Exception as e:
            print(f"[ConfigManager] Chyba pri načítavaní konfigurácie: {e}")

    def get(self, key: str, default=None):
        return self.config_data.get(key, default)

    def set(self, key: str, value: str):
        self.config_data[key] = value
        # Tu by sa dala dopísať aj logika pre uloženie späť do .env súboru
