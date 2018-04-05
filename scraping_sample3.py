def get_link(page_info):
    href_number = page_info.find("href=")

    if href_number == -1:
        return None, 0

    start_number = page_info.find('"', href_number)
    end_number = page_info.find('"', start_number + 1)
    url = page_info[start_number + 1:end_number]

    return url, end_number   # 返り値をurlとend_numberに設定

import requests  # ライブラリをインポート
page = requests.get('https://diveintocode.jp/') #HPにリクエストを生成
page_info = page.text #ページの情報から、ページのHTMLソースの内容だけを取り出す
get_link(page_info)

while True:
    url, end_position = get_link(page_info) # 返り値を二つの変数に代入
    if url == None: # Noneの場合処理を終了
        break
    print(url) # linkを表示
    page_info = page_info[end_position:]
