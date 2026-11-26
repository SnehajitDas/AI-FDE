# we want to control our thread
# asyncio.to_thread() --> uses asyncio's default thread pool.

# req :
'''
we want to have 4 thread workers
we want to manage the thread pool overselves
'''

# ThreadPoolExecutor

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# get the event loop
# then pass ThreadPoolExecutor to the event loop

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
    result = await loop.run_in_executor(
        thread_pool,
        legacy_database_call,
        101
    )

    print("Received : ", result)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as thread_pool:
        asyncio.run(main(thread_pool))
