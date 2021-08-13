from fastapi import FastAPI

app = FastAPI()

'''
    normal def를 사용해도 되지만, async(비동기)를 통해 성능향상 가능
'''

@app.get("/") # operation -> get
async def root():
    return {"message": "Hello World"}



'''
    app.operation({변수})
    해당 방식으로 path parameter 활용
'''
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}




'''
    위에서 아래로 읽기 때문에, 예외를 두려면 순서를 고려해야 한다.
'''
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


'''
If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.
'''
import enum 

class ModelName(str, enum.Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}



'''
Path convertor
Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:
=> /files/{file_path:path}
'''
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


'''
    FastAPI 장점
    - error check
    - 데이터 파싱
    - 데이터 유효성 검사
    - API docs, annotaion 등
'''