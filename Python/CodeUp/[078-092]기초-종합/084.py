""" 빛 섞어 색 만들기
    빨강 초록 파랑 빛을 섞어 여러 가지 빛의 색을 만들어 내려고 한다.
    빨강 초록 파랑 각각의 빛의 개수가 주어질 때
    주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합과 총 가짓 수를 계산해보자.
    입력 : 0~128 공백을 사이에 두고 입력
    출력 : 0 0 0 , 0 0 1, 0 1 0 .... 개수"""

r, g, b = map(int, input("input number : ").split(" "))
count=0

for i in range(r) :
    for j in range(g) :
        for k in range (b) :
            print(i, j, k)
            count += 1

print("%d개" %count)