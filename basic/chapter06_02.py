## 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
# 모듈이 모이면 패키지

def add(x, y) :
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# print('-' * 15)
# print('called! inner!')
#
# print(add(5,5))
# print(substract(15,5))
# print(multiply(5,5))
# print(divide(10,2))
# print(power(5,3))



if __name__ == '__main__':  # 이것이 이곳이 아닌 다른 곳에서 호출할 때는 main 이 아니다.
                            # 그러면 아래의 코드들이 실행되지 않게 된다.
    print('-'*15)
    print('called! __main__')
    print(add(5,5))
    print(substract(15,5))
    print(multiply(5,5))
    print(divide(10,2))
    print(power(5,3))
    print('-'*15)
