'''
Swagger文档地址：http://localhost:8080/docs#/
http://localhost:8080/redoc
IP默认值：127.0.0.1
'''

import uvicorn #运行代码的服务器
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

### get
@app.get('/')  #无参返回，，路径操作装饰器
def read_root():
    return {"Hello": "World"}
@app.get('/add/a={a}/b={b}') #指定传参

def add(a: int = None, b: int = None):
    c = a + b
    res = {"res": c}
    return res

@app.get('/man/name={Name}/age={Age}')
def get_full_name(Name:str,Age:int=None):   #指定传参并指定参数类型，当参数类型错误时，会自动判断给出错误提示
    full_name = Name.title()+str(Age)
    return full_name
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/info/") #  localhost:8080/?start=1&end  不属于路径参数的其他参数将自动解释为函数参数
def look_up(start:int=0,end:int=5):
    return fake_items_db[start:end]

### post

class Item(BaseModel):   #创建数据模型→提交参数的字段和类型
    name: str
    description: str = None  #创建类型和默认值，None表示可以为空
    price: float
    tax: float = None

@app.post("/items/")
async def PostItemInfo(item: Item):  #声明参数，并将其类型说明为创建的模型
    print(item)
    return item   ##这个很重要！！！，表示post后返回过来的内容

###  put

#put方法可以这样理解：1.参数item_id为查询条件，**item.dict()为put提交的内容
@app.put("/put_items/{item_id}")
async def PutItemInfo(item_id: int, item: Item):

    return {"item_id": item_id, **item.dict()} #将PUT的查询条件和put内容合并为json格式，后续可以将数据处理然后更新数据库
# ########============  delete  ============########
class Delete(BaseModel):   #创建数据模型→提交参数的字段和类型
    id:int
@app.delete("/delete_items/")
async def DeleteItem(item: Delete):  #声明参数，并将其类型说明为创建的模型
    print(item)
    return item

if __name__ == '__main__':

    uvicorn.run(app=app,
                host="localhost",
                port=8080,
                workers=1)
