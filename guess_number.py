"""Ce programme permet à l'utilisateur de deviner un nombre"""

from random import randrange

min,max = 1, 1000
to_guess = randrange(min, max + 1)
user_guess = 0
tries = 0

print(f"Devinez un nombre entre {min} et {max}: ")
print('-' * 50)
while to_guess != user_guess:

    try:
        user_guess = int(input("Donnez une valeur: "))

        if user_guess > to_guess:
            print('Vous devez saisir un nombre plus petit !')
        elif user_guess < to_guess:
            print("Vous devez saisir un nombre plus grand !")

        tries += 1
    except ValueError:
        print("Vous devez saisir un nombre !")


print('-' * 50, '\n')
print(f"Bravo ! Vous avez trouvé en {tries} essais !")



print()