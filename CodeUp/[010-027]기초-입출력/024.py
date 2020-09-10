""" 단어 1개를 입력받는다.
    입력받은 단어의 각 문자를 한줄에 한 문자씩 분리해 출력한다.
    (단, 단어의 문자를 하나씩 나누어 한 줄에 한 개씩 ''로 묶어서 출력한다.)
    입력 : boy 출력 : 'b'\n 'o'\n 'y'\n """

string = input()

for i in range(len(string)) :
    print("'{}'".format(string[i]))

