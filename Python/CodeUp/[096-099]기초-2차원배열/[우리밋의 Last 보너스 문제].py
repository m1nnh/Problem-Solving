"""
해당 문제는 이차원 배열의 개념과 원리를 파악하기 위해 "우리밋"이 직접 만든 문제임을 알려드립니다.
x축과 y축의 개념을 머릿 속에서 자유롭게 조작할 수 있도록 훈련하기 위해 만든 문제입니다.
이 점을 기억하시고 아래 문제를 푸시길 바랍니다.
해당 문제를 배포하시거나 외부에서 사용하실 때는 "우리밋"을 한번씩만 거론 부탁드리겠습니다.
구독만 해주신다면 그것으로 충분합니다.

ps. "내 미래"가 해당 문제 이름입니다. 참고로 전 다녀왔습니다. :)
훈련병인 철수는 교관의 지시에 따라야한다.
교관은 "좌로 1보, 하로 2보 가!"와 같이 좌,우,상,하로 이동할 것을 명령한다.
철수의 현재 위치가 입력으로 주어질 때 교관의 명령대로 이동한 위치는 어디일까?
제한 조건
1. 철수의 현재 위치는 첫 입력 값으로 공백을 두고 입력된다.
  ex) 1 1 => (0, 0), 5 4 => (4, 3)
2. 훈련소의 전체 공간 크기는 5*5 이다.
3. 교관이 지시한 명령은 절대 훈련소 공간을 벗어나지 않는다.
4. 좌는 왼쪽, 우는 오른쪽, 상은 위쪽, 하는 아래쪽으로 한다.
5. 입력은 좌,우,상,하의 순서대로 공백을 두고 입력된다.
  ex) 3 2 3 3 => 좌로 2보, 우로 2보, 상으로 3보, 하로 3보 이동.
"""

position = [[0 for _ in range(5)] for _ in range(5)]
init_position=list(map(int, input().split()))
print(init_position)
change_position=list(map(int, input().split()))
print(change_position)
position[init_position[0]-1-change_position[3]+change_position[1]][init_position[1]-1-change_position[0]+change_position[1]]=1
for i in position :
    print(*i)




