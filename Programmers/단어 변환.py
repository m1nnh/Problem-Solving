"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 단어 변환
description : BFS
"""

from collections import deque


def solution(begin, target, words):
    answer = int(1e9)

    if target not in words:
        return 0

    visited = [False] * len(words)

    queue = deque()
    queue.append((0, begin))

    while queue:
        now_count, now_word = queue.popleft()
        if now_word == target:
            answer = min(answer, now_count)
            continue

        for i in range(len(words)):
            if visited[i] is True:
                continue
            count = 0
            for alpha1, alpha2 in zip(words[i], now_word):
                if alpha1 != alpha2:
                    count += 1

            if count == 1:
                queue.append((now_count + 1, words[i]))
                visited[i] = True

    if answer == int(1e9):
        answer = 0

    return answer
