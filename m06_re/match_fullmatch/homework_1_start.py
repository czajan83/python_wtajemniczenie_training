import re

text = input(f"Podaj adres email:\n")
pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")

try:
    info_parts = pattern.fullmatch(text).groups()
    print(f"Nazwa: {info_parts[0]}")
    print(f"Domena: {info_parts[1]}")
    print(f"Rozszerzenie: {info_parts[2]}")
except AttributeError:
    print(f"Nie wykryto adresu email")


