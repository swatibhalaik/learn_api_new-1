from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
from pymongo import MongoClient

app = FastAPI()

DB = "api_test"

EMP_COLLECTION = "emp"



class Info(BaseModel):
    name: str
    loc: str
    is_working_from_home: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Message": "Hello Employee"}

@app.post("/emp/")
def create_item(info: Info):
    with MongoClient() as client:
        msg_collection = client[DB][EMP_COLLECTION]
        result = msg_collection.insert_one(info.dict())
        ack = result.acknowledged
        return {"insertion": ack}

@app.get("/emp/")
def read_item(emp_id: int, remarks: Optional[str] = None):
    return {"emp_id": emp_id, "remarks": remarks}

@app.put("/emp/")
def update_info(remarks: Optional[str] = None):
    return {"updated_remarks": remarks}


if __name__ == "__main__":
    # for testing purpose reload=True
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    # for production and deployment reload =False
