

from collections import deque

a = [(1,2), (3,4), (0,0)]
queue=deque()
queue.append(a)
print(queue)
last = queue.popleft()
print(*last)
for i, j in last:
    print(i, j)
