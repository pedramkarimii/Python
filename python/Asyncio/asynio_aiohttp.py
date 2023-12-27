import asyncio
import aiohttp

# Function to fetch the status code of a given URL using aiohttp
async def show_status(session, url):
    async with session.get(url) as result:
        return result.status

# Main function to run the asynchronous tasks
async def main():
    # Creating a aiohttp ClientSession within a context manager
    async with aiohttp.ClientSession() as session:
        # List of URLs to fetch status codes
        urls = ["https://typeo.top/class/", "https://www.tradingview.com/chart/nKr86WSj/", "https://github.com/pedramkarimii"]
        
        # Creating a list of tasks to fetch status codes concurrently
        tasks = [show_status(session, url) for url in urls]
        
        # Gathering results from the tasks and handling exceptions
        statuses_code = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Printing the status codes obtained from the URLs
        print(f"Status codes are: {statuses_code}")

# Running the main function using the asyncio run function
asyncio.run(main())

