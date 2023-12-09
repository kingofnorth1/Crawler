import json


def read_config():
    # 打开 JSON 文件
    with open('./config/v_config.json', 'r', encoding='utf-8') as file:
        # 从文件中加载 JSON 数据
        data = json.load(file)
    # 打印读取到的内容
    # print(data)
    return data


def get_a1(c):
    # 从cookie中读取a1
    for item_c in c.split(';'):
        key, value = item_c.split('=')
        if key.strip() == 'a1':
            return value
    return None


def has_content(content):
    # 判断评论中是否存在指定配置字符串
    config = read_config()
    comment_keyword = config.get('comment_keyword', '')
    if comment_keyword in content:
        return True
    return False


def while_get_data(temp_list, save_list: list):
    # save_list = []
    for item in temp_list:
        # 判断是否存在配置关键字
        if has_content(item.get('content', '')):
            user_info_temp = item.get('user_info', {})
            save_list.append({
                'create_time': item.get('create_time', 0),
                'content': item.get('content', ''),
                'user_id': user_info_temp.get('user_id', ''),
                'nickname': user_info_temp.get('nickname', ''),
                'ip_location': item.get('ip_location', '')
            })
            sub_comments = item.get('sub_comments', [])
            if len(sub_comments) > 0:
                while_get_data(sub_comments, save_list)

    return save_list
