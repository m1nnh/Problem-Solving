"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 외벽 점검
description : 구현, 조합
"""

from itertools import permutations
import copy


def solution(n, weak, dist):
    answer = len(dist) + 1

    copy_weak = copy.deepcopy(weak)

    for i in range(len(weak)):
        copy_weak.append(weak[i] + n)

    for i in range(len(weak)):
        start = [copy_weak[j] for j in range(i, i + len(weak))]
        comb_list = list(permutations(dist, len(dist)))

        for comb in comb_list:
            idx, count = 0, 1

            length_check = start[0] + comb[idx]

            for j in range(len(start)):
                if start[j] > length_check:
                    count += 1

                    if count > len(comb):
                        break

                    idx += 1
                    length_check = comb[idx] + start[j]

            answer = min(answer, count)

    if answer > len(dist):
        answer = -1

    return answer
