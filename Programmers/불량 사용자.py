"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 불량 사용자
description : 해시, 셋, 조합
"""

from collections import defaultdict
from itertools import permutations
import copy


def solution(user_id, banned_id):
    answer = []
    count_dic = defaultdict(int)
    candidate_dic = defaultdict(set)
    candidate = set()

    for ban in banned_id:
        for user in user_id:
            flag = True

            if len(ban) != len(user):
                continue

            for i in range(len(ban)):
                if user[i] != ban[i]:
                    if ban[i] != "*":
                        flag = False
                        break

            if flag is True:
                candidate.add(user)
                candidate_dic[ban].add(user)

        count_dic[ban] += 1

    combination_list = list(permutations(candidate, len(banned_id)))

    for comb in combination_list:
        cp_candidate_dic = copy.deepcopy(candidate_dic)
        cp_count_dic = copy.deepcopy(count_dic)
        visited = [0 for _ in range(len(comb))]
        result = []

        for ban in banned_id:
            for i in range(len(comb)):
                if comb[i] in cp_candidate_dic[ban]:
                    if visited[i] == 0 and cp_count_dic[ban] > 0:
                        visited[i] = 1
                        cp_count_dic[ban] -= 1
                        result.append(comb[i])

        if visited.count(0) == 0:
            result.sort()

            if result not in answer:
                answer.append(result)

    return len(answer)
