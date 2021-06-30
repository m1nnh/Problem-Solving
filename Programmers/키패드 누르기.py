"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 키패드 누르기
description : 구현
"""


def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left = dic['*']
    right = dic['#']

    for number in numbers:
        now = dic[number]

        if number in [1, 4, 7]:
            answer += 'L'
            left = now

        elif number in [3, 6, 9]:
            answer += 'R'
            right = now

        else:
            dist_left = 0
            dist_right = 0

            for x, y, z in zip(left, right, now):
                dist_left += abs(x - z)
                dist_right += abs(y - z)

            if dist_left < dist_right:
                answer += 'L'
                left = now
            elif dist_right < dist_left:
                answer += 'R'
                right = now
            else:
                if hand == 'left':
                    answer += 'L'
                    left = now
                else:
                    answer += 'R'
                    right = now

    return answer
