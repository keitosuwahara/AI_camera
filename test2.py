#日本語を英語にして変数化する
import pykakasi

kakasi = pykakasi.kakasi() # インスタンスの作成
kakasi.setMode('H', 'a') # ひらがなをローマ字に変換するように設定
kakasi.setMode('K', 'a') # カタカナをローマ字に変換するように設定
kakasi.setMode('J', 'a') # 漢字をローマ字に変換するように設定
conversion = kakasi.getConverter() # 上記モード設定の適用


keys = ['学籍番号', '名前', '出席', '遅刻', '早退']
vars = []

for key in keys:
    vars.append(conversion.do(key)+"s") # keyをローマ字に変換する処理
print(vars)

for var in vars:
    exec(var)
namaes=1
print(namaes)

