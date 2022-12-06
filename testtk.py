import tkinter as tk
import tkinter.messagebox as tmsg
import sqlite3

#データベースを新しく作る時のプログラム

# ウィンドウの作成                                                              
window = tk.Tk()
window.geometry("800x500")
window.title("データベース新規作成")

# 遷移前の画面の作成                                                            
def_newdb = tk.Canvas(width=800, height=800)
def_newdb.place(x=0, y=0) # キャンバス

#新規DBの名前を入力するテキストボックスの処理
dbname_label = tk.Label(window, text = "新規作成するデータベースの名前を入力してください", font = ("Helvetica", 10))
dbname_label.place(x=80, y=10)
dbname_value = tk.Entry(width=20)
dbname_value.place(x=175, y=30)

#新規主キーの名前を入力するテキストボックスの処理
prikey_label = tk.Label(window, text = "主キーを入力してください", font = ("Helvetica", 10))
prikey_label.place(x=80, y=60)

prikey_value = tk.Entry(width=20)
prikey_value.place(x=175, y=80)

intorstr_label =tk.Label(window, text = "数値か文字列か選択してください", font = ("Helvetica", 10))
intorstr_label.place(x=300, y=50)

# チェック有無変数
global prikey_var
prikey_var = tk.IntVar()
# value=0のラジオボタンにチェックを入れる
prikey_var.set(0)

#数値か文字列か決めるラジオボタン
prikey_int_or = tk.Radiobutton(window, value = 0, variable = prikey_var, text = "数値")
prikey_int_or.place(x=300, y=80)

prikey_str_or = tk.Radiobutton(window, value = 1, variable = prikey_var, text = "文字列")
prikey_str_or.place(x=350, y=80)


#新規サブキー1
subkey1_label = tk.Label(window, text = "サブキー1を入力してください", font = ("Helvetica", 10))
subkey1_label.place(x=80, y=110)
subkey1_value = tk.Entry(width=20)
subkey1_value.place(x=175, y=130)

# チェック有無変数
global subkey1_var
subkey1_var = tk.IntVar()
# value=0のラジオボタンにチェックを入れる
subkey1_var.set(0)
#数値か文字列か決めるラジオボタン

subkey1_int_or = tk.Radiobutton(window, value = 0, variable = subkey1_var, text = "数値")
subkey1_int_or.place(x=300, y=130)

subkey1_str_or = tk.Radiobutton(window, value = 1, variable = subkey1_var, text = "文字列")
subkey1_str_or.place(x=350, y=130)

#新規サブキー2
subkey2_label = tk.Label(window, text = "サブキー2を入力してください", font = ("Helvetica", 10))
subkey2_label.place(x=80, y=160)
subkey2_value = tk.Entry(width=20)
subkey2_value.place(x=175, y=180)

# チェック有無変数
global subkey2_var
subkey2_var = tk.IntVar()
# value=0のラジオボタンにチェックを入れる
subkey2_var.set(0)
#数値か文字列か決めるラジオボタン

subkey2_int_or = tk.Radiobutton(window, value = 0, variable = subkey2_var, text = "数値")
subkey2_int_or.place(x=300, y=180)

subkey2_str_or = tk.Radiobutton(window, value = 1, variable = subkey2_var, text = "文字列")
subkey2_str_or.place(x=350, y=180)

#新規サブキー3
subkey3_label = tk.Label(window, text = "サブキー3を入力してください", font = ("Helvetica", 10))
subkey3_label.place(x=80, y=210)
subkey3_value = tk.Entry(width=20)
subkey3_value.place(x=175, y=230)

# チェック有無変数
global subkey3_var
subkey3_var = tk.IntVar()
# value=0のラジオボタンにチェックを入れる
subkey3_var.set(0)
#数値か文字列か決めるラジオボタン

subkey3_int_or = tk.Radiobutton(window, value = 0, variable = subkey3_var, text = "数値")
subkey3_int_or.place(x=300, y=230)

subkey3_str_or = tk.Radiobutton(window, value = 1, variable = subkey3_var, text = "文字列")
subkey3_str_or.place(x=350, y=230)

#新規サブキー4
subkey4_label = tk.Label(window, text = "サブキー4を入力してください", font = ("Helvetica", 10))
subkey4_label.place(x=80, y=260)
subkey4_value = tk.Entry(width=20)
subkey4_value.place(x=175, y=280)

# チェック有無変数
global subkey4_var
subkey4_var = tk.IntVar()
# value=0のラジオボタンにチェックを入れる
subkey4_var.set(0)
#数値か文字列か決めるラジオボタン

subkey4_int_or = tk.Radiobutton(window, value = 0, variable = subkey4_var, text = "数値")
subkey4_int_or.place(x=300, y=280)

subkey4_str_or = tk.Radiobutton(window, value = 1, variable = subkey4_var, text = "文字列")
subkey4_str_or.place(x=350, y=280)


#次のページへの処理
def_new_db_btn = tk.Button(window,text = "次へ", command = lambda:btn_click_to_confirm(def_newdb))
def_new_db_btn.place(x=175, y=340)


def btn_click_to_confirm(widget):
    widget.place_forget() # def_dewdbを隠す

    #入力されたデータベース名を取得
    global dbname
    dbname = dbname_value.get()

    #入力された主キーを取得
    global prikey
    prikey = prikey_value.get()

    #入力されたサブキー1を取得
    global subkey1
    subkey1 = subkey1_value.get()

    #入力されたサブキー2を取得
    global subkey2
    subkey2 = subkey2_value.get()

    #入力されたサブキー3を取得
    global subkey3
    subkey3 = subkey3_value.get()

    #入力されたサブキー4を取得
    global subkey4
    subkey4 = subkey4_value.get()

    #新しい画面を作る
    global def_confirm
    def_confirm = tk.Canvas(width=800, height=800)
    def_confirm.place(x=0, y=0)

    #新規作成するDBの確認
    p = tk.Label(def_confirm, text="この内容で新規作成します", font = ("Helvetica", 9))
    p.place(x=300, y=10)
    preview = tk.Label(def_confirm, text=f"DB名:{dbname} ,主キー:{prikey} ,サブキー1:{subkey1} ,サブキー2:{subkey2} ,サブキー3:{subkey3} ,サブキー4:{subkey4}", font = ("Helvetica", 9))
    preview.place(x=10, y=100)


    #次のページへの処理
    def_container_btn = tk.Button(window,text = "確定", command = lambda:quit(def_newdb))
    def_container_btn.place(x=175, y=340)


def quit(widget):
    widget.quit()



window.mainloop()


try:

    #今まで入力した情報でDBを新規作成する
    new_db = f"./database/{dbname}.db"

    # DBを作成する（既に作成されていたらこのDBに接続する
    conn = sqlite3.connect(new_db)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()
    #ここでテーブルが存在してたらいったん削除する
    drop_sttable = f'drop table if exists {dbname}'
    cur.execute(drop_sttable)
    #テーブルの作成
    cur.execute(f"CREATE TABLE IF NOT EXISTS {dbname}({prikey} INTEGER PRIMARY KEY , {subkey1} STRING, {subkey2} INTEGER, {subkey3} INTEGER, {subkey4} INTEGER)")  


    # コミットしないと登録が反映されない
    conn.commit()

except sqlite3.OperationalError:
    tmsg.showinfo("エラー","重複しているキーがあるか数字など認められないキーを使っています")

