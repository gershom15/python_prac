### 객체지향(OOP)이란 무엇인가?
# for 생산성 향상.
# 플라톤의 이데아라고 생각하면 될 것 같다. dog가 있을 때 구체적인 dog 이전의 이데아로서의 dog

### class 란 무엇인가?    일종의 틀이다. 붕어빵 틀을 떠올리라

# 클래스 변수 : 직접 접근 가능
# 인스턴스 변수 : 객체마다 별도로 존재

## 파이썬 클래스

# 클래스 and 인스턴스 차이 이해

# 예제1
class Dog(object):  #object 상속
    pass

class Dog:
    pass

class Dog():
    pass    #셋 다 쓸 수 있다. 표현법 익혀둘 것

print('>>>>>>>>>>' *8)
class Dog():
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):   #class를 쓰려면 반드시 한번은 이 함수를 선언해줘야함
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)


# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)
c = Dog('mikky', 2)

# 비교
print(a == b, id(a), id(b), id(c))  # a와 c는 정보는 같지만 파이썬에서는 인스턴스화 시킨 것은 전혀 다른 것으로 간주하고 있다.

# 네임스페이스   : 객체를 인스턴스화 할 때 저장된 공간
print('dog1 : ', a.__dict__)
print('dog2 : ', b.__dict__)



# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

print('>>>>>>' *8)

class Dog():
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):   #class를 쓰려면 반드시 한번은 이 함수를 선언해줘야함
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)


# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)
c = Dog('mikky', 2)


if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)   # 클래스로 바로 접근 가능
print(a.species)        # 인스턴스로도 접근 가능
print(b.species)



# 예제2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print('Func2 called')   # init 메소드를 하지 않았다 여기선. 직접 지정하지 않으채 넘어가면
                                # 파이썬이 알아서 기본 것으로 만들어줌. 그래서 이렇게 해도 에러 없이 실행 가능

f = SelfTest()

print(dir(f))  # 어떤 함수를 쓸 수 있는지 확인할 수 있는 명령어이다. 끝에 func1, 2가 있는 걸 확인할 수 있다.

print(id(f))
# f.func1()   예외현상 발생.   func1을 호출하려면 클래스를 바로 불러와야한다.
SelfTest.func1()   # 이러면 클래스로 func1이 불러와진다.

f.func2()  # 인스턴스로 부를 수 있다.
# SelfTest.func2()  # 이번엔 반대로 빈괄호로 클래스를 부르면 func2가 안된다. ()안에 인스턴스를 넣어줘야함
SelfTest.func2(f)


# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1  # 인스턴스가 하나 추가될 떄마다. stock_num도 1오름

    def __del__(self):
        Warehouse.stock_num -= 1   # 인스턴스가 하나 소멸하면 -1 됨

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before : ', Warehouse.__dict__)

print(user1.stock_num)


del user1
print('After : ', Warehouse.__dict__)



# 예제4
class Dog2():
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):   #class를 쓰려면 반드시 한번은 이 함수를 선언해줘야함
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound): # sound 정의 안해줬기 때문에 여기에 써줘야함 주의
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog2('july', 4)
d = Dog2('Marry', 10)
#메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))  # speak은 여기서 넘겨줘야한다.(괄호로)
print(d.speak('Mung Mung'))
