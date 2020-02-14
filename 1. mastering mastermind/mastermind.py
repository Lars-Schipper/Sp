import random
import funties



kleur_opties = ['1', '2', '3', '4', '5', '6']   #kleuren opties definiëren

# main_loop ===============================================
while True:
    wie_raad = input('wil je dat de computer raad?(y/n/q)')

    if wie_raad == 'y': # de computer raad
        a = input_secret()
        b = gok_generator()
        i = 0
        while True:
            i += 1
            print(i)

            # if check(a, gok_generator()) == True:  #de computer zelf automatisch laten raden
            #     break

            if check(a, b) == True:
                break
    # ======================================================
    elif wie_raad == 'n':               # ik raad

        secret = secret_generator()
        print(secret)
        while True:
            if check(secret, input_gok()) == True:
                break
    #========================================================
    elif wie_raad == 'q':               # als q wordt ingevoerd eindigt het programma
        print('bedankt voor het spelen')
        break