"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 기둥과 보 설치
description : 구현
"""


def check(result):
    for x, y, a in result:
        # 기둥
        if a == 0:
            if y == 0 or (x - 1, y, 1) in result or (x, y, 1) in result \
                    or (x, y - 1, 0) in result:
                continue
            else:
                return False
        # 보
        else:
            if (x, y - 1, 0) in result or (x + 1, y - 1, 0) in result or \
                    ((x - 1, y, 1) in result and (x + 1, y, 1) in result):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    result = set()

    for frame in build_frame:
        x, y, a, b = frame

        # 설치
        if b == 1:
            result.add((x, y, a))
            flag = check(result)

            if flag is True:
                continue
            else:
                result.remove((x, y, a))
        # 삭제
        else:
            if (x, y, a) in result:
                result.remove((x, y, a))
                flag = check(result)

                if flag is True:
                    continue
                else:
                    result.add((x, y, a))

    answer = [list(i) for i in result]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer
