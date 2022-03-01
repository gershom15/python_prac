## 튜플
### 리스트와의 비교
## 튜플 자료형(순서O, 중복O, 수정X, 삭제X) 즉 불변-> 한번 선언하면 끝까지 써야함

# 선언
a = ()
b = (1)
b2 = (1,)  # 하나의 원소만 가지는데 튜플로 하려면 뒤에 ,를 찍어야 튜플로 인식
            # 이 의미는 수정, 삭제 하지 못하게 하곘다는 의미


print(type(a), type(b), type(b2))

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))


# 인덱싱
print('>>>>>>>>>>>' * 5)
print('d - ', d[1])

print('d - ', d[0] + d[1] + d[1])  # 튜플도 연산 가능
print('d - ', d[-1])
print('d - ', e[-1])
print('d - ', e[-1][1])

print('d - ', list(e[-1][1]))   # 리스트로 형변환 가능 -> 불변 특성 없어짐


# 수정x
  # d[0] = 1500  print(d)  에러남

# 슬라이싱 - 가능
print('>>>>>' *7)

print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])


# 튜플 연산   - 가능
print('>>>>>>' * 7)
print('c+d - ', c + d)
print('c * 3 - ', c * 3)


# 튜플 함수
a = (5, 2, 3, 1, 2)
print('a - ', a)
print('a - ', a.index(3))   # 숫자 3의 위치가 어디냐?

print('a - ', a.count(2))


## 팩킹 & 언팩킹  -> 튜플에서 매우 중요한 부분

# packing - 위에서 이떄까지 한 것들이 다 팩킹이다. 묶는 것
t = ('foo', 'bar', 'baz', 'qux')
print(t[1])

# unpacking1
(x1, x2, x3, x4) = t    # t의 원소들을 각자 변수로 할당해줌. 을 풀어서 각 순서에 맞는 원소에 대입
                        # 괄호가 없어도 언패킹이 되지만 관습상 언패킹을 했음을 보여주기 위해 괄호침
                        # 튜플 자체가 괄호 없이도 기능함
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print(x1)

# packing & unpacking - 괄호 생략한 버전
t2 = 1, 2, 3
t3 = 4,

x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
