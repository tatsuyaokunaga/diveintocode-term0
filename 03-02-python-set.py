course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}


def find_person(want_to_find_person):
    """
    受講生がどのコースに在籍しているかを出力する。
    まずはフローチャートを書いて、どのようにアルゴリズムを解いていくか考えてみましょう。
    """
    # ここにコードを書いてみる
    for key in course_dict.keys():
        if want_to_find_person <= course_dict[key]:
            print(key+'に'+str(want_to_find_person)+'は在籍しています。')
        elif len(want_to_find_person & course_dict[key])>0:
            print(key+'に'+str(want_to_find_person&course_dict[key])+'のみ在籍しています。')
        else:
            print(key+'に'+str(want_to_find_person)+'は在籍していません。')


def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()
