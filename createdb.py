import sqlite3

def studentdb():
    stdbname = "./database/students.db"
    # DBを作成する（既に作成されていたらこのDBに接続する
    conn = sqlite3.connect(stdbname)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()

    #テーブルの作成
    cur.execute(
        "CREATE TABLE IF NOT EXISTS students(studentID INTEGER PRIMARY KEY , name STRING, attendance INTEGER)"  
    )#                                                                   出席時=1 欠席時=0                             


    #登録されるデータの初期値
    inserts = [
        (435755,"高田悠",1),
        (557855,"黒野怜奈",1),
        (846556,"トゴーフーバダムツェレン",1),
        (454545,"志村",1),
        (210103,"諏訪原慶斗",1),
        (190721,"岩橋大地",1),
        (200284,"桃崎奏斗",1)
        ]
    
    # 複数データ登録
    cur.executemany('INSERT INTO students values(?,?,?)',inserts)

    
    # コミットしないと登録が反映されない
    conn.commit()



def admindb():#管理者用のデータベース
    admindbname = "./database/administrator.db"
    # DBを作成する（既に作成されていたらこのDBに接続する
    conn = sqlite3.connect(admindbname)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()
    #テーブルの作成
    cur.execute(
        "CREATE TABLE IF NOT EXISTS students(studentID INTEGER PRIMARY KEY , name STRING)"  
    )#                                                                                                
    #登録されるデータの初期値
    inserts = [
        (210103,"諏訪原慶斗"),
        ]

    # 複数データ登録
    cur.executemany('INSERT INTO students values(?,?)',inserts)

    # コミットしないと登録が反映されない
    conn.commit()

if __name__ == ("__main__"):
    studentdb()
    admindb()