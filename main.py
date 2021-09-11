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

@app.post("/emp/")
def create_item(info: Info):
    return info

@app.get("/emp/")
def read_item(emp_id: int, remarks: Optional[str] = None):
    return {"emp_id": emp_id, "remarks": remarks}

@app.put("/emp/")
def update_info(remarks: Optional[str] = None):
    return {"updated_remarks": remarks}
