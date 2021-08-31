"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 매칭 점수
description : 정규표현식
"""

import re
from collections import defaultdict


def solution(word, pages):
    web_page = []
    web_link = defaultdict(list)
    score_dic = defaultdict(list)

    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        score = 0

        # print("find")
        for find in re.findall(r'[a-zA-Z]+', page.lower()):
            # print(find)
            if find == word.lower():
                score += 1

        exios_link = re.findall('<a href="(https://[\S]*)"', page)
        # print("exios_link")
        # print(exios_link)
        for ln in exios_link:
            web_link[ln].append(url)

        web_page.append(url)
        score_dic[url].append(score)
        score_dic[url].append(len(exios_link))

    # print(web_page)
    # print(web_link)
    # print(web_page)
    # print(score_dic)
    answer = 0
    max_value = 0
    for index, page in enumerate(web_page):
        result = float(score_dic[page][0])
        for ln in web_link[page]:
            result += float((float(score_dic[ln][0]) / float(score_dic[ln][1])))
        # print(max_value)
        if max_value < result:
            max_value = result
            answer = index
    return answer
