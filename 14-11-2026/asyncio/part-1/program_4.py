import asyncio
import time
# asyncio.Task


# asynchronous function
async def check_customer(var_v): # defines a coroutine function
    try : 
        print("Checking customer", var_v)
        await asyncio.sleep(2) #non-blocking
        print("Customer check completed", var_v)
        return 200
    except:
        return 400

async def main():
    # await check_customer(1)
    # await check_customer(2)

    start = time.perf_counter()

    customer_task_1 = asyncio.create_task(check_customer(1))
    # creates and schedules

    customer_task_2 = asyncio.create_task(check_customer(2))

    result_1 = await customer_task_1
    result_2 = await customer_task_2

    print(result_1)
    print(result_2)

    print(f"Elapsed: {time.perf_counter() - start:.2f} seconds")


asyncio.run(main())

# await can be done for functions that are asynchronous
# as soon as await is encountered, event loop will run the
# function ready to run

# await is still sequential

# code is asynchronous code
# but function calls are still one after other

# Elapsed: 2.01 seconds