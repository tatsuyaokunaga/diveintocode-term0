WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']
def output_schedule(study_time_list):
    lists=[] # 二次元配列を作る
    for (i,n) in enumerate(study_time_list): # リストの要素を取り出す
        list=[] # 各曜日の授業内容をリスト化
        for j in range(i + 1, n + i + 1):
            if i+1 != n+i+1: # 休みの日以外の条件分岐
                list.append(SUBJECT_LIST[j%5])
                i = n + i + 1
        lists.append(list) # listsに各listを格納
    for (i, list) in enumerate(lists): # 二次元配列から各要素（曜日）を表示
        if len(list) == 0: #休みの場合の条件分岐
             print(WEEK_LIST[i]+'曜日は、お休みです。')
        else:
            print(WEEK_LIST[i]+'曜日は、' + str(study_time_list[i])+'時間勉強する予定です。')
            for (j, l) in enumerate(list):
                print(str(j+1)+'限目'+' '+l)
def main():
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)
if __name__ == '__main__':
    main()
