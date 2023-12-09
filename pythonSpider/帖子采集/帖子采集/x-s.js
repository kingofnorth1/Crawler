const {JSDOM} = require('jsdom')
var dom = new JSDOM('', {
    url: 'https://www.xiaohongshu.com/',
})
window = dom.window
var document = window.document;

require('./raw_sign') //这是网站代码修改后的代码


function sign(path, data, cookie) {
    document.cookie = cookie;
    var webmsxyw = window._webmsxyw
    return webmsxyw(path, data);
}

// let xsXt = window._webmsxyw("/api/sns/web/v1/homefeed", {
//         'cursor_score': '',
//         'num': 10,
//         'refresh_type': 3,
//         'note_index': 0,
//         'unread_begin_note_id': '',
//         'unread_end_note_id': '',
//         'unread_note_count': 0,
//         'category': 'homefeed_recommend',
//     })
//
// xsXt = window._webmsxyw('/api/sns/web/v1/user_posted?num=30&cursor=&user_id=5e55b04a000000000100b3a8', '')
xsXt = sign('https://edith.xiaohongshu.com/api/sns/web/v1/search/notes', '', 'a1=18c15c3a584cmn563hjqkvc6q7qanqnrvo0muwp4950000133051;' )
// xsXt = sign('https://edith.xiaohongshu.com/api/sns/web/v1/search/notes', '', 'a1=18c15c3a584cmn563hjqkvc6q7qanqnrvo0muwp4950000133051;' )
console.log(xsXt)

console.log(xsXt['X-s'].length)





module.exports = sign;