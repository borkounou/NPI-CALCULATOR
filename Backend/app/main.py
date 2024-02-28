from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from .database import fetch_all_data, send_result
from .model import NPICalculator, NPIResultData
from .algorithm_npi import polonaise_npi
import pandas as pd 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/calculator")
async def get_data():
    response = await fetch_all_data()
    data = {"expression": [r.expression for r in response], "result": [r.result for r in response]}
    df = pd.DataFrame(data)
    df.to_csv("expressions_results.csv", index=False)
    
    return FileResponse(path='./expressions_results.csv', filename=f"expressions_results.csv")

    
@app.post("/api/calculator", response_model=NPIResultData)
async def compute_data(calculator:NPICalculator):
    resutat = polonaise_npi(calculator.expression)
    print(resutat)
    response = await send_result(resutat.model_dump())

    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong / Bad request")
