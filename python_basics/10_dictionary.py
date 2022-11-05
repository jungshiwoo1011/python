sajeon = {"apple" : "사과", "friend" : "친구", "aori" : "사과"}

print(sajeon["apple"])
print(sajeon["aori"])
print(sajeon.keys())
print(sajeon.values())
print(sajeon.items())
print("apple" in sajeon)
print("pear" in sajeon)

naver = {"jungshiwoo" : ["남자", "양일중", "브롤갓", "자전거"]}

if "jeongsiu" in naver:
    print(naver["jeongsiu"])
else:
    print("요청하신 찐따는 없어요 ㅋㅋㅋㅋㅋ")

naver["codingssam"] = ["남자", "코드플래이", "자가용"]
print(naver)


print(naver)

sajeon.update(naver)
print(sajeon)
print(naver)
