# ThreadPoolExecutor

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def count_primes(start, end):

    count = 0

    for number in range(start, end):

        if number < 2:
            continue

        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return count

async def main(process_pool):
    # customer = await asyncio.to_thread(legacy_database_call(101))
    loop = asyncio.get_running_loop()

    jobs = [
        (2, 50_000),
        (50_000, 100_000),
        (100_000, 150_000),
        (150_000, 200_000)
    ]


    tasks = [
        loop.run_in_executor(process_pool, count_primes, a, b)
        for a,b in jobs
    ]

    results = await asyncio.gather(*tasks)

    for result in results :
        print(result)

    print(sum(results))

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as process_pool:
        asyncio.run(main(process_pool))

