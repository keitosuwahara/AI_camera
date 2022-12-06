import tkinter as tk
import sqlite3

#データベースを新しく作る時のプログラム

# ウィンドウの作成                                                              
window = tk.Tk()
window.geometry("1000x200")
window.title("データベース新規作成")

# 遷移前の画面の作成                                                            
def_dbname = tk.Canvas(width=800, height=800)
def_dbname.place(x=0, y=0) # キャンバス

#新規DBの名前を入力するテキストボックスの処理
dbname_label = tk.Label(window, text = "新規作成するデータベースの名前を入力してください", font = ("Helvetica", 10))
dbname_label.place(x=80, y=10)
dbname_value = tk.Entry(width=20)
dbname_value.place(x=175, y=30)


#主キーを決めるページへ遷移するボタン
def_dbname_btn = tk.Button(def_dbname, text=  "次へ", command = lambda:btn_click_to_prikey(def_dbname))                                                
def_dbname_btn.place(x=220, y=60)





#def_dbnameのボタンが押された時の時の処理
def btn_click_to_prikey(widget):
    widget.place_forget() # def_dbnameを隠す

    #入力されたデータベース名を取得
    global dbname
    dbname = dbname_value.get()

    #新しい画面を作る
    def_prikey = tk.Canvas(width=800, height=800)
    def_prikey.place(x=0, y=0)

    #このページのラベル
    prikey_label = tk.Label(def_prikey, text=f"データベース名:「{dbname}」の主キーを入力してください", font = ("Helvetica", 10))
    prikey_label.place(x=100, y=10)

    #入力したもののプレビュー
    p = tk.Label(def_prikey, text="プレビュー", font = ("Helvetica", 9))
    p.place(x=10, y=160)
    preview = tk.Label(def_prikey, text=f"DB名:{dbname}", font = ("Helvetica", 9))
    preview.place(x=10, y=180)

    #主キーを決めるテキストボックス
    global prikey_value
    prikey_value = tk.Entry(width=20)
    prikey_value.place(x=180, y=45)

    # チェック有無変数
    global prikey_var
    prikey_var = tk.IntVar()
    # value=0のラジオボタンにチェックを入れる
    prikey_var.set(0)

    #数値か文字列か決めるラジオボタン
    int_or_str_label = tk.Label(def_prikey, text = "それは数値か文字列かどちらですか？", font = ("Helvetica", 10))
    int_or_str_label.place(x=120, y=70)

    prikey_int_or = tk.Radiobutton(window, value = 0, variable = prikey_var, text = "数値")
    prikey_int_or.place(x=120, y=100)

    prikey_str_or = tk.Radiobutton(window, value = 1, variable = prikey_var, text = "文字列")
    prikey_str_or.place(x=280, y=100)


    #サブキー1を決めるページへ遷移するボタン
    def_prikey_btn = tk.Button(def_prikey,text = "次へ", command = lambda:btn_click_to_subkey1(def_prikey))
    def_prikey_btn.place(x=220, y=140)


