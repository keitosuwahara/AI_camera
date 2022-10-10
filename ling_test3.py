import MeCab

tagger1 = MeCab.Tagger()
dicdir = '-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-unidic-neologd'
tagger2 = MeCab.Tagger(dicdir)

sample_txt = '鬼滅の刃もいいけれど、約束のネバーランドもね'
print(tagger1.parse(sample_txt))
print(tagger2.parse(sample_txt))