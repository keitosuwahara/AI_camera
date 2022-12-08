import tkinter as tk
import tkinter.messagebox as tmsg
import tkinter.ttk as ttk
import glob
import sqlite3

def show_db():
    #db一覧を取り出す
    db_list = []
    files = glob.glob("./database/*.db")
    for file in files:
        db_list.append(file[11:])

    window = tk.Tk()
    window.title("データベース選択")
    window.geometry("600x500")

    select_db_page = tk.Canvas(width=800, height=800)
    select_db_page.place(x=0, y=0) # キャンバス


    #str型で値を受け取る
    db_var = tk.StringVar()



    #ボタンが押された時の処理
    def push_btn_selectdb(widget):
        widget.place_forget()
        global db_value
        db_value = db_var.get()
        print(db_value[:-3])

        #dbない操作のページ
        dbvalue_page = tk.Canvas(width=800, height=800)
        dbvalue_page.place(x=0, y=0) # キャンバス

        dbname = f'./database/{db_value}'
        conn = sqlite3.connect(dbname)
        # SQLiteを操作するためのカーソルを作成
        cur = conn.cursor()
        # テーブルを選択
        cur.execute(f'select * from {db_value[:-3]}')
        # descを取得する
        descr = cur.description
        #空の配列を作り
        columns_lists = []
        #ループでカラム一覧のリストを作る
        for desc in descr:
            columns_lists.append(desc[0])
        print(columns_lists)
        #表の作成
        # 列の識別名を指定
        # Treeviewの生成
        tree = ttk.Treeview(dbvalue_page, columns=columns_lists)
        # 列の設定
        for c in columns_lists:
            tree.column('#0',width=0, stretch='no')
            tree.column(c, anchor='center', width=80)
            # 列の見出し設定
            tree.heading('#0',text='')
            tree.heading(c, text=c,anchor='center')



        # レコードがないと表示できないので一時的に入れる
        tree.insert(parent='', index='end', iid=0 ,values=(1, 'KAWASAKI',80))
        tree.insert(parent='', index='end', iid=1 ,values=(2,'SHIMIZU', 90))
        tree.insert(parent='', index='end', iid=2, values=(3,'TANAKA', 45))
        tree.insert(parent='', index='end', iid=3, values=(4,'OKABE', 60))
        tree.insert(parent='', index='end', iid=4, values=(5,'MIYAZAKI', 99))
        # ウィジェットの配置
        tree.pack(pady=10)







    for db in db_list:
        db_var.set(db)
        #数値か文字列か決めるラジオボタン
        db_radio = tk.Radiobutton(window, value = db, variable = db_var, text = db[:-3])
        db_radio.pack()


    #ボタンを作る
    btn_selectdb = tk.Button(text="決定", command=lambda:push_btn_selectdb(select_db_page))
    btn_selectdb.pack()

    window.mainloop()


"""
 # DBを作成する（既に作成されていたらこのDBに接続する
    dbname =f"./database/{db_value}"
    conn = sqlite3.connect(dbname)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()
    info = []
    records = cur.execute(f"SELECT * FROM {db_value[:-3]}")
    for record in records:
        info.append(list(record))


"""
if __name__ == "__main__":
    show_db()


