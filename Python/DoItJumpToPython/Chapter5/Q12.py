## time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자.

import time

now = time.gmtime()
print("{}/{}/{} {}:{}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))