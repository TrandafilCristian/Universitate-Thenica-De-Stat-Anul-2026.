import re

# Exercițiul 1: Căutarea unui model într-un text
def verifica_start(text):
    # Folosim r"^Python" pentru a verifica începutul șirului
    pattern = r"^Python"
    if re.match(pattern, text):
        return "Șirul începe cu 'Python'"
    else:
        return "Șirul nu începe cu 'Python'"

# Exercițiul 2: Căutarea unui număr de telefon
def gaseste_telefon(text):
    # Căutăm formatul XXXX-XXX-XXX
    pattern = r"\d{4}-\d{3}-\d{3}"
    result = re.search(pattern, text)
    if result:
        return f"Numărul de telefon găsit: {result.group()}"
    else:
        return "Nu am găsit un număr de telefon."

# Exercițiul 3: Găsirea tuturor cuvintelor care încep cu o literă specifică
def gaseste_cuvinte(text):
    # \ba\w* caută cuvinte care încep cu litera 'a'
    pattern = r"\ba\w*"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches

# Exercițiul 4: Validarea unei adrese de email
def validare_email(email):
    # Verificăm structura local@domeniu.extensie
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return "Adresa de email este validă!"
    else:
        return "Adresa de email nu este validă."

# Exercițiul 5: Înlocuirea unui text
def inlocuire_telefon(text):
    # Înlocuim numărul de telefon cu un text generic
    pattern = r"\d{4}-\d{3}-\d{3}"
    new_text = re.sub(pattern, "[NUMĂR TELEFON]", text)
    return new_text

# Exercițiul 6: Împărțirea unui text în cuvinte
def imparte_text(text):
    # Împărțim textul după unul sau mai multe spații (\s+)
    pattern = r"\s+"
    words = re.split(pattern, text)
    return words

# --- Secțiune de Testare (conform exemplelor din laborator) ---

print("--- Exercițiul 1 ---")
print(verifica_start("Python este un limbaj de programare"))
print(verifica_start("Este Python un limbaj de programare"))

print("\n--- Exercițiul 2 ---")
print(gaseste_telefon("Contactează-ne la 068-555-655 pentru detalii."))
print(gaseste_telefon("Ne poți contacta la 00-00-00-22."))

print("\n--- Exercițiul 3 ---")
print(gaseste_cuvinte("Aceasta este o activitate amuzantă, aleasă de mine."))

print("\n--- Exercițiul 4 ---")
print(validare_email("cazac.cristian@gmail.com"))
print(validare_email("cazac.cristin@gmail.com"))

print("\n--- Exercițiul 5 ---")
print(inlocuire_telefon("Contactează-ne la 079-733-534 pentru detalii."))

print("\n--- Exercițiul 6 ---")
print(imparte_text("Python este un limbaj de programare."))
