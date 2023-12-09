// 先搜索window._webmsxyw   然后令 window.xs = window._webmsxyw
var WebSocket = require("ws");
const {JSDOM} = require('jsdom')
var dom = new JSDOM('', {
    url: 'https://www.xiaohongshu.com/',
})
window = dom.window
var document = window.document;
require('./raw_sign') //这是网站代码修改后的代码


function func() {
    let ws = new WebSocket("ws://127.0.0.1:8848/regist.ws?name=xhs");
    ws.onmessage = function (msg) {
        console.log("发送的消息是", JSON.parse(msg.data));
        let data = JSON.parse(msg.data)

        let s = '/api/sns/web/v1/search/notes';
        let i = JSON.parse(msg.data);
        // '202cb962ac59075b964b07152d234b70'
        var webmsxyw = window._webmsxyw;
        let ret = webmsxyw(s, i);
        console.log("计算完毕, 结果是", JSON.stringify(ret));
        ws.send(JSON.stringify(ret));
    }
}
func();