## 파이썬 예외처리의 이해
# 예외 종류

# SyntaxError, TypeError, NameError, IndexErrorm ValueErrorm KeyError....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요

# 1. 예외는 반드시 처리해야함.
# 2. 로그는 반드시 남긴다.(일종의 증거)
# 3. 예외는 던져진다. -> 다른 곳으로 처리를 위임할 수 있다.(through try & except)
# 4. 예외를 무시할 수도 있다. 그러나 권장하지 않음.


## SyntaxError : 문법오류
# print('error)
# print('error'))
# if True
#   pass



## NameError : 참조없음
# a = 10
# b = 2
# print(c)



## ZeroDivisionError : 0으로 나누려 할 때
# print(100/0)



## IndexError
# x = [50, 70, 30]
# print(x[1])
# print(x[4])



## KeyError
dic = {'name' : 'Lee', 'Age' : 41, 'City' : 'Busan'}
# print(dic['hobby'])
print(dic.get('hobby'))  # get메쏘드를 쓰면 에러가 아닌 none이 나와서 보다 안정적인 코딩가능




## 파이썬으로 프로그래밍 할 때,
### 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리를 권장(by EAFP)



## AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2()) # time 모듈에 time2는 없다는 뜻



## ValueErrorm
# x = [10, 50, 60]
# x.remove(50)
# print(x)
# x.remove(500)



## FileNotFoundError
#f = open('test.txt')



## TypeError : 자료형에 맞지 않는 연산을 수행할 경우
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

print(x + list(y))  # 형변환을 하면 더할 수 있다.




### 예외처리
# try : 에러가 발생할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 :
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제1
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))
except ValueError :
    print('Not found it! - Occurred ValueError!')
else :
    print('Ok, else.')   # 문제가 없기 때문에 else까지 출력됨.

print('>>>>>>>>' * 8)

try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))
except ValueError :
    print('Not found it! - Occurred ValueError!')
else :
    print('Ok, else.') # 원래라면 밸류에러가 떠야하지만 except에서 처리를 한 것이다.



## 예제2
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))
except Exception :   # 이렇게 하면 모든 에러를 다 잡는다. 대신 어떤 에러인지는 알 수 없다.
                    # Exception 빼고 except : 만 해도 됨
    print('Not found it! - Occurred ValueError!')
else :
    print('Ok, else.')


print('>>>>>>' *8)


## 예제3
try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))
except Exception as e : # 이렇게 하면 에러가 어떻게 났는지를 보여줄 수 있다!
    print(e)
    print('Not found it! - Occurred ValueError!')
else :
    print('Ok, else.')
finally:
    print('Ok!, finally.')  # 예외가 발생하든 안하든 항상 실행해줘야할 것이 있을 때 씀


## 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim' :
        print('Ok! Pass!')
    else :
        raise ValueError  # 밸류에러가 발생할 이유가 없지만 raise를 통해 일부로 발생시킴.
                        # 에러 종류를 보고 어떤 상황인지 알 수 있기 때문
except ValueError:
    print('Occurred! Exception!')
else:
    print('Ok! else!')


print('>>>>>>>>>' * 8)

try:
    a = 'Kim'
    if a == 'Kim' :
        print('Ok! Pass!')
    else :
        raise ValueError  # 밸류에러가 발생할 이유가 없지만 raise를 통해 일부로 발생시킴.
                        # 에러 종류를 보고 어떤 상황인지 알 수 있기 때문
except ValueError:
    print('Occurred! Exception!')
else:
    print('Ok! else!')
