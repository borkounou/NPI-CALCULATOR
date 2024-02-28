from .model import NPIResultData
import os
# MongoDB driver
import motor.motor_asyncio

# This mongodb url is just used for test, it is not a good pratice to show all your credentials, you have put all your credentials in environmment variables. 

'''

The MongoDB URL provided here is only intended for testing purposes. 
It's not considered best practice to expose all of your credentials in plain text.
Instead, it's recommended to store sensitive information such as credentials in environment variables for improved security.
'''

# password= os.getenv('PASSWORD')
# username = os.getenv('USERNAME')
# client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb+srv://{username}:{password}@nousradine.zkkmsbk.mongodb.net/?retryWrites=true&w=majority&appName=nousradine")

client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb+srv://hassan:Borkounou@nousradine.zkkmsbk.mongodb.net/?retryWrites=true&w=majority&appName=nousradine")

database = client.CalculatorNPI 
collection = database.npi 


async def send_result(resultdata):
    document = resultdata
    result = await collection.insert_one(document)
    return document


async def fetch_all_data():
    result = []
    cursor = collection.find({})
    async for document in cursor:
        result.append(NPIResultData(**document))

    return result