klucz = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}


def encrypt(phrase):
    phrase = phrase.split(sep=" ")          # podziel daną frazę na słowa
    crypt = []                              # utwórz listę dla rezultatów
    for word in phrase:
        cryptword = ""                      # pusty string dla rezultatów
        for letter in word:
            if letter in klucz:             # jeżeli dana litera jest kluczem
                cryptword += klucz[letter]  # dodaj jej wartość do nowego słowa
            else:
                cryptword += letter         # jeśli nie, dodaj do nowego słowa
        crypt.append(cryptword)             # dodaj zaszyfrowane słowo do listy rezultatów
    return " ".join(crypt)          # zwróć listę zaszyfrowanych słów oddzieloną spacją


print(encrypt("To jest mój tekst"))

print(encrypt("Ala ma kota"))

print(encrypt("\nszedł za twym tronem - tuż - blisko,"
              "\npotknął się - krok nieszczęśliwy - "
              "\nupadł i leży chłopisko, "
              "\npijany, a może nieżywy."))
