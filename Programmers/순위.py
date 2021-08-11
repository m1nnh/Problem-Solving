"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 순위
description : 그래프
"""

from collections import defaultdict


def solution(n, results):
    answer = 0
    wins, loses = defaultdict(set), defaultdict(set)

    for i in range(len(results)):
        wins[results[i][0]].add(results[i][1])
        loses[results[i][1]].add(results[i][0])

    for i in range(1, n + 1):
        for winner in wins[i]:
            loses[winner].update(loses[i])
        for loser in loses[i]:
            wins[loser].update(wins[i])

    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer
