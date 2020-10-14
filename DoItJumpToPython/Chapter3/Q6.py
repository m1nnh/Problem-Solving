## 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
""" numbers = [1, 2, 3, 4, 5]
    result = []
    for n in numbers :
        if n % 2 == 1 :
            result.append(n*2)
"""

numbers = [1, 2, 3, 4, 5]

result = [n*2 for n in numbers if n % 2 == 1]
print(result)
