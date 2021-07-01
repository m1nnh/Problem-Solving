"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 폰켓몬
description : 구현
"""

def solution(nums):
    answer = 0
    dic = {}
    for number in nums:
        if number not in dic:
            dic[number] = 1
        else:
            dic[number] += 1
    if len(dic) <= len(nums) // 2:
        answer = len(dic)
    else:
        answer = len(nums) // 2
    return answer


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