#def_prikeyのボタンが押された時の時の処理
#サブキー1を決める処理
def btn_click_to_subkey1(widget):
    widget.place_forget() # def_prikeyを隠す

    #入力された主キーを取得
    global prikey
    prikey = prikey_value.get()

    #新しい画面を作る
    def_subkey1 = tk.Canvas(width=800, height=800)
    def_subkey1.place(x=0, y=0)

    #このページのラベル
    subkey1_label = tk.Label(def_subkey1, text=f"主キー:「{prikey}」のサブキー1を入力してください", font = ("Helvetica", 10))
    subkey1_label.place(x=100, y=10)

    #入力したもののプレビュー
    p = tk.Label(def_subkey1, text="プレビュー", font = ("Helvetica", 9))
    p.place(x=10, y=160)
    preview = tk.Label(def_subkey1, text=f"DB名:{dbname} ,主キー:{prikey}", font = ("Helvetica", 9))
    preview.place(x=10, y=180)

    #サブキー1を決めるテキストボックス
    global subkey1_value
    subkey1_value = tk.Entry(width=20)
    subkey1_value.place(x=180, y=45)

    # チェック有無変数
    global subkey1_var
    subkey1_var = tk.IntVar()
    # value=0のラジオボタンにチェックを入れる
    subkey1_var.set(0)

    #数値か文字列か決めるラジオボタン
    int_or_str_label = tk.Label(def_subkey1, text = "それは数値か文字列かどちらですか？", font = ("Helvetica", 10))
    int_or_str_label.place(x=120, y=70)

    subkey1_int_or = tk.Radiobutton(window, value = 0, variable = subkey1_var, text = "数値")
    subkey1_int_or.place(x=120, y=100)

    subkey1_str_or = tk.Radiobutton(window, value = 1, variable = subkey1_var, text = "文字列")
    subkey1_str_or.place(x=280, y=100)

    #サブキー2を決めるページへ遷移
    def_subkey1_btn = tk.Button(def_subkey1,text = "次へ", command = lambda:btn_click_to_subkey2(def_subkey1))
    def_subkey1_btn.place(x=220, y=140)


#サブキー2を決める処理
def btn_click_to_subkey2(widget):
    widget.place_forget() # def_subkey1を隠す

    #入力されたサブキー1を取得
    global subkey1
    subkey1 = subkey1_value.get()

    #新しい画面を作る
    def_subkey2 = tk.Canvas(width=800, height=800)
    def_subkey2.place(x=0, y=0)

    #このページのラベル
    subkey1_label = tk.Label(def_subkey2, text=f"主キー:「{prikey}」のサブキー2を入力してください", font = ("Helvetica", 10))
    subkey1_label.place(x=100, y=10)

    #入力したもののプレビュー
    p = tk.Label(def_subkey2, text="プレビュー", font = ("Helvetica", 9))
    p.place(x=10, y=160)
    preview = tk.Label(def_subkey2, text=f"DB名:{dbname} ,主キー:{prikey} ,サブキー1:{subkey1}", font = ("Helvetica", 9))
    preview.place(x=10, y=180)

    #サブキー2を決めるテキストボックス
    global subkey2_value
    subkey2_value = tk.Entry(width=20)
    subkey2_value.place(x=180, y=45)

    # チェック有無変数
    global subkey2_var
    subkey2_var = tk.IntVar()
    # value=0のラジオボタンにチェックを入れる
    subkey2_var.set(0)

    #数値か文字列か決めるラジオボタン
    int_or_str_label = tk.Label(def_subkey2, text = "それは数値か文字列かどちらですか？", font = ("Helvetica", 10))
    int_or_str_label.place(x=120, y=70)

    subkey2_int_or = tk.Radiobutton(window, value = 0, variable = subkey2_var, text = "数値")
    subkey2_int_or.place(x=120, y=100)

    subkey2_str_or = tk.Radiobutton(window, value = 1, variable = subkey2_var, text = "文字列")
    subkey2_str_or.place(x=280, y=100)

    #サブキー3を決めるページへ遷移
    def_subkey2_btn = tk.Button(def_subkey2, text = "次へ", command = lambda:btn_click_to_subkey3(def_subkey2))
    def_subkey2_btn.place(x=220, y=140)



