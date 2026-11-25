import aiohttp
import asyncio 

async def perform_calculation():

    url = "http://127.0.0.1:8000/calculate"

    payload = {
        "num1": 45,
        "num2": 85,
        "operation":"multiply"
    }


    async with aiohttp.ClientSession() as session:

        async with session.post(url, json=payload) as response:

            result = await response.json()

            print("Status Code :", response.status)
            print("Response: ", result)

if __name__ == '__main__':
    asyncio.run(perform_calculation())