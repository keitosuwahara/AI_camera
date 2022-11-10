inserts = [
        (435755,"高田悠",1),
        (557855,"黒野怜奈",1),
        (846556,"トゴーフーバダムツェレン",1),
        (454545,"志村",1),
        (210103,"諏訪原慶斗",1),
        (190721,"岩橋大地",1),
        (200284,"桃崎奏斗",1)
        ]

#5文字以上の数字のみ抜き出す
for insert in inserts:
    for student in list(insert):
        if str(student).isdigit() == True and len(str(student)) > 5:
            print(student)
            
#日本語とカタカナ、アルファベットの文字列を抜き出す
for insert in inserts:
    for student in list(insert):
        if str(student).isalpha():
                print(student)

#2文字以下の数字のみ抜き出す
for insert in inserts:
    for student in list(insert):
        if str(student).isdigit() == True and len(str(student)) < 2:
            print(student)
# info = "INSERT INTO Students values("
    # for i in range(len(inserts[0])):
    #     info += "?,"
    # info += ")"

    # print(info)    