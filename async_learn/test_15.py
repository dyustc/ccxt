# 获取协程的返回值
import asyncio
import time
from functools import partial
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "bobby"

def callback(future):
    print("send email to bobby")

def callback1(url, future): # 传入值的时候，future必须在最后一个
    print(url)
    print("send email to bobby")

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.imooc.com"))
    task.add_done_callback(partial(callback1, "http://www.imooc.com"))
    loop.run_until_complete(task)
    print(task.result())