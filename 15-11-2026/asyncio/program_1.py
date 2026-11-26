import asyncio
import time

def fetch_customer():
    print("Fetching customer from legacy system...")

    time.sleep(3)

    return {
        "customer_id": 101,
        "name": "John"
    }

async def main():

    print("Async application started")

    customer = await asyncio.to_thread(fetch_customer)

    print("Customer received:", customer)

asyncio.run(main())