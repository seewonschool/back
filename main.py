from typing import Union

from fastapi import FastAPI

app = FastAPI()

from model.major import Major
from cse.important import cse_important
from kor.main import kor_important
from mec.main import mec_important

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/notices/today/{major}")
def read_notice(major: Major):
    if major == "cse":
      return cse_important()
    if major == "kor":
        return kor_important()
    if major == "mec":
        return mec_important()