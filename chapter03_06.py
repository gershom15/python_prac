## 집합 (set)  특징
# set 자료형(순서x, 중복x)

# 선언
 # 1) set() 하고 그 안에 리스트형식으로 넣는다
 # 2) 중괄호하고 열거(키값, 밸류값 없이)
a= set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'pen', 'cap', 'plate'])  # 숫자 문자형 같이 가능
e = {'foo', 'bar', 'baz', 'foo', 'qux'}  # 딕셔너리처럼 중괄호를 썼지만 키와 밸류형식이 아니라 이렇게 열거 형식인 경우도 set임
f = {42, 'foo', (1,2,3), 3.141592}   # 잡탕도 가능

print('a - ', type(a), a, 'boy' in a)  # in 함수도 가능
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)  # 중복을 허용하지 않기 떄문에 foo 하나만 출력됨
print('f - ', type(f), f)


# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)


# length
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))


# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)   # 교집합을 보여줌
print('s1 & s2 : ', s1.intersection(s2))  # 위와 같음


print('s1 | s2 : ', s1 | s2)   # 합집합
print('s1 | s2 : ', s1.union(s2))


print('s1 - s2 : ', s1 - s2)  # 차집합
print('s1 - s2 : ', s1.difference(s2))


# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))   # False가 나오면 교집합 원소가 있다는 뜻


# 집합 관계 확인
print('subset : ', s1.issubset(s2))  # s1이 s2의 부분 집합이냐?
print('subset : ', s1.issubset(s1))

print('superset : ', s1.issuperset(s2)) # s1이 s2를 포함하느냐?


# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)    # 추가


s1.remove(2)
print('s1 - ', s1)  # 제거1
    # s1.remove(7) 없는 키를 삭제하라는 명령을 받으면 에러가 난다.
    # 에러가 안나게 하려면 먼저 이 키가 있는지 확인하는 코드를 먼저 짜야한다.

s1.discard(3)
print('s1 - ', s1)   # 제거2
s1.discard(7)
print('s1 - ', s1) # 이건 없는 키값으로 해도 에러가 나지 않는다. 훨씬 안정적이다.


s1.clear()
print('s1 - ', s1)   # 싹다 지움



 # cf. 리스트도 clear 함수 사용 가능
r = [1, 2, 3, 4]
r.clear()
print(r)
