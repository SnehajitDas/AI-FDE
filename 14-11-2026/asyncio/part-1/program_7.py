import asyncio
# advantage of create_task

async def monitor_service():
    try:
        print("Monitoring started")
        await asyncio.sleep(60)
    finally:
        # close connection for stream data
        # # close cloud connection 
        print("Cleaning up monitoring task")

async def main():
    task = asyncio.create_task(monitor_service())

    await asyncio.sleep(1)

    # asyncio.Task can be cancelled using task.cancel()
    # it raises asyncio.CancelledError in the coroutine at an 
    # opportunity where cancellation can be delivered.
    task.cancel()

    try : 
        await task
    except asyncio.CancelledError:
        print("Monitoring was cancelled")

asyncio.run(main())