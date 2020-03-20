import psycopg2
import csv

c = psycopg2.connect("dbname=postgres user=postgres password=3621")  #TODO: edit this.
cur = c.cursor()

select = "select * from products"
cur. execute(select)
producten = cur.fetchall()

with open('lijkt_op.csv', 'w', newline='') as f:
   fieldnames = ['ID', 'brand', 'type']
   thewriter = csv.DictWriter(f, fieldnames= fieldnames)

   thewriter.writeheader()
   for rij in producten:
       if rij[0] == None or rij[2] == None or rij[3] == None:
           continue
       thewriter.writerow({'ID' : rij[0], 'brand' : rij[2], 'type' : rij[3]})


cur.close()
c.close()
f.close()

