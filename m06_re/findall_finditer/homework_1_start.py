import re


def print_emails_details(text):
    pattern = re.compile(r"([.|\w]+)@(\w+)((?:\.\w+)+)")
    info_parts = pattern.findall(text)
    for info_part in info_parts:
        print(f"Nazwa: {info_part[0]}")
        print(f"Domena: {info_part[1]}")
        print(f"Rozszerzenie: {info_part[2]}")
        print(20 * f"-")


def print_iter_emails_details(text):
    pattern = re.compile(r"([.|\w]+)@(\w+)((?:\.\w+)+)")
    info_parts = pattern.finditer(text)
    for info_part in info_parts:
        print(f"Pełny adres: {info_part[0]}")
        print(f"Nazwa: {info_part[1]}")
        print(f"Domena: {info_part[2]}")
        print(f"Rozszerzenie: {info_part[3]}")
        print(f"Początkowa pozycja adres w podanym tekście: {info_part.span()[0]}")
        print(f"Końcowa pozycja adres w podanym tekście: {info_part.span()[1]}")
        print(20 * f"---")


def main():
    text = "ale jaja czajosand@o2.pl ale jaja andrzej.b.czajka@gmail.com ale jaja fajne są softest@softest.com.pl"
    print_iter_emails_details(text)


if __name__ == "__main__":
    main()
