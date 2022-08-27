ban_dict = ["개새끼", "시발", "병신", "ㅂㅅ", "ㅅㅂ"]
status = True

print("챗봇 시작한다")
while status:
    bad_words = 0
    chat = input("말해 : ")
    for word in ban_dict:
        if word in chat:
            bad_words += 1
    if chat == "꺼져":
        status = False
    if bad_words == 0:
        print("야 맞았다")
    else:
        print("야이 새까 ㅈㄹ하고 자빠졌네")

print("어~ 들어가")
   