import asyncio

async def check_service(name):
    await asyncio.sleep(1)

    if name == "Payment API":
        raise ConnectionError("Service is unreachable")

    return f"{name}: healthy"

async def main():
    results = await asyncio.gather(
        check_service("Customer API"),
        check_service("Payment API"), # async task fails
        check_service("Inventory API"),
        return_exceptions=True
    )

    for result in results:
        if isinstance(result, Exception):
            print(f"Check failed: {result}")
        else:
            print(result)

asyncio.run(main())