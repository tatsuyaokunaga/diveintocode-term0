import csv
#csvモジュールをインポートする

with open('KOUKYOU.csv', 'r')  as f: #ファイルオブジェクトとしてファイルを開く
    dataReader = csv.reader(f) #与えられた csvfile 内の行を反復処理するような reader オブジェクトを返す

    for row in dataReader: #dataReaderは、1行ずつをリストとして返す
       mojiretsu=' '.join(row) # リスト内の各要素を半角スペースで連結
       print(mojiretsu)
