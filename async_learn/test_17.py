import asyncio
import time

async def main():
    # 不await都不会被调用
    # asyncio.sleep(1)
    # asyncio.sleep(2)
    for i in range(0, 2):
        start = int(time.time())
        await asyncio.sleep(1)
        await asyncio.sleep(2)
        end = int(time.time())
        print("%d seconds elapsed" % (end - start))

asyncio.run(main())