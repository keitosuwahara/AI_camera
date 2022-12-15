import os 
import datetime

date = datetime.datetime.now()
year = date.year
month = date.month

"""
for i in range(0, 12):
    os.makedirs(f"./database/xl_dir/{year}_{month}", exist_ok=True)
    month -= 1
"""

dir_path = './database/xl_dir'
files = os.listdir(dir_path)  # ディレクトリ内のファイルリストを取得
files.sort()  # ファイルリストを昇順に並び替え
print(files)

