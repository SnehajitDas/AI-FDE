import asyncio

# ordinary function
# def check_customer():
#     print("Checking customer")

# asynchronous function
async def check_customer(var_v): # defines a coroutine function
    print("Checking customer", var_v)
    print("Customer check completed")

async def main():
    await check_customer(1)
    a = check_customer(1)
    await check_customer(2)
    await check_customer(3)


# asyncio.run(main()) # entry point
asyncio.run(main())
# scheduling the coroutine object to execute