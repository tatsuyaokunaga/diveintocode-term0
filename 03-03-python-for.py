WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

def output_schedule(study_time_list):
    '''今週の勉強予定を出力します'''
    a=1 # 月曜日が「数学」から始まっているのでインデックスは１から始める
    lists=[] #二重配列を作る
    for n in study_time_list: # リストの要素を取り出す
        list=[] # 各曜日の授業内容をリスト化
        for j in range(a, n + a):
            if a != n: # 休みの日以外の条件分岐
                list.append(SUBJECT_LIST[j%5])
                a = n + a
        lists.append(list) # 二重配列化

    for (i, list) in enumerate(lists): # 二重配列の各要素（曜日）ごとに表示させる
        if len(list)==0: #休みの場合の条件分岐
             print(WEEK_LIST[i]+'曜日は、お休みです。')
        else:
            print(WEEK_LIST[i]+'曜日は、' + str(study_time_list[i])+'時間勉強する予定です。')
            for (j, l) in enumerate(list):
                print(str(j+1)+'限目'+' '+l)


def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()
