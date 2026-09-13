from abc import ABC, abstractmethod

class BaseModule(ABC):
    def __init__(self):
        self.name = "Base Module"

    @abstractmethod
    def can_handle(self, command: str) -> bool:
        """Určuje, či tento modul dokáže spracovať daný príkaz."""
        pass

    @abstractmethod
    def execute(self, command: str) -> str:
        """Vykoná akciu modulu a vráti výsledok."""
        pass
