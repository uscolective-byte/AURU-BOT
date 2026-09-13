import datetime
from modules.base_module import BaseModule

class SystemModule(BaseModule):
    def __init__(self):
        super().__init__()
        self.name = "SystemModule"

    def can_handle(self, command: str) -> bool:
        keywords = ["čas", "datum", "dátum", "info", "system"]
        return any(keyword in command.lower() for keyword in keywords)

    def execute(self, command: str) -> str:
        cmd = command.lower()
        if "čas" in cmd or "čas" in cmd:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            return f"TRINITY [SystemModule]: Aktuálny čas je {current_time}."
        elif "dátum" in cmd or "datum" in cmd:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            return f"TRINITY [SystemModule]: Dnešný dátum je {current_date}."
        
        return f"TRINITY [SystemModule]: Systémové informácie sú v poriadku."
