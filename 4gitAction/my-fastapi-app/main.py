import platform
from fastapi import FastAPI

# app 객체를 생성합니다.
app = FastAPI()

# 반드시 @app.get() 을 사용해야 합니다!
@app.get("/")
def read_root():
    return {
        "message": "FastAPI가 정상 작동 중입니다.",
        "os_info": platform.system(),
        "architecture": platform.architecture()[0]
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}