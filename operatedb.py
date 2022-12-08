from createdb import createdb
import sqlite3
import datetime
import tkinter as tk
import tkinter.messagebox as tmsg
import glob
from testtk import show_db


def now():#現在時刻を出す関数
    dt_now = datetime.datetime.now()#現在時刻
    return dt_now.strftime('%H時%M分')


#DBの更新をするプログラムです
"""
tkinterでdb内の閲覧や情報の更新ができるようにする
"""


window = tk.Tk()
window.geometry("700x250")
window.title("データベース設定")

# 遷移前の画面の作成                                                            
top_page = tk.Canvas(width=800, height=800)
top_page.place(x=0, y=0) # キャンバス



top_label =  tk.Label(window, text = "項目を選んでください", font = ("Helvetica", 10))
top_label.place(x=270, y=10)

btn_createdb = tk.Button(window,text = "データベースの新規作成", command = lambda:run_createdb(top_page))
btn_createdb.place(x=100, y=150)

#createdbを呼び出す
def run_createdb(widget):
    widget.place_forget()
    createdb()

btn_operatedb = tk.Button(window,text = "データベースの新規登録", command = lambda:run_operatedb(top_page))
btn_operatedb.place(x=280, y=150)

#作成済みテーブルに値を挿入する
def run_operatedb(widget):
    widget.place_forget()
    operateTop_page = tk.Canvas(width=800, height=800)
    operateTop_page.place(x=0, y=0) # キャンバス
    operateTop_label = tk.Label(window, text = "値入力するデータベースを選択してください", font = ("Helvetica", 10))
    operateTop_label.place(x=225, y=10)


btn_updatedb = tk.Button(window,text = "作成済みデータベースの更新", command = lambda:run_updatedb(top_page))
btn_updatedb.place(x=460, y=150)


#作成済みデータベースを操作する
def run_updatedb(widget):
    widget.place_forget()
    files = glob.glob("./database/*.db")
    for file in files:
        file[11:]
    
    updateTop_page = tk.Canvas(width=800, height=800)
    updateTop_page.place(x=0, y=0) # キャンバス
    updateTop_label = tk.Label(window, text = "操作するデータベースを選択してください", font = ("Helvetica", 10))
    updateTop_label.place(x=225, y=10)







window.mainloop()













# DBを作成する（既に作成されていたらこのDBに接続する
dbname ="./database/students.db"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()

conn.commit()












