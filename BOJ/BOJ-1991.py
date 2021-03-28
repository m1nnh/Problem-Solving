"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 트리 순회
description : 재귀함수
"""


def pre(now_node):
    if now_node == '.':
        return
    else:
        print(now_node, end='')
        left, right = Tree[now_node]
        pre(left)
        pre(right)


def mid(now_node):
    if now_node == '.':
        return
    else:
        left, right = Tree[now_node]
        mid(left)
        print(now_node, end='')
        mid(right)


def post(now_node):
    if now_node == '.':
        return
    else:
        left, right = Tree[now_node]
        post(left)
        post(right)
        print(now_node, end='')


N = int(input())

Tree = {}

for _ in range(N):
    parent, left_child, right_child = map(str, input().split())
    Tree[parent] = [left_child, right_child]

pre('A')
print()
mid('A')
print()
post('A')
