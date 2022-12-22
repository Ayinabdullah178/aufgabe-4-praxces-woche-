from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


#mange Class
class Mangas(BaseModel):
    mange_id:int |None = None
    mange_title: str |None = None
    Bande_name: str |None = None
    Erscheinung_Jahr:int |None = None
    Herausgeber:str |None = None
    Autor:str |None = None
    seitenzahl:int |None = None
    
    
    
#anime Class 
class Anime(BaseModel):
    anime_id:int |None = None
    mange_title: str |None = None
    Erscheinung_Jahr:int |None = None
    Herausgeber:str |None = None
    länger:int |None = None
    
    
#Mangas 
mangas =[
    {"mange_id":1,
    "mange_title":'Attack on Titan',
    "band_name": 'eins',
    "Erscheinung_Jahr":2017,
    "Herausgeber":'Egmont_Manga',
    "Autor":'Makoto Shinkal',
    "seitenzahl": 180},
    
    {"mange_id":2,
    "mange_title":'Attack on Titan ',
    "band_name": 'eins',
    "Erscheinung_Jahr":2014,
    "Herausgeber":'Carlsen',
    "Autor":'Hajime Isayama',
    "seitenzahl": 192 } ,
    
    {"mange_id":3,
    "mange_title":'Death Note',
    "band_name": 'eins',
    "Erscheinung_Jahr":2015,
    "Herausgeber":'TOKYOPOP',
    "Autor":'Takeshi Obata  und Tsugumi Ohba',
    "seitenzahl": 208 } ]   


#Anime
animes=[
    {"anime_id":1,
     "anime_title":'Death Note',
     "Erscheinung_Jahr":2006,
     "Herausgeber":'Yosuke Yafune',
     "länger":	125},
    
    {"anime_id":2,
     "anime_title":'Attack on Titan',
     "Erscheinung_Jahr":2013,
     "Herausgeber":'Mikasa Ackermann',
     "länger":120},
    
    {"anime_id":3,
     "anime_title":'One Piece',
     "Erscheinung_Jahr":1999,
     "Herausgeber":'Eiichirō Oda',
     "länger":24}]






       
app = FastAPI()

@app.get("/")
async def root():
    return {"Die werte von Mangas und Anime"}

@app.get("/mangas")
async def get_mange():
    return mangas

@app.get("/mangas/{id}")
async def get_mange(id):
    for u in mangas:
        if u["mange_id"] == int(id):
            return u
#post
@app.post("/mangass", status_code=201)
async def add_Mangas(new_mange:Mangas):
    mangas.append(new_mange)
    return(mangas)
#put
@app.put("/maangas/{mange_id}")
async def put_mange(mange_id: int, mange: Mangas):
    update_encoded = jsonable_encoder(mange)
    mangas[mange_id-1] = update_encoded
    return mangas

#delete
@app.delete("/manngas/{mange_id}", status_code=200)
async def delete_mange(mange_id: int) -> None:
    mangas.remove(mangas[mange_id-1])
    return mangas



@app.get("/animes")
async def get_anime():
    return animes

@app.get("/animes/{id}")
async def get_anime(id):
    for u in animes:
        if u["anime_id"] == int(id):
            return u

@app.post("/aniimes", status_code=201)
async def add_anime(new_anime:Anime):
    animes.append(new_anime)
    return(animes)
#put
@app.put("/annimes/{anime_id}")
async def put_anime(anime_id: int, anime: Anime):
    update_encoded = jsonable_encoder(anime)
    animes[anime_id-1] = update_encoded
    return animes

#delete
@app.delete("/animmes/{anime_id}", status_code=200)
async def delete_anime(anime_id: int) -> None:
    animes.remove(animes[anime_id-1])
    return animes

