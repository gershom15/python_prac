## 딕셔너리
# 범용적으로 가장 많이 사용

# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)


# 선언   - 딕셔너리는 선언방법이 다양하다
a = {'name' : 'Kim', 'phone' : '0101389147', 'birth' : '000301'}
b = {0 : 'Hello python'}  # 키에 숫자도 가능
c = {'arr' : [1,2,3,4]}
d = {
    'name' : 'Niceman',
    'city' : 'Seoul',
    'age' : 33,
    'grade' : 'A',
    'status' : True
}

e = dict([
    ('name', 'Niceman'),
    ('city', 'Seoul'),
    ('age', 33),
    ('grade', 'A'),
    ('status', True)
])                      # dict하고 튜플&리스트 형태로 해서 각 원소별로 튜플식으로 괄호 -> 이게 가장 정석직인 표기지만 잘 쓰지 않음

f = dict(
        name = 'Niceman',
        city = 'Seoul',
        age = 33,
        grade = 'A',
        status = True
)               # 보통 많이 쓰는 딕셔너리 선언 방식. 키에 따옴표가 없고, : 이 아니라 = 임에 주목

    # f를 한 사람의 정보라 생각해보자. 그러면 student = [f1, f2, f3..] 이런 식으로 효율적으로 관리할 수 있다.
    # json 형태가 이런 딕셔너리 형태로 되어있다.


print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)


# 출력
print('a - ', a['name'])
print('a - ', a.get('name'))   # 이럴 때는 둘다 같은 결과를 가져온다. 그런데

    # print('a - ', a['name1'])   키가 존재하지 않으면 에러가 난다.
print('a - ', a.get('name1')) # 이렇게 해도 none이 뜬다. 즉 좀더 안정적인 코딩이 가능


print('b - ', b[0])
print('b - ', b.get(0))


print('f - ', f.get('city'))
print('f - ', f.get('age'))



# 딕셔너리 추가
a['address'] = 'Seoul'  # 키가 같으면 이걸로 수정해버림
print('a - ', a)

a['rank'] = [1, 2, 3]
print('a - ', a)  # 밸류값 자리에 리스트도 추가가 된다.


# 딕셔너리 세기 => 키의 개수를 셈
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))
print('e - ', len(e))


# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys()) # 키를 보여줌

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))   # 키 값들을 리스트로 변환할 수 있다


print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())   # 값만 보여줌

print('a - ', list(a.values()))
print('b - ', list(b.values()))  # 값을 리스트로


print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items()) # 키와 밸류를 둘다 보여주고 각 원소마다 튜플식으로 괄호로 묶여있음.
                        # 정식적인 표현을 원할 떄 출력값을 복사하면 될듯

print('a - ', list(a.items()))
print('b - ', list(b.items()))  # 이 자체도 리스트로 변환해서 사용 가능



print('a - ', a.pop('name'))   # 해당 키를 꺼내오고 딕셔너리 목록에는 없앤다.
print('a - ', a)

print('c - ', c.pop('arr'))
print('c - ', c)    # 꺼내온 값은 쓰면 되고 해당 딕셔너리는 비어있다.



print('f - ', f.popitem())
print('f - ', f)

print('f - ', f.popitem())
print('f - ', f)

print('f - ', f.popitem())
print('f - ', f)        # 끝에 키값을 가져옴



# in 연산자   => in 연산자는 일종의 ctrl+f 기능과 같다고 볼 수 있다.
print('a - ', 'birth2' in a)
print('d - ', 'city' in d)     # 해당 키가 있는지 색출 가능


# 수정 & 추가
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'Ulsan'
print('a - ', a)    # 이와 같은 식으로도 수정, 추가할 수도 있다.


a.update(birth='220301')
print('a - ', a)   # 이 방식이 좀더 코드적이다.

temp = {'address' : 'Backreoung'}
a.update(temp)
print('a - ', a)   # 이렇게 명시적으로 선언하고 이 함수를 쓸 수도 있다.
