import asyncio
import httpx

URLS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org"
]

async def check_url(client, url):

    try:
        response = await client.get(url)

        return {
            "url": url,
            "status": response.status_code
        }

    except httpx.RequestError as error:

        return {
            "url": url,
            "error": str(error)
        }

async def main():
    async with httpx.AsyncClient(timeout=5.0) as client:
        results = await asyncio.gather(
            *[
                check_url(client, url)
                for url in URLS
            ]
        )

        # results = await asyncio.gather(
        #                 check_url(client, url),
        #                 check_url(client, url),
        #                 check_url(client, url),

        #         )

        for result in results:
            print(result)

if __name__ == "__main__":
    asyncio.run(main())