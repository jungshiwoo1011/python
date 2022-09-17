result = 0
input_data = 0
while True:
    input_data = input("궁금하면 말해 새꺄 : ")
    if "+" in input_data:
         result = int(input_data.split("+")[0]) + int(input_data.split("+")[1])
    elif "-" in input_data:
        result = int(input_data.split("-")[0]) - int(input_data.split("-")[1])
    elif "*" in input_data:
        result = int(input_data.split("*")[0]) * int(input_data.split("*")[1])
    elif "/" in input_data:
        result = int(input_data.split("/")[0]) / int(input_data.split("/")[1])
    elif "꺼져" in input_data:
        print("니 얼굴")
        break
    else:
        print("계산식 넣어 개XX야")
        continue
    print(f"{input_data} = {result}")