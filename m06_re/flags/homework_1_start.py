import re


def print_com_or_pl_emails_details(text):
    pattern = re.compile(r"([.|\w]+)@(\w+)(.pl|.com)", flags=re.I)
    info_parts = pattern.findall(text)
    for info_part in info_parts:
        print(f"Nazwa: {info_part[0]}")
        print(f"Domena: {info_part[1]}")
        print(f"Rozszerzenie: {info_part[2]}")
        print(20 * f"-")


def main():
    text = "ale jaja czajosand@o2.pl ale jaja andrzej.b.czajka@gmail.CoM ale jaja fajne są softest@softest.acv"
    print_com_or_pl_emails_details(text)


if __name__ == "__main__":
    main()
