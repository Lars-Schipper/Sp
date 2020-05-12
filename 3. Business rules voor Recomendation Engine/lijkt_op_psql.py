import psycopg2
import csv

c = psycopg2.connect("dbname=postgres user=postgres password=3621")
cur = c.cursor()

with open('lijkt_op.csv') as file:
    csv_reader = csv.reader(file, delimiter= ',')
    counter = 0
    lijst = []
    lijst_tijdelijk = []
    lijst_vergelijkbaren_producten = []
    for line in csv_reader:
        if counter != 0:
            lijst.append(line)
        counter += 1

    print(len(lijst))
    print(lijst)
    new_dict = dict({})
    for element in lijst:
        Merk = element[1]
        catagorie = element[2]


        for product in lijst:
            if product[1] == element[1]:
                new_dict.update({element[0]: product[0]})


    print(new_dict)

    # i = 0
    # for element in lijst:
    #     print(element)
    #     lijst_vergelijkbaren_producten.append(element)
    #     for teller in range(0, 10):
    #
    #         if lijst[teller][1] == element[1] and lijst[teller][2] == element[2]:
    #             if len(lijst_vergelijkbaren_producten) < 4 and lijst[teller] != element:
    #                 lijst_vergelijkbaren_producten.append(lijst[teller])
    #     print(lijst_vergelijkbaren_producten)
    #     i += 1



cur.close()
c.close()
file.close()
