import openpyxl as xl
import sqlite3
import datetime
import os
import shutil

#アイデア
    #西暦と月日+名前で以前の出席を残す
    #月ごとのフォルダを自動で作り一年以上たったフォルダから消していく


#db内の情報をエクセルに転記するプログラム
def printxl(db):
    dbname =f"./database/{db}.db"
    conn = sqlite3.connect(dbname)
    #SQLiteを操作するためのカーソル,コントローラー
    cur = conn.cursor()
    #データベース内の表示
    info = []#仮でデータを入れておく##二次元配列にする→[[],[],[],[],[]]
    keys = []#キーを格納するリスト


    #選択したDBのそれぞれの行をリストで取り出す
    records = cur.execute(f"SELECT * FROM {db}")
    for record in records:
        info.append(list(record))
    #print(info)

    #キーの取得
    for desc in cur.description:
        keys.append(desc[0])

    conn.commit()

#↓エクセルの操作

    wb = xl.Workbook()
    ws = wb.worksheets[0]

    today = datetime.date.today()#今日の日付

    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minutes = date.minute
    sec = date.second

    ws.cell(row = 1, column = 1, value = str(year)+"年")#西暦の転記
    ws.cell(row = 2, column = 1, value = str(month)+"月"+str(day)+"日")#月日の転記
    ws.cell(row = 3, column = 1, value = str(hour)+"時"+str(minutes)+"分")#時分の転記
    ws.cell(row = 4, column = 1, value = str(sec)+"秒時点")#秒の転記
    ws.cell(row = 5, column = 1, value = "DB名")
    ws.cell(row = 6, column = 1, value = db)#データベース名の転記
    

    
    
    tpm = []#datasに格納するために成形したリストを一時的に格納する
    datas = []#順番通りのリストを作る→[[DBの0番目のみ],[DBの1番目のみ],[DBの2番目のみ]]


    for i in range(0,len(info)):#リスト内リストの数
        for j in range(0,len(info[0])):#リスト内リストの要素数
            tpm.append(info[i][j])
    #print(tpm)[190721, '岩橋大地', 1, 0, 0, 200284, '桃崎奏斗', 1, 0, 0, 210103, '諏訪原慶斗', 1, 0, 1, 435755, '高田悠', 1, 1, 1, 454545, '志村', 1, 1, 1, 557855, '黒野怜奈', 1, 1, 1, 846556, 'トゴーフーバダムツェレン', 1, 1, 1]


    for iiii in range(0, len(info)-2):
        for iii in range(0, len(tpm), len(info[0])):
            datas.append(tpm[iii+iiii])#要素ごとに分けることには成功
    #print(datas)

    #datasを要素ごとの二次元配列にする関数(変換したいリスト, リスト内リスト数)
    def convert_1d_to_2d(datas, cols):
        return [datas[i:i + cols] for i in range(0, len(datas), cols)]

    stds = convert_1d_to_2d(datas, len(info))
    

    for index, key in enumerate(keys):#キーのみ転記する
        ws.cell(row=1, column=2+index, value=key)

    for ind, std in enumerate(stds):#キーに合った要素を転記する
        for i in range(0, len(std)):
            ws.cell(row=2+i, column=2+ind, value=std[i])
    
    os.makedirs(f"./database/xl_dir/{year}_{month}", exist_ok=True)
    wb.save(f'./database/xl_dir/{year}_{month}/{today}.xlsx')

    #2年前の出席シートを削除
    dir_path = './database/xl_dir'
    files = os.listdir(dir_path)  # ディレクトリ内のファイルリストを取得
    if len(files) >= 25:
        files.sort()  # ファイルリストを昇順に並び替え
        shutil.copytree(f'./database/xl_dir/{files[0]}', f'./static/ゴミ箱/xl_dirs/{files[0]}')#削除する前にゴミ箱に移す
        shutil.rmtree(f"./database/xl_dir/{files[0]}")# 先頭のファイル(=一番古いファイル名)を削除

    print("printxl関数が正常に実行されExcelに転記しました")

    #もう少し確実性のあるフォルダの日時の遡り方を考える


if __name__ == "__main__":
    printxl("students")





