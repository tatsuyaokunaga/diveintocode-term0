import csv #csvモジュールをインポートする

with open('KOUKYOU.csv', 'r')  as f:#ファイルオブジェクトとしてファイルを開く
    dataReader = csv.reader(f) #与えられた csvfile 内の行を反復処理するような reader オブジェクトを返す
    header = next(dataReader)  # 最初の一行をヘッダーとして取得
    data=sorted(dataReader,key=lambda x:x[1]) #昇順に並び替える
    print(' '.join(header))  # ヘッダーをスペース区切りで表示
    for row in data: #dataは、1行ずつをリストとして返す
        mojiretsu=' '.join(row) # リスト内の各要素を半角スペースで連結
        print(mojiretsu)
