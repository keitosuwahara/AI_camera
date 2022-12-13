import sqlite3
inserts = [
        (435755,"高田悠",1,1,1),
        (557855,"黒野怜奈",1,1,1),
        (846556,"トゴーフーバダムツェレン",1,1,1),
        (454545,"志村",1,1,1),
        (210103,"諏訪原慶斗",1,0,1),
        (190721,"岩橋大地",1,0,0),
        (200284,"桃崎奏斗",1,0,0)
        ]

for ii in inserts:
    for suf, i in enumerate(list(ii)):
        if suf == 0:
            print(i)

dbname ="./database/students.db"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()
cur.executemany("insert into students values (?,?,?,?,?)",inserts)

conn.commit()

# info = "INSERT INTO Students values("
    # for i in range(len(inserts[0])):
    #     info += "?,"
    # info += ")"

    # print(info)    


