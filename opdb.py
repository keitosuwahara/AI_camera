import sqlite3

# DBを作成する（既に作成されていたらこのDBに接続する
dbname ="./database/students.db"

conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()



#update用のSQL
update_sql = 'UPDATE students SET name="志村耀介" WHERE studentID=454545'

# データ更新
cur.execute(update_sql)
cur.execute('UPDATE students SET studentID= 186758 WHERE name="志村耀介"')
cur.execute('UPDATE students SET attendance=1 WHERE name="志村耀介"')

#データベース内の表示データベース内の表示
records=cur.execute("SELECT * FROM students")
print("学籍番号  名前  出欠席")
for record in records:
    print(record)


# コミットしないと登録が反映されない
conn.commit()













