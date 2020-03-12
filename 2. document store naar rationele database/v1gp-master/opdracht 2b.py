    conn = psycopg2.connect("""dbname={} user={} password={}""".format(dbname,username,password))
    return conn

def tableinit(connect):
    """Creates a table in the PostgreSQL database, needs a 'dbsting' that consists of the following:
    'dbname=postgres user=postgres password=geefpasswordop'"""
    cursor = connect.cursor()
    todo = ("DROP TABLE IF EXISTS products",  # Heel belangrijk deze; de functie moet herbruikbaar zijn.
            "CREATE TABLE products("
            "id VARCHAR(255) PRIMARY KEY,"
            "productnaam VARCHAR(255),"
            "prijs INTEGER)")
    for thing in todo:
        cursor.execute(thing)
    cursor.close()
    connect.commit()
    connect.close()
    return 1


# Nu de table is aangemaakt, kiezen we wat data en stoppen we die in de relationele database.
# Het is wel van belang dat alles wat we willen in een record zit.

def fetchrecords(dbcollection):
    """Returns a dictionary containing ID's, names and (selling) prices of products in order of position encountered.
    Needs a connection to the doc store's collection."""
    identity = []
    names = []
    prices = []

    for post in collection.find():
        for entry in post:
            if entry == '_id':
                identity.append(post[entry])
            elif entry == 'name':
                names.append(post[entry])
            elif entry == 'price':
                prices.append(post[entry]['selling_price'])

    outputdict = {'ids':identity,'names':names,'prices':prices}
    return outputdict

# Sanitising.
# That is crucial by the way since I keep getting SQL errors from inserting that, and the
# following sanitizing rules don't remove these things.

def sanitize(sstring):
    """Sanitises a string for SQL input; removes all cases of ' from the string, and
    also creates a workaround for all numbers encountered at the start and end of the given string."""
    forbiddennumbers = ['0','1','2','3','4','5','6','7','8','9']
    endinput = ''
    if sstring[0] in forbiddennumbers:
        endinput += '_'
    for char in sstring:
        if char != '\'':
            endinput += char
    if sstring[-1] in forbiddennumbers:
        endinput += '_'
    return endinput

# TODO: Uitvogelen waarom de - in een ID meteen verwijst naar een column. Reden volgt.
# Traceback (most recent call)
# line 92, in <module>
# updatedata(fetchrecords(collection),connect("postgres","postgres","TenFour"))
# line 86, in updatedata
# VALUES ({},'{}',{})""".format(id,sanitize(names[ids.index(id)]),prices[ids.index(id)]))
# psycopg2.errors.UndefinedColumn: column "groen" does not exist
# LINE 2:         VALUES (25363-groen,'Bodysecret Zen Fresh Bodyscrub ...

def updatedata(datadict,connect):
    """Fetches data out of a given dict, and writes it into a postgreSQL database."""
    curs = connect.cursor()
    ids = datadict['ids']
    names = datadict['names']
    prices = datadict['prices']
    for id in ids:
        curs.execute("""INSERT INTO products(id,productnaam,prijs)
        VALUES ({},'{}',{})""".format(id,sanitize(names[ids.index(id)]),prices[ids.index(id)]))
    curs.close()
    connect.commit()
    connect.close()
    return 1

updatedata(fetchrecords(collection),connect("postgres","postgres","TenFour"))
# (APA) Bronlijst:
#
# PostgreSQL Python Tutorial With Practical Examples. (2018, 23 februari).
# Geraadpleegd op 4 maart 2020, van https://www.postgresqltutorial.com/postgresql-python/
# PyMongo 3.9.0 Documentation — PyMongo 3.9.0 documentation. (z.d.).
# Geraadpleegd op 4 maart 2020, van https://api.mongodb.com/python/current/