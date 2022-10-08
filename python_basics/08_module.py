from msilib.schema import MsiAssemblyName
from random import random


import random
from split_04 import *
from lotto_06 import lotto1
import fortuneteller_07 as ft

elect = 0

running = True
while running:
    select = int(input('''마! 반갑다 뭐해줄까?
    1. 계산기 2. 로또번호 추첨기   3. 미래배우자 알리미 4. 끝

    (위에 앱 중 하나 선택해라 마!) : '''))

    if select == 4:
        break
    elif select == 2:
        lotto1()
    elif select == 1:
        ft.future()
    elif select == 1:
        print(myname)
        calculater()

print("마 좋은 하루 되라이")