#サブキー3を決める処理
def btn_click_to_subkey3(widget):
    widget.place_forget() # def_subkey2を隠す

    #入力されたサブキー2を取得
    global subkey2
    subkey2 = subkey2_value.get()

    #新しい画面を作る
    global def_subkey3
    def_subkey3 = tk.Canvas(width=800, height=800)
    def_subkey3.place(x=0, y=0)

    #このページのラベル
    subkey3_label = tk.Label(def_subkey3, text=f"主キー:「{prikey}」のサブキー3を入力してください", font = ("Helvetica", 10))
    subkey3_label.place(x=100, y=10)

    #入力したもののプレビュー
    p = tk.Label(def_subkey3, text="プレビュー", font = ("Helvetica", 9))
    p.place(x=10, y=160)
    preview = tk.Label(def_subkey3, text=f"DB名:{dbname} ,主キー:{prikey} ,サブキー1:{subkey1} ,サブキー2:{subkey2}", font = ("Helvetica", 9))
    preview.place(x=10, y=180)

    #サブキー3を決めるテキストボックス
    global subkey3_value
    subkey3_value = tk.Entry(width=20)
    subkey3_value.place(x=180, y=45)

    # チェック有無変数
    global subkey3_var
    subkey3_var = tk.IntVar()
    # value=0のラジオボタンにチェックを入れる
    subkey3_var.set(0)

    #数値か文字列か決めるラジオボタン
    int_or_str_label = tk.Label(def_subkey3, text = "それは数値か文字列かどちらですか？", font = ("Helvetica", 10))
    int_or_str_label.place(x=120, y=70)

    subkey3_int_or = tk.Radiobutton(window, value = 0, variable = subkey3_var, text = "数値")
    subkey3_int_or.place(x=120, y=100)

    subkey3_str_or = tk.Radiobutton(window, value = 1, variable = subkey3_var, text = "文字列")
    subkey3_str_or.place(x=280, y=100)

    def_subkey3_btn = tk.Button(def_subkey3, text = "次へ", command = lambda:btn_click_to_subkey4(def_subkey3))
    def_subkey3_btn.place(x=220, y=140)


#サブキー４を決める処理
def btn_click_to_subkey4(widget):
    widget.place_forget() # def_subkey2を隠す

    #入力されたサブキー3を取得
    global subkey3
    subkey3 = subkey3_value.get()

    #新しい画面を作る
    global def_subkey4
    def_subkey4 = tk.Canvas(width=800, height=800)
    def_subkey4.place(x=0, y=0)

    #このページのラベル
    subkey4_label = tk.Label(def_subkey4, text=f"主キー:「{prikey}」のサブキー4を入力してください", font = ("Helvetica", 10))
    subkey4_label.place(x=100, y=10)

    #入力したもののプレビュー
    p = tk.Label(def_subkey4, text="プレビュー", font = ("Helvetica", 9))
    p.place(x=10, y=160)
    preview = tk.Label(def_subkey4, text=f"DB名:{dbname} ,主キー:{prikey} ,サブキー1:{subkey1} ,サブキー2:{subkey2} ,サブキー3:{subkey3}", font = ("Helvetica", 9))
    preview.place(x=10, y=180)

    #サブキー4を決めるテキストボックス
    global subkey4_value
    subkey4_value = tk.Entry(width=20)
    subkey4_value.place(x=180, y=45)

    # チェック有無変数
    global subkey4_var
    subkey4_var = tk.IntVar()
    # value=0のラジオボタンにチェックを入れる
    subkey4_var.set(0)

    #数値か文字列か決めるラジオボタン
    int_or_str_label = tk.Label(def_subkey4, text = "それは数値か文字列かどちらですか？", font = ("Helvetica", 10))
    int_or_str_label.place(x=120, y=70)

    subkey4_int_or = tk.Radiobutton(window, value = 0, variable = subkey4_var, text = "数値")
    subkey4_int_or.place(x=120, y=100)

    subkey4_str_or = tk.Radiobutton(window, value = 1, variable = subkey4_var, text = "文字列")
    subkey4_str_or.place(x=280, y=100)

    def_subkey4_btn = tk.Button(def_subkey4, text = "完了", command = lambda:confirm(def_subkey4))
    def_subkey4_btn.place(x=220, y=140)



#最終確認
def confirm(widget):
    widget.place_forget() # def_subkey4を隠す

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


window.mainloop()



#今まで入力した情報でDBを新規作成する
new_insert = []

if prikey_var == 0:
    new_insert.append((int(prikey)))
    print("数値")
else:
    new_insert.append((str(prikey)))
    print("文字列")

print(f"DB名:{dbname} ,主キー:{prikey} ,サブキー1:{subkey1} ,サブキー2:{subkey2} ,サブキー3:{subkey3} ,サブキー4:{subkey4}")
