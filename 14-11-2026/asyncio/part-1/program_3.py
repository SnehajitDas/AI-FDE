import asyncio
import time


# asynchronous function
async def check_customer(var_v): # defines a coroutine function
    print("Checking customer", var_v)
    await asyncio.sleep(2) #non-blocking
    print("Customer check completed", var_v)

async def main():

    start = time.perf_counter()

    await check_customer(1)
    await check_customer(2)

    print(f"Elapsed: {time.perf_counter() - start:.2f} seconds")

asyncio.run(main())

# await can be done for functions that are asynchronous
# as soon as await is encountered, event loop will run the
# function ready to run

# await is still sequential

# code is asynchronous code
# but function calls are still one after other

# Elapsed: 4.01 seconds