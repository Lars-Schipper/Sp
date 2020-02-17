import func




# main_loop ===============================================
while True:
    wie_raad = input('wil je dat de computer raad?(y/n/q)')

    # ===================================================== de computer raad
    if wie_raad == 'y' or wie_raad == 'ja':
        i = 0
        secret = func.input_secret()
        while True:
            i += 1
            gok = func.gok_generator()
            print(i , gok)
            check = func.check(secret, gok)
            zwart = check[0]
            wit = check[1]

            if zwart == 4:
                print('\n\n\n\n\n\n\nGefeliciteerd de computer heeft je code gerade in:', i, 'beurt(en)\n')
                break

    # ====================================================== speler raad
    elif wie_raad == 'n' or wie_raad == 'nee' or wie_raad == 'ik':

        secret = func.secret_generator()
        print('de computer heeft een code in gedachte probeer deze te raden:')
        i = 0

        while True:
            i += 1
            check = func.check(secret, func.input_gok())
            zwart = check[0]
            wit = check[1]
            print('zwart = {}, wit = {}'. format(zwart, wit))

            if zwart == 4:
                print('\n\n\n\n\n\n\n\nGefeliciteerd je hebt gewonnen in:', i, 'beurt(en)\n')
                break

    #======================================================== programma word afgesloten
    elif wie_raad == 'q' or wie_raad == 'quit' or wie_raad == 'exit':
        print('bedankt voor het spelen')
        break

    # ======================================================= test
    elif wie_raad == 't':
        algoritme_kueze = input('welk algoritme wil je gebruiken(1,2 of 3): ')

        if algoritme_kueze == '1':
            secret = func.input_secret()
            if func.algoritme_1(secret) == True:
                print('hij werkt eindelijk')
            else:
                print('hij doet nogsteeds niks')

        elif algoritme_kueze == '2':
            secret = func.input_secret()
            print(func.algoritme_2(secret))