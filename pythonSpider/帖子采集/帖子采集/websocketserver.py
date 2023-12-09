import websockets
import asyncio
import re

browser_info = {}
client_info = {}


async def regist(ws, path):
    obj = re.compile(r"/(?P<action>.*?)\.ws\?name=(?P<name>.*)")
    search_result = obj.search(path)
    action = search_result.group("action")
    name = search_result.group("name")
    if action == "regist":
        browser_info[name] = ws
        return "browser", name

    elif action == 'invoke':
        client_info[name] = ws
        return "client", name


async def handle(ws, path):
    t, name = await regist(ws, path)
    async for msg in ws:
        if t == 'browser':
            print("调用浏览器")
            await client_info[name].send(msg)
        elif t == 'client':
            print("调用客户端")
            await browser_info[name].send(msg)


async def main():
    async with websockets.serve(handle, "127.0.0.1", 8848) as flkjdaslkfjadslkjfkladsjflkasd:
        print("你成功的启动了一个websocket")
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
