## 영문자(a~z) 1개가 입력 되었을 때 그 문자까지의 알파벳을 순서대로 출력 해 보자.

converter = ord(input())

for i in range(97, converter+1):
  print( chr(i), end=' ' )