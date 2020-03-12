from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)

db = client.huwebshop
products = db.products


# Query 1
def firstProduct():
    """return eerste product in databse"""
    result = products.find_one()
    return result["name"]


# Query 2
def productStartsWith(letter):
    """Query 2: return eerste product dat begint met letter"""
    name = "name"

    # regex statement gemaakt dmv internetbron.
    res = products.find_one({name: {'$regex': '^' + letter, '$options': 'i'}}, {})
    p = products.find_one(res)
    return p["name"]


# Query 3
def avrgPrice():
    """return gemiddelde van alle prijzen v.d. producten in de database"""
    prices = []
    for x in products.find():
        prices.append(x["price"]["selling_price"])
    avrg = 0
    for i in prices:
        avrg += int(i)
    return avrg / len(prices)


print(firstProduct())
print(productStartsWith("W"))
print(avrgPrice())
