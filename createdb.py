import sqlite3
import datetime
import tkinter

#GUIでデータベースの中身をいじる関数
def GUI():


















    

def now():#現在時刻を出す関数
    dt_now = datetime.datetime.now()#現在時刻
    return dt_now.strftime('%H時%M分')

#studentテーブルのパス
stdbname = "./database/students.db"
#管理者テーブルのパス
admindbname = "./database/administrator.db"
def studentdb():
    # DBを作成する（既に作成されていたらこのDBに接続する
    conn = sqlite3.connect(stdbname)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()

    #ここでテーブルが存在してたらいったん削除する
    drop_sttable = '''drop table if exists students'''
    cur.execute(drop_sttable)

    #テーブルの作成
    cur.execute(
        "CREATE TABLE IF NOT EXISTS students(学籍番号 INTEGER PRIMARY KEY , 名前 STRING, 出席 INTEGER, 遅刻 INTEGER, 早退 INTEGER)"  
    )#                                                                   出席時=1 欠席時=0                             


    #登録されるデータの初期値
    inserts = [
        (435755,"高田悠",1,0,0),
        (557855,"黒野怜奈",1,0,0),
        (846556,"トゴーフーバダムツェレン",1,now(),0),
        (454545,"志村",1,0,0),
        (210103,"諏訪原慶斗",1,0,0),
        (190721,"岩橋大地",1,0,0),
        (200284,"桃崎奏斗",1,0,0)
        ]
    
    # 複数データ登録
    cur.executemany("INSERT INTO students values(?,?,?,?,?)",inserts)

    
    # コミットしないと登録が反映されない
    conn.commit()



def admindb():#管理者用のデータベース
    # DBを作成する（既に作成されていたらこのDBに接続する
    conn = sqlite3.connect(admindbname)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()
    #ここでテーブルをいったん削除する
    drop_adtable = '''drop table if exists administrator'''
    cur.execute(drop_adtable)
    #テーブルの作成
    cur.execute(
        "CREATE TABLE IF NOT EXISTS administrator(ID INTEGER PRIMARY KEY , 名前 STRING)"  
    )#                                                                                                
    #登録されるデータの初期値
    inserts = [
        (210103,"諏訪原慶斗"),
        ]

    # 複数データ登録
    cur.executemany('INSERT INTO administrator values(?,?)',inserts)

    # コミットしないと登録が反映されない
    conn.commit()

if __name__ == ("__main__"):
    studentdb()
    admindb()