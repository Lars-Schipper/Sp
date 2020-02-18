import func

# ============================================================================== Main loop
while True:
    wie_raad = input('wil je dat de computer raad?(y/n/q)')

    # =========================================================================== De computer raad
    if wie_raad == 'y' or wie_raad == 'ja':

        while True:

            algoritme_kueze = input('welk algoritme wil je gebruiken(1,2 of 3): ')

            if algoritme_kueze == '1': #========================================= Algoritme 1

                secret = func.input_secret()
                algoritme_1 = func.algoritme_1(secret)[0]

                # print('secret = {}, algo = {}'.format(secret, algoritme_1[0]))

                if algoritme_1[0] == secret:
                    print('jouwn code was:', algoritme_1[0])
                    print('hij werkt eindelijk')
                else:
                    print('hij doet nogsteeds niks')

            elif algoritme_kueze == '2': # ====================================== Algoritme 2
                secret = func.input_secret()
                print(func.algoritme_2(secret))

            elif algoritme_kueze == '3': #======================================= Algoritme 3
                print('algoritme 3')

            elif algoritme_kueze == 'q' or algoritme_kueze == 'quit' or algoritme_kueze == 'exit':
                break

    # =========================================================================== De speler raad
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

    #============================================================================ Programma word afgesloten
    elif wie_raad == 'q' or wie_raad == 'quit' or wie_raad == 'exit':
        print('bedankt voor het spelen')
        break

    # =========================================================================== Test optie
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