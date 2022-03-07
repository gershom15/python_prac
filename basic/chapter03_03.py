## 파이썬 리스트
## 자료구조에서 중요

### 리스 자료형의 특징 : 순서0, 중복0, 수정0, 삭제0   이 모든게 되는 유일한 자료형

#선언
a = []  # 빈 리스트 선언
b = list()   # 이 역시도 빈 리스트 선언
c = [70,75,80,85]

print(len(c))

d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]  #리스트 안에 리스트도 가능
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>' * 5)

print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[1] + d[0] + d[0])
print('d - ', d[-1])
print('e - ', e[2][1]) # 리스트 안의 리스트 인덱싱
print('e - ', list(e[2][1]))


# 슬라이싱
print('>>>>>>' *5)
print('d - ', d[0:3])
print('d - ', d[2:])

print('e - ', e[-1][1:3])


# 리스트 연산 : 리스트 + 리스트 = 리스트

print('>>>>>>>' *5)
print('c + d : ', c + d)
print('c * 3 : ', c *3)
print("'test' + c[0] : ", 'test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))    # 이번에도 효율성을 위해 갖은 주소를 가지고 있다.


# 리스트 수정, 삭제
print('>>>>>>>' *5)
c[0] = 4
print('c - ', c)

c[1:2] = ['a', 'b', 'c']
print('c - ', c)

c[1] = ['a', 'b', 'c']   # 위의 코드와 인덱싱 자체는 다르지 않지만 결과는 다르다. 리스트로서 통쨰로 들어감
print('c - ', c)

c[1:3] = []
print('c - ', c) # 제거되는 효과


del c[2]   # 삭제
print('c - ', c)


# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)

##추가
a.append(10)
print('a - ', a)

a.sort()
print('a - ', a)   # 오름차순으로 정렬됨

a.reverse()
print('a - ', a)    # 역순으로 정렬됨. 내림차순 오름차순 상관없이 현재 정렬의 역순일 뿐임

print('a - ', a.index(3))
print('a - ', a[3])   # 둘다 가능

# insert : append와 달리 추가할 위치 선정 가능
a.insert(2, 7)
print('a - ', a)

a.insert(len(a),12)   # 이것은 곧 append를 쓴 것과 같다.
print('a - ', a)


# 간편하게 제거하기 : del 은 순서를 알아야하기 때문에 방대한 양에서는 적합하지 않다
a.remove(10)
print('a - ', a)


# pop : 맨 끝 원소를 추출하고 나머지로 리스트 구성
print('a - ', a.pop())
print('a - ', a)    # 마지막에 있던 놈이 먼저 나올 떄 씀. 자주 씀

# count : 해당 값을 가진 원소의 개수를 알고 싶을 때
print('a - ', a.count(4))   # 4값을 가진 원소 몇개냐?

# extend : append의 리스트 버전
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제의 종류 : del(자료 개수 적을 떄) / pop(끝에 거부터 지울 떄) / remove

# 반복문 활용
while a:
    data = a.pop()
    print(data)
