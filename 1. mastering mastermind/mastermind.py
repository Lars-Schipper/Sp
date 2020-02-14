import functies




# main_loop ===============================================
while True:
    wie_raad = input('wil je dat de computer raad?(y/n/q)')




    # ===================================================== de computer raad
    if wie_raad == 'y' or wie_raad == 'ja':
        a = functies.input_secret()
        i = 0
        while True:
            i += 1
            print(i)

            # if functies.check(a, gok_generator()) == True:  #de computer zelf automatisch laten raden
            #     break

            if functies.check(a, functies.input_gok()) == True:
                break



    # ====================================================== speler raad
    elif wie_raad == 'n' or wie_raad == 'nee' or wie_raad == 'ik':

        secret = functies.secret_generator()
        print(secret)
        while True:
            if functies.check(secret, functies.input_gok()) == True:
                break



    #======================================================== programma word afgesloten
    elif wie_raad == 'q' or wie_raad == 'quit' or wie_raad == 'exit':
        print('bedankt voor het spelen')
        break