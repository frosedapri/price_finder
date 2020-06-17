import random
from datetime import datetime

YN = input("list ou pas: ")
if YN == "oui":
    list_number = []
    nb = int(input("nombre: "))
    start_time = datetime.now()
    resultat = 1

    print(nb)

    for i in range(1, nb+1):
        list_number.append(i)
    for e in range(len(list_number)):
        resultat *= list_number[e]
    
    


    


    end_time = datetime.now()


    print('Duration: {}'.format(end_time - start_time))

else:

    nb = int(input("nombre: "))
    start_time = datetime.now()
    resultat = 1

    print(nb)

    for i in range(1, nb+1):
        resultat *= i
    
    


    


    end_time = datetime.now()


    print('Duration: {}'.format(end_time - start_time))

