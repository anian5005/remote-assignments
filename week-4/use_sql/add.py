import mysql.connector


def add_user(my_mail,my_password):

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
         result_email = cursor.fetchall() #[('123@gmail.com', '123')]
         #print(result_email)

         try:
             #檢查郵件是否已經註冊
             result_email[0] #('123@gmail.com', '123')
             password = result_email[0][1] #123
             #print(result_email[0])

             #郵件存在
             if result_email != []:
                #print("用戶已存在")
                return "ISmember"

            #郵件不存在 #result_email == []
            #新郵件，註冊資料加進資料庫

         except:
                #print("用戶不存在")
                my_cursor = mydb.cursor()
                sqlStuff = "INSERT INtO user (email,password) VALUES (%s,%s)"
                record = (my_mail,my_password)
                my_cursor.execute(sqlStuff,record)
                mydb.commit()
                #print("註冊成功")
                return "Added"


#add_user("test2@gmail.com","256")
 
