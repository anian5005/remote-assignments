
import mysql.connector



def check_user(my_mail,my_password):

    mydb = mysql.connector.connect(host='localhost',
                         user='root',
                         password='_su3cjo4t/6ej2k7',
                         database = 'assignment',)


    with mydb.cursor() as cursor:
        # 查詢資料SQL語法

        command = "SELECT email,password FROM user WHERE email = %s"
        # 執行指令
        cursor.execute(command, (my_mail,))
        # 取得所有資料
        result = cursor.fetchall() #[('123@gmail.com', '123')]


        try:
            #資料庫存在此郵件
            result[0] #('123@gmail.com', '123')
            password = result[0][1] #123

            #郵件密碼皆正確
            if result != [] and password == my_password:
                return "ISmember"

            #郵件正確 密碼錯誤
            elif result != [] and password != my_password:
                return "wrong_password"
            #用戶不存在
        except:
               return None