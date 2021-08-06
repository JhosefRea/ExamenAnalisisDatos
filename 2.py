import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument

db_client = MongoClient()
my_db = db_client.bdnoticia
my_posts = my_db.colecc
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):

    return string.find(substring, string.find(substring))

response = requests.get("https://www.elcomercio.com/deportes/argentina-perdio-fase-grupos-fue-eliminada-juegos-olimpicos.html")
soup = BeautifulSoup(response.content, "lxml")

Course=[]
Provider=[]
Duration=[]
Start_Date=[]
Offered_By=[]
No_Of_Reviews=[]
Rating=[]


title = soup.find_all("h1", class_="entry__title")
post_course=soup.find_all("span", class_="text-1 weight-semi line-tight")
post_provider=soup.find_all("a", class_="color-charcoal italic")

extracted = []
    

print(title)
print(Provider)

dfDS = pd.DataFrame({'course':Course, 'provider':Provider})
out = dfDS.to_dict()
print(dfDS)