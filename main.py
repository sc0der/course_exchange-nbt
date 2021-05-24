from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
app = FastAPI()
URL = "https://nbt.tj/ru/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
vall_block = soup.find(class_='kursTable')
kursTableItemsKey = vall_block.find_all('td', class_='k_fColl')
kursTableItemsValue = vall_block.find_all('td', class_='k_sColl')
keys = [x.text.strip() for x in kursTableItemsKey]
values = [x.text.strip() for x in kursTableItemsValue]
dicts = {keys[i][2:]:values[i] for i in range(len(keys))}

@app.get("/nbt/simple/course")
def read_root():
    return dicts
