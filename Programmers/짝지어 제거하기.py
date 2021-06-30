from collections import deque

def solution(s):
    answer = 0
    flag = True
    for i in range(len(s) - 1):


        if s[i] == s[i + 1]:
            flag = False
            answer = 1




print(solution('baabaa'))
print(solution('cdcd'))