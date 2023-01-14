def samhaengsi():
    name = ""
    name3 = []
    name_in = ""
    name = input("삼행시 지을 세글자 넣으시오 : ")

    for word in name:  
        name_in = input(f"{word} : ")
        while True:
            if word == name_in[0]:
                name3.append(name_in)
                break
            else:
                print("첫글자 안맞음. 다시.")
    print("*" * 50)
    print(f"{name} 이라는 단어로 삼행시 지어봄")
    for n in range(len(name)):
        print(f"{name[n]} : {name3[n]}")
    print("*" * 50)
    return name3

f = open("event.txt", "a", encoding = "UTF-8")
for word in samhaengsi():
    f.write(word + "\n")
f.close()
