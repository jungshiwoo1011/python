ban_dict = ["개새끼", "시발", "병신", "ㅂㅅ", "ㅅㅂ", "fuck"]
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
    if chat == "추가":
        add_word = input("추가할 금칙어 말해 ㅅㅂ새꺄")
        if add_word in ban_dict:
            print("{add_word} 단어 이미 사전에 있어~")
        else:
            ban_dict.append(add_word)
            print(f"{add_word} 단어가 금칙어 사전에 등록완료")
        continue
    if bad_words == 0:
        print("야 맞았다")
    else:
        print("야이 쉬파 새까 ㅈㄹ하고 자빠졌네")

print("어~ 들어가")
   