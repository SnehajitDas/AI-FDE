# asyncio.gather()
# run multiple coroutines concurrently and collect their results together

import asyncio
import time

async def check_service(name):
    print(f"Checking {name}")
    await asyncio.sleep(2)
    print(f"{name} is healthy")
    return f"{name}: OK"

async def main():
    start = time.perf_counter()

    results = await asyncio.gather(
        check_service("Customer API"),
        check_service("Payment API"),
        check_service("Inventory API")
    )
    
    # schedules the supplied coroutine operations and 
    # collects their results in the order in which they were supplied

    for result in results:
        print(result)

    print(f"Elapsed: {time.perf_counter() - start:.2f} seconds")

asyncio.run(main())
