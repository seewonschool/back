from typing import Union

from fastapi import FastAPI

app = FastAPI()

from model.major import Major

from cse.important import cse_important
from kor.main import kor_important
from MEC.main import MEC_important
from AI.main import AI_important
from AIE.main import AIE_important
from SSE.main import SSE_important
from CBE.main import CBE_important
from EE.main import EE_important


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/notices/all/{major}")
def read_notice(major: Major):
    if major == "cse":
      return cse_important()
    if major == "kor":
        return kor_important()
    if major == "MEC":
        return MEC_important()
    if major == "AI":
        return AI_important()
    if major == "AIE":
        return AIE_important()
    if major == "SSE":
        return SSE_important()
    if major == "CBE":
        return CBE_important()
    if major == "EE":
        return EE_important()
