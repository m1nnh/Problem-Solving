## 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.

class Calculator :
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator) :
    def add(self, val):
        if self.value > 100 :
            self.value = 100
        else :
            self.value += val

cal = MaxLimitCalculator()
cal.add(50)
cal.add(40)

print(cal.value)