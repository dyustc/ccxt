import asyncio
async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response = await asyncio.sleep(2)
    print("IO请求结束，结果为：", response)
# 看不懂
coroutine_list = [func(), func()]
# coroutine_list = [ asyncio.create_task(func()), asyncio.create_task(func()) ] 
# 错误：coroutine_list = [ asyncio.create_task(func()), asyncio.create_task(func()) ] 
# 此处不能直接 asyncio.create_task，因为将Task立即加入到事件循环的任务列表，
# 但此时事件循环还未创建，所以会报错。
# 使用asyncio.wait将列表封装为一个协程，并调用asyncio.run实现执行两个协程
# asyncio.wait内部会对列表中的每个协程执行ensure_future，封装为Task对象。
done,pending = asyncio.run( asyncio.wait(coroutine_list) )