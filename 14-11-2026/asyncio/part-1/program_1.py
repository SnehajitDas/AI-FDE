import asyncio

# ordinary function
# def check_customer():
#     print("Checking customer")

# asynchronous function
async def check_customer(): # defines a coroutine function
    print("Checking customer")

result = check_customer() # function creates a coroutine object


asyncio.run(result)
# scheduling the coroutine object to execute