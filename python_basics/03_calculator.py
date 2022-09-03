number_a = 0
symbol = 0
number_b = 0
result = 0
input_data = 0

number_a = int(input("숫자 A를 입력하시오 : "))
symbol = input("+, -, *, / 중 하나를 입력하시오: ")
number_b = int(input("숫자 B를 입력하시오 : "))

if symbol == "+":
    result = number_a + number_b
elif symbol == "-":
    result = number_a + number_b
elif symbol == "*":
    result = number_a + number_b
elif symbol == "/":
    result = number_a + number_b

result = number_a + number_b
result = number_a - number_b
result = number_a * number_b
result = number_a / number_b

print(f"{number_a} {symbol} {number_b} = {result}")