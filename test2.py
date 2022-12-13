#辞書にリストをぶち込むプログラム
"""
info =[]
keys = ["学籍番号","名前","出席","遅刻","早退"]
stds = []
id = [21121,72849,19890,59821,98239]
name = ["wer","as","sas","fd","fghd"]
att = ["1","1","1","1","1"]
late = ["32","43","54","54","23"]
earl = ["65","45","65","76","87"]

for stds in zip(id, name, att, late, earl):
    info.append(list(stds))
print(info)


stdlist = dict(zip(keys,info)) #keyとinfoをまとめて辞書型にする
print("________________________________")
print(stdlist)
print("______________________________")
for i in range(0,len(keys)):
    print(stdlist[keys[i]])
"""
info =[[190721, '岩橋大地', 1, 0, 0], [200284, '桃崎奏斗', 1, 0, 0], [210103, '諏訪原慶斗', 1, 0, 1], [435755, '高田悠', 1, 1, 1], [454545, '志村', 1, 1, 1], [557855, '黒野怜奈', 1, 1, 1], [846556, 'トゴーフーバダムツェレン', 1, 1, 1]]


tpm = []
datas = []#順番通りのリストを作る→[[DBの0番目のみ],[DBの1番目のみ],[DBの2番目のみ]]


for i in range(0,len(info)):#リスト内リストの数
    for j in range(0,len(info[0])):#リスト内リストの要素数
        tpm.append(info[i][j])

#print(tpm)[190721, '岩橋大地', 1, 0, 0, 200284, '桃崎奏斗', 1, 0, 0, 210103, '諏訪原慶斗', 1, 0, 1, 435755, '高田悠', 1, 1, 1, 454545, '志村', 1, 1, 1, 557855, '黒野怜奈', 1, 1, 1, 846556, 'トゴーフーバダムツェレン', 1, 1, 1]


#for iiii in range(0, len(info)):
    #print(iiii)
for iii in range(0, len(tpm), len(info[0])):
    print(iii)#最終的な数値が34にならなくてはいけない
#print(datas)

