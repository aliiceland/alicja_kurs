"""
otworz plik z emailami, odczytaj go, wypisz na ekranie przeczyszczone unikalne emaile
przyjmij nazwe pliku jako paramentr z cmd line - jako parametr w wierszu polecen pythona.
obsluz sytuacje gdy uzytkownik nie poda tej nazwy
obsluz sytuacje gdy podana nazwa jest nazwa nieistniejacego pliku
doloz drugi opcjonalny parametr - plik wynikowy
jesli podamy drugi
"""
import sys 
print(sys.argv)

def clean_email(text):
    text = text.strip().lower()
    if text.count("@") == 1:
        return text

def main(file_name,out_file_name=None):
    cleaned_emails = set()

    with open(file_name) as f:
        for line in f:
            email = clean_email(line)
            if email: 
                cleaned_emails.add(email)
    cleaned_emails = sorted(cleaned_emails)
    cleaned_emails = "\n".join(cleaned_emails)
    if out_file_name:
        with open(out_file_name) as f:
            f.write(cleaned_emails)
    else:
        print(cleaned_emails)
    print("\n".join(cleaned_emails))

#main("../emails.txt")

try: 
    file_name = [sys.argv[1]]
except IndexError:
    print("nie podales nazwy pliku")
    exit()
try:
    out_file_name = [sys.argv[2]]
except IndexError:
    out_file_name = None

try:
    main(file_name,out_file_name)
except FileNotFoundError:
    print("nie ma takiego pliku")


