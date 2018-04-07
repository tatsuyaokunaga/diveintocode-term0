import webbrowser

class School():
    def __init__(self,name,address,number_of_students,founding_year,\  #コンストラクタでインスタンス変数を定義
           introduction_video_url,introduction_statement):
        self.name = name
        self.address = address
        self.number_of_students = number_of_students
        self.founding_year = founding_year
        self.introduction_video_url = introduction_video_url
        self.introduction_statement = introduction_statement

    def sample_instance_method(self): #インスタンスメソッドを定義
        print("{}。そして、{}は、{}にあり創立から{}年の学校で、生徒は{}人です。".format(self.introduction_statement,\
             self.name,self.address,self.founding_year,self.number_of_students))
        webbrowser.open(self.introduction_video_url)

# A学校用のオブジェクトを作成
a_school = School("A学校","渋谷区",300,100,'https://www.youtube.com/watch?v=fizvBkVYdso','A学校は自然豊かな...')
a_school.sample_instance_method()
# B学校用のオブジェクトを作成
b_school = School("B学校", "東京都新宿区..", 500, 30, "https://www.youtube.com/watch?v=wmfLQMKiwWI&t=311s", "B学校は文武両立で...")
b_school.sample_instance_method()
