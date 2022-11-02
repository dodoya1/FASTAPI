#以下のように、型を定義できる。(型ヒント)
#ただし、定義した型と異なる型が代入されても、エラーは発生しない。
#開発者にとって分かりやすいよう書いているだけのようなもの。
price:int=100
tax:float=1.1

#以下のように、型を定義できる(型ヒント)。返り値の型も定義できる。
def calc_price_including_tax(price:int,tax:float) -> int:
    return int(price*tax)

if __name__=="__main__":
    print(f"{calc_price_including_tax(price=price,tax=tax)}円")



#型を配列もしくは辞書として定義する方法は、以下のように行う。(型ヒントの仕方が少し違う)
from typing import List, Dict

sample_list: List[int] = [1, 2, 3, 4]
sample_dict: Dict[str,str] = {"username": "abcd"}