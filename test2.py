import MeCab

dic_path='-d "C:/Program Files (x86)/MeCab/dic/ipadic" -u "C:/Program Files (x86)/MeCab/mecabfolder/userdic/NEologd.dic"'
inwakati_dic='-Owakati -d "C:/Program Files (x86)/MeCab/dic/ipadic" -u "C:/Program Files (x86)/MeCab/mecabfolder/userdic/NEologd.dic"'
text = ''
text2="Pythonやpythonやjava,Java,C,C++"
mecab = MeCab.Tagger(dic_path)
mecab2 = MeCab.Tagger(inwakati_dic)
nodes = mecab.parseToNode(text2)

#大文字を小文字に変換する
def lower_text(text):
    return text.lower()

#textのうち名詞動詞形容詞のみ抜き出し大文字を小文字にする
while nodes:
    if nodes.feature.split(",")[0] in ["名詞" , "動詞" , "形容詞"]:
        print(lower_text(nodes.surface))
        print(lower_text(nodes.feature))
    nodes = nodes.next





print(mecab2.parse(text2))
