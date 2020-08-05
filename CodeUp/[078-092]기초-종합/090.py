""" 등비수열 만들기
    입력 : 시작값(a), 등비(r), 몇 번째(n) : 2 3 7
    출력 : n번째 수 출력 1458 """

a, r, n = map(int, input().split())

i=a
count=0
list = []

while count<n :
    list.append(i)
    i *= r
    count += 1
print(list[-1])