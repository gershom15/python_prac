### 파이썬 함수식 및 람다(Lamda)

# 함수 정의 방법
# def function_name(parameter):
#       code


# 예제1
def first_func(w):  # w는 이 함수에서 쓸 변수를 선언한 것(보통 인수라고 함)
    print('hello, ', w)


word = 'goodboy'

first_func(word)    # word를 괄호안에 넣어주면 함수에서 선언한 변수 w로 넘어가서 출력됨




# 예제2
def return_func(w1):
    value = 'hello, ' + str(w1)
    return value

x= return_func('goodboy2')
print(x)    #예제1은 그냥 함수가 출력을 하는 것이라면 예제2는 변수로 반환 받은 것까지 함


# 다중 반환
def func_mul(x):
    y1 = x* 10
    y2 = x* 20
    y3 = x* 30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x, y, z)


# 튜플리턴
def func_mul2(x):
    y1 = x* 10
    y2 = x* 20
    y3 = x* 30
    return (y1, y2, y3)

q = func_mul2(20)

print(type(q), q)   # 괄호로 묶여있다. 즉 팩킹되어있다. 여러개의 선언을 하나로 묶음


# 리스트 리턴
def func_mul3(x):
    y1 = x* 10
    y2 = x* 20
    y3 = x* 30
    return [y1, y2, y3]

p = func_mul3(30)

print(type(p), p ,set(p))   # 리스트로도 받을 수 있다.




# 딕셔너리 리턴
def func_mul4(x):
    y1 = x* 10
    y2 = x* 20
    y3 = x* 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}

d = func_mul4(30)

print(type(d), d, d.get('v2'), d.items(), d.keys()) # 'v2' (키부분) 따옴표 붙이는 것 주의


# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args):   # 매개변수명은 자유 # 묶음 데이터를 보내주면 언팩킹을 함
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim') # *를 함수 인자에 붙이면 가변인자로 인식하는 것이다.


# **kwargs(언팩킹)
def kwargs_func(**kwargs):  # ** 두개인 것은 키와 밸류 두개를 넘기는 것이다.
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('-----')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park')



# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1 = 20, age2 = 30, age3 = 40)



# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In func')
    func_in_func(num + 100)

nested_func(100)
# func_in_func(1000) 이건 호출되지 않는다. nested_func 안에 있으므로 이게 먼저 불러져야 쓸 수 있음




## 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉실실행 함수라서 Heap 영역에 저장되고, 메모리 초기화 된다.
# 즉 좀더 효율적으로 메모리를 쓴다. 하지만 남발하면 가독성이 저하된다.

def mul_func(x, y):
    return x * y

lambda x, y : x*y   # 둘은 같은 기능을 하지만 차이점이 있다. 람다는 함수명이 없다.

# 그렇기 때문에 변수에 담아서 쓴다.


# 일반적 함수 -> 할당
mul_func(10, 50)
print(mul_func(10, 50))

mul_func_var = mul_func

print(mul_func_var(20, 50))  # 함수에서는 변수에 다시 할당해도 된다.

# 람다 함수 -> 할당
lambda_mul_func = lambda x, y : x*y
print(lambda_mul_func(30,10)) # 람다도 위와 같이 변수에 할당한 것을 바로 사용할 수 있다.



def func_final(x, y, func):
    print(x * y * func(100, 100))

func_final(10, 20, lambda x,y:x*y)  # 위에 함수 func 부분은 정의하지 않았지만
                     # 람다를 사용하면 즉시 실행이기 떄문에 바로 값을 받을 수 있다.
                    # 일시적으로 바로 그 자리에 함수가 필요할 때
