## 홍길동씨의 주민등록번호는 881120-1068234이다.
## 홍길동씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.

pin = "881120-1068234"
yyyymmdd = "19"+pin[0:2]+pin[2:4]+pin[4:6]
num = pin[8:]
print(yyyymmdd)
print(num)