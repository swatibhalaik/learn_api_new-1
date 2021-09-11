from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Info(BaseModel):
    name: str
    loc: str
    is_working_from_home: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Message": "Hello Employee"}


@app.get("/emp/{emp_id}")
def read_item(emp_id: int, remarks: Optional[str] = None):
    return {"emp_id": emp_id, "remarks": remarks}


@app.put("/emp/{emp_id}")
def update_item(emp_id: int, info: Info):
    return {"emp_name": info.name, "emp_id": emp_id}
