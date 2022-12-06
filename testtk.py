import tkinter as tk
import tkinter.messagebox as tmsg
import glob
import sqlite3

db_list = []
files = glob.glob("./database/*.db")
for file in files:
    db_list.append(file[11:])


window = tk.Tk()
window.geometry("700x250")
window.title("データベース設定")


list_var = tk.StringVar(value=db_list)
listbox = tk.Listbox(window, height=5, listvariable=list_var)
listbox.bind('<<ListboxSelect>>', lambda e: select_list())
listbox.pack()

#ここでdbを選択する処理
def select_list():
    selected_index = listbox.curselection()
    global selected_module
    selected_module = listbox.get(selected_index)
    print(selected_module)


window.mainloop()


# DBを作成する（既に作成されていたらこのDBに接続する
dbname =f"./database/{selected_module}"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()
info = []
records = cur.execute(f"SELECT * FROM {selected_module[:-3]}")
for record in records:
    info.append(list(record))
print(info+"info")

# コミットしないと登録が反映されない
conn.commit()

conn.commit()



