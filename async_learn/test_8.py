import asyncio
async def others(time):
    print("start" + str(time))
    await asyncio.sleep(time)
    print('end' + str(time))
    return '返回值' + str(time)

async def my_print(response):
    print(response)

async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response2 = asyncio.create_task(others(2))
    response1 = asyncio.create_task(others(1))
    tasks = [response1, response2]
    done, pending = await asyncio.wait(tasks)
    print(done)
    
    # response2 = asyncio.create_task(others(2))
    # response1 = asyncio.create_task(others(1))
    # r2 = await response2
    # r1 = await response1
    
    # response2 = asyncio.create_task(others(2))
    # r2 = await response2
    # response1 = asyncio.create_task(others(1))
    # r1 = await response1

    # r2 = await others(2)
    # r1 = await others(1)

    # print("IO请求结束，结果为：", r2)
    # print("IO请求结束，结果为：", r1)
    

asyncio.run( func() )