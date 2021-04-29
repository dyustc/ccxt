import asyncio
import time

async def others(time):
    print("start" + str(time))
    await asyncio.sleep(time)
    print('end' + str(time))
    return '返回值' + str(time)

async def my_print(response):
    print(response)

async def func():
    start = int(time.time())
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    # response2 = asyncio.create_task(others(2))
    # response1 = asyncio.create_task(others(1))
    # tasks = [response1, response2]
    # await asyncio.wait(tasks)
    # r2 = response2.result()
    # r1 = response1.result()

    response2 = asyncio.create_task(others(2))
    response1 = asyncio.create_task(others(1))
    r2 = await response2
    r1 = await response1
    
    # response2 = asyncio.create_task(others(2))
    # r2 = await response2
    # response1 = asyncio.create_task(others(1))
    # r1 = await response1

    # r2 = await others(2)
    # r1 = await others(1)
    end = int(time.time())
    print("%d seconds elapsed" % (end - start))
    print("IO请求结束，结果为：", r2)
    print("IO请求结束，结果为：", r1)
    
# run 只能跟corountine
# await 可以跟coroutine, task, future
# corountine 一定要加await， 不加await不会被调用
# wait 跟task or corountine wrapped in list, 返回一个coroutine, corountine每个元素都成为了task
# gather 和 wait 来比较, gather 和 wait都能得到结果，gather 更high-level一些
# run_until_complete 可以跟coroutine,  task
asyncio.run( func() )