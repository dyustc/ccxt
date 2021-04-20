import time
import asyncio

# def hello():
#     time.sleep(1)

# def run():
#     for i in range(5):
#         hello()
#         print('Hello World: %s' % time.time())

async def hello():
    # await asyncio.sleep(1)
    asyncio.sleep(1)
    print('Hello World: %s' % time.time())

def run():
    for i in range(5):
        # loop.run_until_complete(hello())
        asyncio.run(hello())

loop = asyncio.get_event_loop()

if __name__ == '__main__':
    run()
    loop.close()