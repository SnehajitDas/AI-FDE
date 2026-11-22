# asyncio.gather()
# run multiple coroutines concurrently and collect their results together

import asyncio
import time

async def check_service(name, version):
    print(f"Checking {name}, Version : {version}")
    await asyncio.sleep(2)
    print(f"{name} is healthy")
    return f"{name}: OK"

async def main():
    start = time.perf_counter()

    results_1 = asyncio.gather(
        check_service("Customer API", 1.0),
        check_service("Payment API", 1.0),
        check_service("Inventory API", 1.0)
    )

    results_2 = asyncio.gather(
        check_service("Customer API", 2.0),
        check_service("Payment API", 2.0),
        check_service("Inventory API", 2.0)
    )

    results_1, results_2 = await asyncio.gather(results_1, results_2)
    
    for result in results_1:
        print(result)

    for result in results_2:
            print(result)

    print(f"Elapsed: {time.perf_counter() - start:.2f} seconds")

asyncio.run(main())
