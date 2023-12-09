from sanic import Sanic, HTTPResponse
import websockets

app = Sanic(__name__)
import json


@app.route("/get", methods=["GET", "POST"])
async def func(req):
    project_name = req.args.get("project_name")

    project_params = req.json  # {url: "xxxxx"}
    if not project_params:
        project_params = "没参数"

    if project_name:
        async with websockets.connect(f"ws://127.0.0.1:8848/invoke.ws?name={project_name}") as ws:
            await ws.send(json.dumps(project_params))
            print("连接成功了")
            ret = await ws.recv()
        return HTTPResponse(ret)
    else:
        return HTTPResponse("你没有给我project_name")


if __name__ == '__main__':
    app.run()
