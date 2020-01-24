import tracemalloc
import asyncio

tracemalloc.start()
async def hello():
    async def test():
        print('Hello World!')
        asyncio.sleep(5000)
    test()
hello()