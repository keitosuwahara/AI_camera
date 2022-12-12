import openpyxl as xl
import sqlite3
import pykakasi
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
    info = []
    keys = []
    records = cur.execute("SELECT * FROM students")
    for record in records:
        info.append(list(record))
    #キーの取得
    for desc in cur.description:
        keys.append(desc[0])

    conn.commit()

    stdlist = [dict(zip(keys,item)) for item in info]#keyとinfoをまとめて辞書型にする
    print(keys)

    wb = xl.Workbook()
    ws = wb.worksheets[0]

    today = datetime.date.today()#今日の日付

    ws.cell(row = 1, column = 1, value = str(today)+"時点")

    for i in range(0,5):#キーのみを転記する
        ws.cell(row = 1, column = i+2, value = keys[i])

    
    #キーをそれぞれローマ字にしてそれに合った変数にする
    kakasi = pykakasi.kakasi() # インスタンスの作成
    kakasi.setMode('H', 'a') # ひらがなをローマ字に変換するように設定
    kakasi.setMode('K', 'a') # カタカナをローマ字に変換するように設定
    kakasi.setMode('J', 'a') # 漢字をローマ字に変換するように設定
    conversion = kakasi.getConverter() # 上記モード設定の適用

    vars = []#ローマ字にした変数のリスト

    for key in keys:
        vars.append(conversion.do(key)+"s") # keyをローマ字に変換する処理
    print(vars)
    

    #それぞれの属性の空リストを作る
    for index, var in enumerate(vars):
        var = []
    
    
    """
    #それぞれの属性をリスト化
    for std in stdlist:
        ids.append(std["学籍番号"])
        names.append(std["名前"])
        attends.append(std["出席"])
        tikokus.append(std["遅刻"])
        soutais.append(std["早退"])
    
    

    #学籍番号の転記
    for index, id in enumerate(ids):
        ws.cell(row = index + 2, column = 2, value = id)
    #名前の転記
    for index, name in enumerate(names):
        ws.cell(row = index + 2, column = 3, value = name)
    #出席の転記
    for index, attend in enumerate(attends):
        ws.cell(row = index + 2, column = 4, value = attend)
    #遅刻の転記
    for index, tikoku in enumerate(tikokus):
        ws.cell(row = index + 2, column = 5, value = tikoku)
    #早退の転記
    for index, soutai in enumerate(soutais):
        ws.cell(row = index + 2, column = 6, value = soutai)

    """
    wb.save(f'./database/xl_dir/{today}.xlsx')


if __name__ == "__main__":
    printxl()





