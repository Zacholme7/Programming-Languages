# 4.8: Setting a timeout as as_completed
import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed, fetch_status

@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, "https://www.example.com", 1),
                    fetch_status(session, "https://www.example.com", 10),
                    fetch_status(session, "https://www.example.com", 10)]

        # await all the tasks and set the timeout to 2
        for done_task in asyncio.as_completed(fetchers, timeout = 2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("We got a timeout error")
        for task in asyncio.tasks.all_tasks():
            print(task)

asyncio.run(main())
