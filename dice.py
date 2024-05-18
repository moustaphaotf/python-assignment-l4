from random import randrange
throws = int(input('Combien de lancés de dés effectuer ? '))

if throws <= 0:
    print('Vous devez fournir un nombre positif !')

else:
    results = [0] * 6
    for i in range(throws):
        dice_value = randrange(1, 7)
        results[dice_value - 1] += 1


    # Print stats
    print(f"Les resultats des lancés sont:")
    for i in range(len(results)):
        result = results[i]
        print(i+1, '--->', round(result / throws * 100, 2), '%')
    