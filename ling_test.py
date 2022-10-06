link="https://qiita.com/wf-yamaday/items/3ffdcc15a5878b279d61"
import spacy
from spacy import displacy
from IPython.core.display import display, HTML
# Languageクラス 変数名をnlpで宣言するのが一般的（spaCy推奨）
nlp: spacy.Language = spacy.load('ja_ginza')


# text を Doc クラスに変換する
text: str = '錦織圭選手はテニスが大好きです。'
doc: spacy.tokens.doc.Doc = nlp(text)

# Doc クラスは Token クラスのイテレーターになっている
#for token in doc:
 # print(token.text, type(token)) # token.text は日本語の形態素の単位

# 依存関係の可視化（jupyter=TrueとすることでNotebook上で表示できる）
displacy.render(doc, style="dep",options={"compact":True},  jupyter=True)
# エンティティの可視化
displacy.render(doc, style="ent", options={"compact":True},  jupyter=True)

"""
for ent in doc.ents:
    for token in ent:
        print(token.text, type(token))
"""

doc2=nlp('山田孝之は偉大な俳優なので演技をしてテレビに出演します。')
# noun_chunksでテキスト文に含まれる名詞句を取り出す
#for chunk in doc2.noun_chunks:
    #print(chunk.text, type(chunk))
"""
for token in doc2:
    if token.pos_ in ["NOUN", "PROPN"]:# NOUNが名詞、PROPNが固有名詞
        print(token.text," =",token.tag_, type(token))
"""
#コサイン類似度は0〜1までの値を取り、1に近いほど2つの文章が似ているという尺度になります。
print("doc1", doc.text)
print("doc2", doc2.text)

print("cos類似度:", doc.similarity(doc2))


text3 = '''
阪神がリーグ優勝を逃した。すでに勝利で試合を終えたヤクルトがマジック１としており、この試合に敗れた瞬間、ヤクルトの６年ぶりの優勝と阪神のＶ逸が決定。阪神にとって１６年ぶりの夢が、本拠地で散った。
ミスで無駄な点を与える、今季を象徴するような戦いぶりだった。二回１死一、二塁、木下拓の三ゴロで併殺コースは、二塁手・糸原が一塁へ悪送球する適時失策で先制点を献上した。
０－１の五回は無死から２番手・及川が、先頭・岡林をスライダーで空振り三振に仕留めたが、ワンバウンドした球を捕手・坂本が一塁ベンチ方向にそらし、振り逃げで出塁を許した。（記録は投手の暴投）この後、四球、安打で１死満塁として三番手・馬場に交代。馬場は２死後、大島に２点適時打を浴びた。
負けられない１戦。矢野監督は二回、２死一、三塁の好機に、先発の青柳に代打・小野寺を送る積極采配。結果は遊飛に終わった。決死のリレーも及川が３イニング目につかまった。今季最終戦だが、“第２先発”を任せられる他の先発陣をベンチにはスタンバイさせる策を取っていなかった。
打線も沈黙した。糸原が猛打賞と気を吐いたが、その他は大山の１安打のみ。計４安打完封負けで今季を終えた。
今季は佐藤輝、中野、伊藤将のルーキートリオが大活躍。マルテ、スアレスら外国人も機能し、５月まで破竹の勢いで白星を重ねた。一時は２位に最大７ゲーム差をつけ、独走の雰囲気も漂った。
だが、打線の勢いが低下し、夏場に失速。８月末に首位の座を奪われた。１０月は投手陣の奮闘もあり、ヤクルトに負けじと貯金を増やした。最後までＶへの執念もみせたが、わずかに頂点へ届かなかった。
矢野監督は試合後の挨拶で「今日のこの最後の試合、こういう試合で勝ちきれる、もっともっといいチームに、もっともっと強いチームになっていけるよう。新たなスタートとして、この悔しさを持って戦っていきます」と今後に向けて語った。
'''

#doc3の
doc3=nlp(text3)

result=[]
for chunk in doc3.noun_chunks:
    result.append((chunk.text, chunk.similarity(doc3)))









































