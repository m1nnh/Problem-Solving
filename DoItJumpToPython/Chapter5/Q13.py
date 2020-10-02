## random 모듈을 사용하여 로또 번호 (1~45 사이의 숫자 6개)를 생성해 보자 ( 단 중복된 숫자가 있으면 안됨 )

import random

list = []
check = 1

for i in range(0,6) :
    random_num = random.randint(1,45)
    if random_num not in list :
        list.append(random_num)

print(list)