""" 년월일을 출력하는 방법은  나라마다 형식마다 조금씩 다르다.
    년월일(yyyy.mm.dd)를 입력받아,
    일월년(dd--mm--yyyy)로 출력해보자.
    (단, 한 자리 일/월은 0을 붙여 두자리로 출력한다. """

day = input().split('.')

if len(day[1]) == 1 :
    day[1] = '0'+day[1]
if len(day[2]) == 1 :
    day[2] = '0'+day[2]

print("{}--{}--{}".format(day[2], day[1], day[0]))