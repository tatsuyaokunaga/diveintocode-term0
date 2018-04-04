def show_staffs(names=None):
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # XXXここの関数の定義を行なってくださいXX
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        if names==None:# 引数に何も渡されなかった時の処理
            print('今日出勤する人はいません。')
        else:
            if type(names)==str: # 条件分岐 一人の時
                print('今日出勤する人は、'+str(names)+'さんです。')
            else:
                for name in names:# 条件分岐 リストの場合
                    print('今日出勤する人は、'+str(name)+'さんです。')

show_staffs()
show_staffs('一郎')
workers = ["一郎", "次郎", "三郎"]
show_staffs(workers)
