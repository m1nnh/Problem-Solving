## 정수 1개가 입력 되었을 때, 음/양 과 짝/홀 출력

var = int(input())

if var < 0 :
    if var % 2 == 0 :
        print("minus, even")
    else :
        print("minus, odd")
elif var > 0 :
    if var % 2 == 0 :
        print("plus, even")
    else :
        print("plus, odd")
else :
    print("0")
