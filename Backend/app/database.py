from model import NPIResultData
import os
# MongoDB driver

import motor.motor_asyncio

password= os.getenv('PASSWORD')
username = os.getenv('USERNAME')

client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb+srv://{username}:{password}@nousradine.zkkmsbk.mongodb.net/?retryWrites=true&w=majority&appName=nousradine")

database = client.CalculatorNPI 
collection = database.npi 


async def send_result(resultdata):
    document = resultdata
    result = await collection.insert_one(document)
    return document


async def fetch_all_data():
    result = []
    cursor = collection.find({})
    # data = [{"expression":doc["expression"], "result":doc["result"]} for doc in cursor]
    # df = pd.DataFrame(data)
    # df.to_csv("results.csv", index=False)

    async for document in cursor:
        result.append(NPIResultData(**document))

    return result