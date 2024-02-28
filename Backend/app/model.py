from pydantic import BaseModel

class NPICalculator(BaseModel):
    expression:str


class NPIResultData(NPICalculator):
    result:str