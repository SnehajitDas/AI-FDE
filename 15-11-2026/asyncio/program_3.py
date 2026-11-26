# ThreadPoolExecutor

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def legacy_database_call(customer_id):
    print(f"Fetching customer {customer_id}")

    time.sleep(2)

    return {
        "customer_id": customer_id,
        "status": "active"
    }

async def main(thread_pool):
    # customer = await asyncio.to_thread(legacy_database_call(101))
    loop = asyncio.get_running_loop()

    customer_ids = [101, 102, 103, 104]

    tasks = [
        loop.run_in_executor(thread_pool, legacy_database_call, cid)
        for cid in customer_ids
    ]

    results = await asyncio.gather(*tasks)

    for result in results :
        print(result)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as thread_pool:
        asyncio.run(main(thread_pool))

# asyncio.to_thread()
# Uses default thread pool
# Not directly configurable per call
# Passed directly
# Convenient way to offload blocking calls

# run_in_executor()
# Can use a specified thread pool
# Configure through ThreadPoolExecutor
# Passed after executor argument
# More explicit executor management
