import os
from pathlib import Path

def remove_latestdb():
    p = Path("./database")
    files = list(p.glob("*"))
    file_updates = {file_path: os.stat(file_path).st_mtime for file_path in files}

    newst_file_path = max(file_updates, key=file_updates.get)
    os.remove(newst_file_path)

#最新ファイルのみ抜き出す