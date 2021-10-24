"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 스타트와 링크
description : 완전탐색
"""


def solution(N, skills, team, next):
    global answer

    if len(team) == N // 2:
        start, link = 0, 0
        link_team = []
        for i in range(N):
            if i not in team:
                link_team.append(i)

        for i in range(len(team) - 1):
            for j in range(i + 1, len(team)):
                start += skills[team[i]][team[j]] + skills[team[j]][team[i]]

        for i in range(len(link_team) - 1):
            for j in range(i + 1, len(link_team)):
                link += skills[link_team[i]][link_team[j]] + skills[link_team[j]][link_team[i]]

        answer = min(answer, abs(start - link))
        return

    for i in range(next, N):
        team.append(i)
        next = i + 1
        solution(N, skills, team, next)
        team.pop()


if __name__ == "__main__":
    global answer
    answer = int(1e9)
    N = int(input())
    skills = [list(map(int, input().split())) for _ in range(N)]
    solution(N, skills, [], 0)
    print(answer)
