import MeCab
#-dと-uのパスは家と学校とは同じにする
tagger = MeCab.Tagger('-d "C:/Program Files (x86)/MeCab/dic/ipadic" -u "C:/Program Files (x86)/MeCab/mecabfolder/userdic/NEologd.dic"')
tagger2= MeCab.Tagger('-Owakati -d "C:/Program Files (x86)/MeCab/dic/ipadic" -u "C:/Program Files (x86)/MeCab/mecabfolder/userdic/NEologd.dic"')
#result = tagger.parse("私が一番好きな漫画は、進撃の巨人とGANTZです。")
result = tagger.parse("横浜システム工学院専門学校")
result2 = tagger2.parse("横浜システム工学院専門学校")
print(result)
print(result2)
#