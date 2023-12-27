import asyncio
import aiohttp

async def show_status(session, url, delay):
    # Simulate a delay before making the request
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        print(f"Status for {url} is {result.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        # Create a list of coroutines
        requests = [
            show_status(session, "https://typeo.top/class/", 3),
            show_status(session, "https://www.tradingview.com/chart/nKr86WSj/", 6),
            show_status(session, "https://github.com/pedramkarimii", 1)
        ]

        # Use asyncio.gather to run coroutines concurrently
        # responses = await asyncio.gather(*requests)

        # Note: You can process the responses if needed

        # Alternatively, you can use asyncio.as_completed to iterate over completed futures
        for request in asyncio.as_completed(requests):
            response = await request
            Process the response

# Run the main function using asyncio.run()
asyncio.run(main())

