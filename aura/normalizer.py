class AURANormalizer:
    @staticmethod
    def process_input(raw_input: str) -> str:
        # Odstránenie prebytočných medzier a úprava na štandardný reťazec
        cleaned = " ".join(raw_input.strip().split())
        return cleaned
