import sqlite3

dbname = "./database/students.db"
    # DBを作成する（既に作成されていたらこのDBに接続する
conn = sqlite3.connect(dbname)
    #SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()

    #テーブルの作成
print(cur.execute("SELECT COUNT * FROM sqlite_master WHERE TYPE='table' AND name='students'"))                             



# info = "INSERT INTO Students values("
    # for i in range(len(inserts[0])):
    #     info += "?,"
    # info += ")"

    # print(info)    