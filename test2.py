import sqlite3

#studentテーブルのパス
stdbname = "./database/students.db"
#管理者テーブルのパス
admindbname = "./database/administrator.db"
def studentdb():
    # DBを作成する（既に作成されていたらこのDBに接続する
    conn = sqlite3.connect(stdbname)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()

    for i in cur.execute('select * from students'):
        print(i)
studentdb()