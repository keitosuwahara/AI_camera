import MeCab
import unidic
#やっと辞書を入れれた
tagger = MeCab.Tagger('-Owakati -d "C:/Program Files/MeCab/dic/ipadic" -u "C:/Program Files (x86)/MeCab/mecabfolder/userdic/mecab-user-dict-seed.dic"')
result = tagger.parse('私が最近見た映画は、約束のネバーランドでした、あと鬼滅の刃、呪術廻戦')
print(result)