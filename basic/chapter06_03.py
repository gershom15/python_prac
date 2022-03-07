### 파이썬 패키지
## 패키지 작성 및 사용법
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성

# 상대경로 : ..(부모 경로)(바로 위 경로) / .(현재 디렉토리) -> 모듈 내부에서만 사용
## cf> cmd 에서 cd .. 하면 부모 경로로 감 / cd \ 하면 바로 C:\로 감

# 예제1
import sub.sub1.module1

# 예제2
from sub.sub1 import module1   # 예제1처럼 일일이 치지 않고 이렇게 주소를 지정해서 가져올 수 있다
from sub.sub2 import module2 as m2   # alias    약어로 지정할 수도 있다.


# 호출
module1.mod1_test1()
m2.mod2_test2()


# 예제3
from sub.sub1 import *   # *를 하면 sub1 안에 파일이 10개 있으면 10개 다 가져온다는 뜻
                        # 별로 쓰지 않는 것을 추천, 쓰지도 않는데 불필요한 작업이기 때문


## __init__.py : 일종의 패키지로 인식하는 허가증. python 3.3부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
