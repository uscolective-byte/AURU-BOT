class SecurityChecker:
    @staticmethod
    def verify(command: str) -> bool:
        # Základná bezpečnostná kontrola (napr. blokovanie nebezpečných výrazov)
        forbidden_keywords = ["rm -rf", "drop database", "format"]
        for word in forbidden_keywords:
            if word in command.lower():
                return False
        return True
