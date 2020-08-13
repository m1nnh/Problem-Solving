""" 원하는 문자가 입력 될 때 까지 반복 출력하기.
    'q'가 입력 될 때 까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
    입력 : x b k d l q g a c
    출력 : 'q' 입력시 종료 """

boolean = True

while True:
    word = input().split()
    if word == 'q':
        boolean = False

