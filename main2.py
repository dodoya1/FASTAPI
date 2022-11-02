#クエリパラメータ
from fastapi import FastAPI

#インスタンス化を行う。
app = FastAPI()

#以下のように、パスパラーメーターはないが、引数が設定されている場合、その引数がクエリパラメータとなる。
#「=」として、デフォルト値を設定することができる。
#「http://127.0.0.1:8000/countries/?country_name=America&country_no=3
#のように、「?」以降にクエリパラメータを設定することで実行できる。
@app.get("/countries/")
async def country(country_name:str="japan",country_no:int=1):
    return {
        "country_name": country_name,
        "country_no": country_no
    }