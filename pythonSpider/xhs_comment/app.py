# 1. 设定关键词配置文本，爬取搜索结果的作品id
# 2. 遍历第二步产生的作品评论区，如果评论区包含关键词就采集内容本地保存

import sys
import time
import json
import pandas as pd

from utils.func import read_config, while_get_data
from list_item import note_list
from comment import get_comment

# config
config_v = read_config()
note_keyword = config_v.get('note_keyword', None)
comment_keyword = config_v.get('comment_keyword', None)
try:
    if not (note_keyword and comment_keyword):
        sys.exit('请填写完整配置文件')
except Exception as e:
    sys.exit(f'请填写完整配置文件:{e.args}')


# -------------
def get_notes():
    # get note list
    note_has_more = True
    note_page = 1
    note_set = []
    try:
        while note_has_more:
            note_list_data = note_list(note_keyword, note_page)
            note_list_data = note_list_data.get('data', {})
            # 保存
            note_items = note_list_data.get("items", [])
            for item in note_items:
                if item.get('id', None):
                    note_set.append({
                        'id': item.get('id', None)
                    })
                    print(f"{note_page}::{item.get('note_card', {}).get('display_title', '')}::{item.get('id', None)}")

            # 判断下一页
            note_page += 1
            note_has_more = note_list_data.get('has_more', False)
            time.sleep(5)

        note_df = pd.DataFrame(note_set)
        note_df.to_csv('note_list.csv', index=False)

    except Exception as ee:
        print(f'{ee.args}')
        note_df = pd.DataFrame(note_set)
        note_df.to_csv('note_list.csv', index=False)


def comment_list():
    # read csv
    comment_data_final = {}
    note_df = pd.read_csv('./note_list.csv')
    try:
        for index, row in note_df.iterrows():
            # get comment
            note_id = row['id']
            has_more = True
            cursor = ''
            temp_list = []
            page_count = 1
            while has_more:
                comment_info = get_comment(note_id, cursor, '', 'main')
                # print(comment_info)
                comment_info = comment_info.get('data', {})
                cursor = comment_info.get('cursor', None)
                if not cursor:
                    raise ValueError('cursor is None')
                has_more = comment_info.get('has_more', False)
                comments = comment_info.get('comments', [])

                temp_list = temp_list + while_get_data(comments, [])

                # 展开回复
                for item in comments:
                    sub_comment_has_more = item.get('sub_comment_has_more', False)
                    sub_comment_cursor = item.get('sub_comment_cursor', '')
                    root_comment_id = item.get('id', '')
                    sub_count = 0
                    if root_comment_id:
                        while sub_comment_has_more:
                            sub_c = get_comment(note_id, sub_comment_cursor, root_comment_id, 'sub')
                            sub_c = sub_c.get('data', {})

                            sub_comment_has_more = sub_c.get('has_more', False)
                            sub_comment_cursor = sub_c.get('cursor', '')
                            if not sub_comment_cursor:
                                raise ValueError('sub_comment_cursor is None')
                            sub_comments = sub_c.get('data', {})
                            temp_list = temp_list + while_get_data(sub_comments, [])
                            print(f'sub:{sub_count}')
                            sub_count += 1
                            time.sleep(3)

                print(f'{note_id}::{page_count}::{len(temp_list)}')

                page_count += 1
                time.sleep(5)
            print('_______________________')
            comment_data_final[note_id] = temp_list
        # save
        with open('comments.json', 'w', encoding='utf-8') as json_file:
            json.dump(comment_data_final, json_file, indent=4, ensure_ascii=False)
        print('完成')
    except Exception as e:
        print(f'错误：{e.args}')
        with open('comments.json', 'w', encoding='utf-8') as json_file:
            json.dump(comment_data_final, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    get_notes()
    comment_list()
    # d = get_comment('65433f3c000000002500a3c3', '655c29600000000020029e78', '6556bfba0000000021003c84', 'sub')
    # print(d)
