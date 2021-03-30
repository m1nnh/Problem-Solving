"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 특정 거리의 도시 찾기
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.  2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

description : DFS/BFS
"""
import sys
from collections import deque

input = sys.stdin.readline


def BFS(graph, visited, X):
    queue = deque()
    queue.append((X, 0))
    visited[X] = True
    while queue:
        now, count = queue.popleft()
        if count == K:
            dis.append(now)
        for i in graph[now]:
            if visited[i] is False:
                queue.append((i, count + 1))
                visited[i] = True


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dis = []

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

BFS(graph, visited, X)
if len(dis) == 0:
    print(-1)
else:
    dis.sort()
    [print(x) for x in dis]
