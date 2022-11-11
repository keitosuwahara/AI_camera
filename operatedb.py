import sqlite3
from flask import Flask, render_template, request

#作成した出欠席表をwebに表示とDBの更新をするプログラムです


# DBを作成する（既に作成されていたらこのDBに接続する
dbname ="./database/students.db"
conn = sqlite3.connect(dbname)
#SQLiteを操作するためのカーソル,コントローラー
cur = conn.cursor()
#update用のSQL
update_sql = 'UPDATE students SET name="志村燿平" WHERE studentID=186758'
# データ更新
cur.execute(update_sql)
cur.execute('UPDATE students SET studentID= 186758 WHERE name="志村燿平"')
cur.execute('UPDATE students SET attendance=1 WHERE name="志村燿平"')

#データベース内の表示
info = []
records = cur.execute("SELECT * FROM students")
for record in records:
    info.append(list(record))
#print(info)
# コミットしないと登録が反映されない
conn.commit()


app = Flask(__name__)

#トップページ
@app.route("/", methods=["GET","POST"])
def top():
    for users in info:
        for id in list(users):
            if str(id).isdigit() == True and len(str(id)) > 5:
                print(id)
    return render_template("/displaydb.html",id=id)


if __name__ == "__main__":
    app.run(debug=True)













