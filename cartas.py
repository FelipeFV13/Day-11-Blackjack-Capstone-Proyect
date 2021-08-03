from random import choice
carts=["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

c_user=[]

for i in range(2):
    c_user.append(choice(carts))
suma_cart=0

for i in c_user:
    suma_cart += i

def more_card(c_user,suma_cart):
    if suma_cart <=10 :
        c_user.append(choice(carts))
        suma_cart=0

        for j in c_user:
            if j == "J" or j == "Q" or j == "K":
                j = 10
            elif j == "As":
                j = 11
            suma_cart += j
        return suma_cart

    elif suma_cart < 21:
        c_user.append(choice(carts))
        suma_cart=0
        for j in c_user:
            if j == "J" or j == "Q" or j == "K":
                j = 10
            elif j == "As":
                j = 1
            suma_cart += j
            return suma_cart

more_card(c_user,suma_cart)