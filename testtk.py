import sqlite3
import tkinter as tk
import tkinter.messagebox as tmsg

#db新規作成名前定義プログラムのプロトタイプ
def_name = tk.Tk()
def_name.geometry("450x200")
def_name.title("データベース新規作成")


#新規DBの名前を入力するテキストボックスの処理
dbname_label = tk.Label(def_name, text = "新規作成するデータベースの名前を入力してください", font = ("Helvetica", 10))
dbname_label.place(x=60, y=10)
dbname_value = tk.Entry(width=20)
dbname_value.place(x=150, y=30)



#ボタンクリック時の処理
def btn_click():
    #入力されたデータベース名を取得
    global dbname
    dbname = dbname_value.get()

    #ウィンドウを閉じる
    def_name.quit()
    #確認メッセージ
    #tmsg.showinfo("確認",f"学籍番号:「{id}」と名前:「{name}」がデータベースに登録されました")


#ボタン作成
btn_name = tk.Button(def_name, text = "次へ", font = ("Helvetica", 14), command = btn_click)
btn_name.place(x=180, y=100)


def_name.mainloop()

#次のキーを決める段階のプログラム
if def_name.quit() == None:
    def_prikey = tk.Tk()
    def_prikey.geometry("450x200")
    def_prikey.title("主キー作成")
    
    #このページのラベルと主キーを決めるテキストボックスと数値か文字列か決めるラジオボタン
    prikey_label = tk.Label(def_prikey, text = f"データベース「{dbname}」の主キーの名前を入力してください", font = ("Helvetica", 10))
    prikey_label.place(x=60, y=10)
    prikey_value = tk.Entry(width=20)
    prikey_value.place(x=00, y=40)
    int_or_str_label = tk.Label(def_prikey, text = "それは数値か文字列かどちらですか？", font = ("Helvetica", 10))
    int_or_str_label.place(x=60, y=70)


    #ボタンクリック時の処理
def btn_click2():
    #入力された主キーを取得
    global prikeyname
    prikeyname = prikey_value.get()

    #ウィンドウを閉じる
    def_prikey.quit()
    #確認メッセージ
    #tmsg.showinfo("確認",f"学籍番号:「{id}」と名前:「{name}」がデータベースに登録されました")


#ボタン作成
btn_prikey = tk.Button(def_prikey, text = "次へ", font = ("Helvetica", 14), command = btn_click2)
btn_prikey.place(x=180, y=150)



def_prikey.mainloop()
print(prikeyname)










inserts = []
#testテーブルのパス
stdbname = "./database/test.db"

# DBを作成する（既に作成されていたらこのDBに接続する
conn = sqlite3.connect(stdbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()
#ここでテーブルが存在してたらいったん削除する
drop_sttable = '''drop table if exists test'''
cur.execute(drop_sttable)
#テーブルの作成
cur.execute(
    "CREATE TABLE IF NOT EXISTS test(学籍番号 INTEGER PRIMARY KEY , 名前 STRING, 出席 INTEGER, 遅刻 INTEGER, 早退 INTEGER)"  
)#                                                                   出席時=1 欠席時=0                             

# 複数データ登録
cur.executemany("INSERT INTO test values(?,?,?,?,?)",inserts)#insertsはさっき入力した値を格納したリスト

# コミットしないと登録が反映されない
conn.commit()


#追加する機能  1 テーブルが存在してても削除せずに情報を追加する機能  2 学籍番号が重複してたらエラーを出して何もしない機能


















