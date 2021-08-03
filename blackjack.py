from random import choice

carts = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
tope = 21
saldo = 2000


def continuar():
    question = input("Do you wish to continue, enter (Y/N) :").lower()
    while True:
        if question in "y":
            return True
            break
        elif question in "n":
            return False
            break


def run(saldo):
    print("Bienvenido a mi juego de BlackJack\n")
    start_game = input("Quieres jugar (Y/N): >").lower()

    if start_game == "y":
        print(f"tu saldo es ${saldo}")
        apuesta = input("""Cuanto quieres apostar, escribe:\n1. $10\n2. $100\n3. $500\n4. $1000\n5. $2000: \n """)

        saldo -= saldo_apostar(apuesta)
        print(f"tu saldo es ahora de ${saldo}")

        carts_u = []

        for i in range(2):
            carts_u.append(choice(carts))
        print(f"tus cartas son:\n{carts_u}\n")
        suma_cart_u = 0
        for j in carts_u:
            if j == "J" or j == "Q" or j == "K":
                j = 10
            elif j == "As":
                j = 11
            suma_cart_u += j
        print(f"Tienes un {suma_cart_u}\n")

        croupier = []
        croupier.append(choice(carts))
        carts_croupier = 0
        print(f"El couprier son: {croupier}")
        croupier.append(choice(carts))
        for i in croupier:
            if i == "J" or i == "Q" or i == "K":
                i = 10
            elif i == "As":
                i = 11
            carts_croupier += i

        add_cart = input("Quieres otra carta (Y/N)? ").lower()

        if add_cart == "n":

            if suma_cart_u == tope and suma_cart_u != carts_croupier:
                print(f"Las cartas del couprier son {croupier}")
                print(f"Suman un total de: {carts_croupier}")
                print("Blackjack!!\nYou Won")
                saldo += saldo_apostar(apuesta) * 3
                print(f"Tu saldo es {saldo}")
                return saldo
            elif suma_cart_u > carts_croupier:
                print(f"Las cartas del couprier son {croupier}")
                print(f"Suman un total de: {carts_croupier}")
                print("You won")
                saldo += saldo_apostar(apuesta) * 2
                print(f"Tu saldo es {saldo}")
                return saldo
            elif suma_cart_u < carts_croupier:
                print(f"Las cartas del couprier son {croupier}")
                print(f"Suman un total de: {carts_croupier}")
                print(f"You lose\ntu saldo es de {saldo}")
                return saldo

        elif add_cart == "y":

            saldo = more_card(carts_u, suma_cart_u, croupier, carts_croupier, saldo, apuesta)
            return saldo


def saldo_apostar(apu):
    if apu == "1":
        return 10
    elif apu == "2":
        return 100
    elif apu == "3":
        return 500
    elif apu == "4":
        return 1000
    elif apu == "5":
        return 2000


def more_card(c_user, suma_cart, croupier, carts_croupier, saldo, apuesta):
    if suma_cart <= 10:
        c_user.append(choice(carts))
        suma_cart = 0

        for j in c_user:
            if j == "J" or j == "Q" or j == "K":
                j = 10
            elif j == "As":
                j = 11
            suma_cart += j


    elif suma_cart < 21:
        c_user.append(choice(carts))
        suma_cart = 0

        for j in c_user:
            if j == "J" or j == "Q" or j == "K":
                j = 10
            elif j == "As":
                j = 1
            suma_cart += j

    if suma_cart > tope:
        print(f"tus cartas son {c_user}\n{suma_cart}")
        print(f"You lose\npasaste de {tope}\ntu saldo es de {saldo}")
        return saldo
    elif suma_cart > carts_croupier and suma_cart <= tope:
        print(f"tus cartas son {c_user}\n{suma_cart}")
        print(f"Las cartas del couprier son {croupier}")
        print(f"Suman un total de: {carts_croupier}")
        print("You won")
        saldo += saldo_apostar(apuesta) * 2
        print(f"Tu saldo es {saldo}")
        return saldo
    elif suma_cart < carts_croupier:
        print(f"tus cartas son {c_user}\n{suma_cart}")
        print(f"Las cartas del couprier son {croupier}")
        print(f"Suman un total de: {carts_croupier}")
        print(f"You lose\ntu saldo es de {saldo}")
        return saldo


if __name__ == '__main__':
    saldo = run(saldo)
    while True:
        if saldo > 0:
            if continuar() == False:
                print(f"Your balance is {saldo}")
                break
            else:
                saldo = run(saldo)
        else:
            print("you do not have enough balance to play")
            break
