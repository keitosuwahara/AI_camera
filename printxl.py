import openpyxl as xl
import sqlite3
import datetime

#アイデア
    #西暦と月日+名前で以前の出席を残す
    #月ごとのフォルダを自動で作り一年以上たったフォルダから消していく
db="students"

#db内の情報をエクセルに転記するプログラム
def printxl():
    dbname =f"./database/{db}.db"
    conn = sqlite3.connect(dbname)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()
    #データベース内の表示
    info = []#仮でデータを入れておく##二次元配列にする→[[],[],[],[],[]]
    keys = []
    stds = []

    #選択したDBのそれぞれの行をリストで取り出す
    records = cur.execute(f"SELECT * FROM {db}")
    for record in records:
        info.append(list(record))
    print(info)

    #キーの取得
    for desc in cur.description:
        keys.append(desc[0])

    conn.commit()


#↓エクセルの操作

    wb = xl.Workbook()
    ws = wb.worksheets[0]

    today = datetime.date.today()#今日の日付

    ws.cell(row = 1, column = 1, value = str(today)+"時点")#日付けの転記

    for i in range(0,len(keys)):#キーのみを転記する
        ws.cell(row = 1, column = i+2, value = keys[i])
    
    tpm = []
    datas = []#順番通りのリストを作る→[[DBの0番目のみ],[DBの1番目のみ],[DBの2番目のみ]]

    for i in range(0,len(info)):#リスト内リストの数
        for j in range(0,len(info)):#リスト内リストの要素数
            tpm.append(info[i][j])
    
    
    

    
    wb.save(f'./database/xl_dir/{today}.xlsx')


if __name__ == "__main__":
    printxl()





