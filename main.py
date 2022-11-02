#パスパラメータ
from fastapi import FastAPI

#インスタンス化を行う。
app = FastAPI()

@app.get("/countries/{country_name}")
async def country(country_name:str):
    return {"country_name": country_name}