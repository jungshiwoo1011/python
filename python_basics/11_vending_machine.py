drinks = {"갈아만든 사과" : [4500, 10], "콜라" : [2000, 10],  "환타" : [3000, 10], "박카스" : [1500, 10], "레드볼" : [4000, 10], "칵테일" : [30000, 10]}
money = 0
customer = True
select = 0
choice = 0
income = 0
name = []
price = []
price_stock = []
stock = []
name = list(drinks.keys()) 
price_stock = list(drinks.values())
for i in price_stock:
    price.append(i[0])
    price.append(i[1]) 

def display():
    print("*" * 22)
    print("*" * 5, "독약자판기", "*" * 5) 
    for j in range(len(name)):
        print(f"{name[0]} - {price[0]}원")
    print(name)
    print(price)
    print("*" * 22)
    print(f"잔액 : {money}")
    print("*" * 22)

while True:
    customer = True
    while customer:
        display()
        select = int(input("1. 돈넣기 / 2.물건사기 / 3.나가기 : "))

        if select == 1:
            money = int(input("금액입력 : "))
            continue
        elif select == 2:
            display()
            choice = name.index(input("음료선택 : "))
            if money >= price[choice]:
                if stock[choice] > 0:
                    print(f"<{name[choice]}> 음료구매 완료 ")
                    income += price[choice]
                    money = money - price[choice]
                    stock[choice] -= 1
                else:
                    print(f"{name[choice]} 음료는 품절입니다")
                    break
            else:
                print("잔액부족")
                break
        elif select == 3:
            print("독약 자판기 이용 감사")
            if money > 0:
                print(f"환불금액 : {money}")
                money = 0
                customer = False
        elif select == 1470:
            print(f"오늘의 수익 : {income}")
            print("+ + + + 음료별 판매 현황 + + + +")
            for x in range(len(name)):
                print(f"{name[x]} = {10 - stock[x]}개 판매")
            input("부좌 돼롸~ 수ㅖ꺄")
        else:
            print("잘못 눌렀다 새꺄")
