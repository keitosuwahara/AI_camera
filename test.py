import sqlite3
import datetime
from printxl import printxl

date = datetime.datetime.now()
hour = date.hour
minutes = date.minute
sec = date.second

entry = f"{hour}時{minutes}分{sec}秒"

inserts = [
        ("323443","高田悠","1",f"{entry}",f"3"),
        ("353322","黒野怜奈","1",f"2",f"3"),
        ("234567","トゴーフーバダムツェレン","1",f"2",f"3"),
        ("435625","志村","1",f"2",f"{entry}"),
        ("210103","諏訪原慶斗","1",f"{entry}",f"3"),
        ("755456","岩橋大地","1",f"2",f"3"),
        ("305847","桃崎奏斗","1",f"2",f"{entry}")
        ]

dbname ="./database/students.db"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students(学籍番号 STRING PRIMARY KEY , 名前 STRING, 出席 STRING, 遅刻 STRING, 早退 STRING)")
cur.executemany("INSERT INTO students values (?,?,?,?,?)",inserts)

conn.commit()

printxl("students")

# info = "INSERT INTO Students values("
    # for i in range(len(inserts[0])):
    #     info += "?,"
    # info += ")"

    # print(info)    


