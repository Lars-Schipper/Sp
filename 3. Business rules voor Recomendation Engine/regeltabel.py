import psycopg2

c = psycopg2.connect("dbname=postgres user=postgres password=3621") #TODO: edit this.
cur = c.cursor()

cur.execute("DROP TABLE IF EXISTS lijkt_op CASCADE")
# cur.execute("DROP TABLE IF EXISTS veel_naar_gekeken CASCADE")

cur.execute("""CREATE TABLE lijkt_op
                (FOREIGN KEY (prodid) REFERENCES products(id),
                 product_1 VARCHAR,
                 product_2 VARCHAR,
                 product_3 VARCHAR); """)


c.commit()
cur.close()
c.close()