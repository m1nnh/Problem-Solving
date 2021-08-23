"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [3차] 파일명 정렬
description : 정렬
"""


def solution(files):
    answer = []
    split_files = []
    index = 0
    for file in files:
        head, num, tail = "", "", ""

        for i in range(len(file)):

            if len(num) != 0 and (file[i].isalpha() or file[i] in [" ", ".", "-"]):
                tail += file[i:]
                break
            elif file[i].isdigit():
                num += file[i]
            else:
                head += file[i]

        split_files.append([head, num, tail, index])
        index += 1

    sort_files = sorted(split_files, key=lambda x: (x[0].lower(), int(x[1]), x[3]))

    for file in sort_files:
        answer.append("{0}{1}{2}".format(file[0], file[1], file[2]))

    return answer
