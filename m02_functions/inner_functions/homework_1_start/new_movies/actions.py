from .inventory import Inventory
from .user import User

user = User("Andrzej", role="user")


def rent_movie():
    for i in range(0, len(Inventory.INVENTORY)):
        if i not in Inventory.in_rental:
            print(f" film nr {i} - {Inventory.INVENTORY[i]}")
    rental = int(input(f"Wybierz film do wypozyczenia podając numer dostepnej pozycji\n"))
    if rental not in Inventory.in_rental:
        if user.do_movie_rent(Inventory.INVENTORY[rental]):
            Inventory.in_rental.append(rental)
            print(f"Wypozyczyles film {Inventory.INVENTORY[rental]}")
    else:
        print(f"Nie mamy takiego filmu, lub film jest obecnie wypozyczony")
    print(f"Filmy wypozyczone przez uzytkownika {user.name} to {user.rented_movies}")


def view_movie():
    def view_possible():
        return selection <= len(user.rented_movies) and user.rented_movies[selection].views_left > 0

    def do_view():
        if view_possible():
            user.rented_movies[selection].update_views_left()
            return f"Obejrzales film {user.rented_movies[selection]}, " \
                   f"pozostalo jeszcze {user.rented_movies[selection].views_left} dostepnych projekcji tego filmu"
        else:
            return f"Nie wypozyczyles filmu lub przekroczyles limit dopuszczalnych projekcji"

    if len(user.rented_movies) > 0:
        for i in range(0, len(user.rented_movies)):
            print(f"film nr {i} - {user.rented_movies[i]}")
        selection = int(input(f"Wybierz film do obejrzenia od 0 do {len(user.rented_movies) - 1}\n"))
        print(do_view())
        print(do_view())
        print(do_view())
        print(do_view())
    else:
        print(f"Nie wypozyczyles jeszcze zadnego filmu")


def reset_message(text):
    def print_message(text2):
        return text2 + text
    return print_message


def reset_possible_rents():
    if user.role == "administrator" or user.role == "moderator":
        user.available_rents = User.DEFAULT_RENTS
        rst_message = reset_message("success")
    else:
        rst_message = reset_message("brak uprawnien")
    print(rst_message(f"reset mozliwych filmow do wypozyczenia przez uzytkownika {user.name}: "))


def say_hello():
    print(f"Witaj w naszej wypozyczalni {user.name}")


def run():
    say_hello()
    while 1:
        action = input(f"Wybierz dostepna opcje: \n"
                       f"1 - wypozyczyc film \n"
                       f"2 - obejrzec wypozyczony film\n"
                       f"3 - zresetowac ilosc mozliwych filmow do wypozyczenia \n"
                       f"jakakolwek inna - zkonczyc dzialanie programu")
        if action == "1":
            rent_movie()
        elif action == "2":
            view_movie()
        elif action == "3":
            reset_possible_rents()
        else:
            print(f"Do zobaczenia")
            break
