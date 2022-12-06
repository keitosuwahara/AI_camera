import sqlite3
import datetime
import tkinter as tk
import tkinter.messagebox as tmsg


def now():#現在時刻を出す関数
    dt_now = datetime.datetime.now()#現在時刻
    return dt_now.strftime('%H時%M分')


#DBの更新をするプログラムです
"""
tkinterでdb内の閲覧や情報の更新ができるようにする
"""


root = tk.Tk()
root.geometry("800x700")
root.title("初期設定")


#学籍番号を入力するテキストボックスの処理
id_label = tk.Label(root, text = "学籍番号を入力してください", font = ("Helvetica", 10))
id_label.place(x=290, y=10)
id_value = tk.Entry(width=20)
id_value.place(x=290, y=30)


#名前を入力するテキストボックスの処理
name_label = tk.Label(root, text = "名前を入力してください", font = ("Helvetica", 10))
name_label.place(x=290, y=100)
name_value =  tk.Entry(width=20)
name_value.place(x=290, y=120)

#後々dbに新規格納する値を格納するリスト
inserts = []

#ボタンクリック時の処理
def btn_click():
    #入力された学籍番号を取得
    global id
    id = id_value.get()

    #入力された名前を取得
    global name
    name = name_value.get()

    #dbに値を入れるリストにidとnameを格納
    inserts.append((int(id),str(name),0,0,0))

    #ウィンドウを閉じる
    root.quit()

    #確認メッセージ
    tmsg.showinfo("確認",f"学籍番号:「{id}」と名前:「{name}」がデータベースに登録されました")


#ボタン作成
btn = tk.Button(root, text = "データベースに新規追加", font = ("Helvetica", 14), command = btn_click)
btn.place(x=290, y=150)


root.mainloop()













# DBを作成する（既に作成されていたらこのDBに接続する
dbname ="./database/students.db"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()

conn.commit()












