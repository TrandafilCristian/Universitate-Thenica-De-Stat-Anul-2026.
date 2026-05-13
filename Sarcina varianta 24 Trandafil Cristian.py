import re

def valideaza_format_card(numar_card):
    # Explicație Pattern:
    # ^          - Începutul șirului
    # \d{4}      - Exact 4 cifre
    # ( \d{4}){3} - Un spațiu urmat de 4 cifre, totul repetat de 3 ori
    # $          - Sfârșitul șirului
    pattern = r"^\d{4} \d{4} \d{4} \d{4}$"
    
    if re.match(pattern, numar_card):
        return True
    else:
        return False

# --- Testare ---
numere_test = [
    "1234 5678 9876 5432",  # Valid
    "1234-5678-9876-5432",  # Invalid (are cratime în loc de spații)
    "1234567898765432",     # Invalid (nu are spații)
    "123A 5678 9876 5432",  # Invalid (conține o literă)
    "1234 5678 9876"        # Invalid (prea scurt)
]

print("Rezultate Verificare Card:")
print("-" * 30)

for card in numere_test:
    rezultat = "VALID" if valideaza_format_card(card) else "INVALID"
    print(f"{card} -> {rezultat}")
