import mysql.connector


def add_user(my_mail,my_password):

    mydb = mysql.connector.connect(host='localhost',
                         user='root',
                         password='_su3cjo4t/6ej2k7',
                         database = 'assignment',)


    with mydb.cursor() as cursor:
        try:
            my_cursor = mydb.cursor()
            sqlStuff = "INSERT INtO user (email,password) VALUES (%s,%s)"
            record = (my_mail,my_password)
            my_cursor.execute(sqlStuff,record)
            mydb.commit()
            #print("註冊成功")
            return "Added"
        except:
            #print("資料庫新增會員失敗")
            return None


#add_user("test2@gmail.com","256")
 
