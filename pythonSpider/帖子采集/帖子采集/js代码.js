// 先搜索window._webmsxyw   然后令 window.xs = window._webmsxyw
var WebSocket = require("ws");
const jsdom = require("jsdom");
const {JSDOM} = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = dom.window;

(function () {

    let ws = new WebSocket("ws://127.0.0.1:8848/regist.ws?name=xhs");
    ws.onmessage = function (msg) {
        console.log("发送的消息是", JSON.parse(msg.data));
        let data = JSON.parse(msg.data)

        let s = '/api/sns/web/v1/search/notes';
        let i = JSON.parse(msg.data);
        // '202cb962ac59075b964b07152d234b70'
        let ret = window.xs(s, i);
        console.log("计算完毕, 结果是", JSON.stringify(ret));
        ws.send(JSON.stringify(ret));
    }
})();