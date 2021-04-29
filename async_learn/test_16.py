# coding=utf-8
import asyncio
import time


async def step1 (n, start):
    try:
        await asyncio.sleep(n)
        print("第一阶段完成")
        print("此时用时", time.time() - start)
        return n
    except asyncio.CancelledError:
        print(f"数字{n}被取消")
        raise


async def step2 (n, start):
    try:
        await asyncio.sleep(n)
        print("第二阶段完成")
        print("此时用时", time.time() - start)
        return n
    except asyncio.CancelledError:
        print(f"数字{n}被取消")
        raise


async def main ():
    now = time.time()
    tasks = [
        step1(5, now), step2(2, now)
    ]
    # 1.gather并发：gather通常被用来阶段性的一个操作，做完第一步才能做第二步
    result = await asyncio.gather(*tasks)
    for i in result:
        print(i)
    
    # 2.wait并发：阻塞式并行，大于最大的阻塞时间--------------------------
    # timeout：超时时间
    # complete, pending = await asyncio.wait(tasks)
    # for i in complete:
    #     print(i.result())
    # if pending:
    #     print("取消未完成的任务")
    #     for p in pending:
    #         p.cancel()
    
    print("总用时", time.time() - now)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

