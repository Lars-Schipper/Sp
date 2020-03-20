import psycopg2
import csv

c = psycopg2.connect("dbname=postgres user=postgres password=3621")  #TODO: edit this.
cur = c.cursor()

with open('lijkt_op.csv') as file:
    csv_reader = csv.reader(file, delimiter= ',')
    counter = 0
    lijst = []
    lijst_tijdelijk = []
    lijst_voor_vergelijking = []
    for line in csv_reader:
        if counter != 0:
            lijst.append(line)
        counter += 1
    print(lijst)
    print(len(lijst))

    i = 0
    for element in lijst:
        for i in range(0, len(lijst)):
            print(i)
            # if len(lijst_tijdelijk) <= 3:

                # if element[1] == i[1] and element[2] == i[2]:
                #     lijst_voor_vergelijking.append(i)
    print(lijst_voor_vergelijking)

cur.close()
c.close()
file.close()
