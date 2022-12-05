import sqlite3
import datetime

#とDBの更新をするプログラムです


# DBを作成する（既に作成されていたらこのDBに接続する
dbname ="./database/students.db"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()

def operatedb(sql):
    result = cur.execute(sql)
    conn.commit()
    return result
# コミットしないと登録が反映されない

today = datetime.date.today()#今日の日付

#UPDATE テーブル名 SET 列名 = "変えた後の値" where 列名 = "変える前の値" 
operatedb('UPDATE students SET 名前 = "山田孝之" where 名前 = "諏訪原慶斗"')
conn.commit()












