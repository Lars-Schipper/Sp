import psycopg2

c = psycopg2.connect("dbname=postgres user=postgres password=3621") #TODO: edit this.
cur = c.cursor()

cur.execute("DROP TABLE IF EXISTS products CASCADE")
cur.execute("DROP TABLE IF EXISTS profiles CASCADE")
cur.execute("DROP TABLE IF EXISTS profiles_previously_viewed CASCADE")
cur.execute("DROP TABLE IF EXISTS sessions CASCADE")
cur.execute("DROP TABLE IF EXISTS lijkt_op CASCADE")
cur.execute("DROP TABLE IF EXISTS populaire_producten CASCADE")

# All product-related tables

cur.execute("""CREATE TABLE products
                (id VARCHAR PRIMARY KEY,
                 name VARCHAR,
                 brand VARCHAR,
                 type VARCHAR,
                 category VARCHAR,
                 subcategory VARCHAR,
                 subsubcategory VARCHAR,
                 targetaudience VARCHAR,
                 msrp INTEGER,
                 discount INTEGER,
                 sellingprice INTEGER,
                 deal VARCHAR,
                 description VARCHAR);""")

# All profile-related tables

cur.execute("""CREATE TABLE profiles
                (id VARCHAR PRIMARY KEY,
                 latestactivity TIMESTAMP,
                 segment VARCHAR);""")

cur.execute("""CREATE TABLE profiles_previously_viewed
                (profid VARCHAR,
                 prodid VARCHAR,
                 FOREIGN KEY (profid) REFERENCES profiles (id),
                 FOREIGN KEY (prodid) REFERENCES products (id));""")

# All session-related tables

cur.execute("""CREATE TYPE d_type AS ENUM ('mobile', 'tablet', 'pc', 'other');""")
cur.execute("""CREATE TABLE sessions
                (id VARCHAR PRIMARY KEY,
                 profid VARCHAR,
                 segment VARCHAR,
                 sale BOOLEAN,
                 starttime TIMESTAMP,
                 endtime TIMESTAMP,
                 duration INTEGER,
                 os VARCHAR,
                 devicefamily VARCHAR,
                 devicetype d_type,
                 FOREIGN KEY (profid) REFERENCES profiles (id));""")

cur.execute("""CREATE TABLE lijkt_op
                (prodID VARCHAR,
                 product_1 VARCHAR,
                 product_2 VARCHAR,
                 product_3 VARCHAR,
                 FOREIGN KEY (prodID) REFERENCES products(id)); """)

cur.execute("""CREATE TABLE populaire_producten
                (prodID VARCHAR,
                 product_1 VARCHAR,
                 product_2 VARCHAR,
                 product_3 VARCHAR,
                 product_4 VARCHAR,
                 product_5 VARCHAR,
                 FOREIGN KEY (prodID) REFERENCES products(id)); """)

c.commit()
cur.close()
c.close()