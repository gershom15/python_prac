### 파이썬 반복문
## FOR 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>


for v1 in range(100):    # v1은 for문 안에서 쓸 변수를 선언한 것이다.
                        # range() 괄호안은 n-1 로 외워라
    print('v1 is ', v1)

print()

for v2 in range(1,11):   # 1~10까지 나옴
    print('v2 is ', v2)

print()

for v3 in range(2,11,2):    # 한칸 건너 뛰어라.   ## 짝수 홀수, 배수 구할 떄 유용
    print('v3 is ', v3)


# 1 ~ 1000까지의 합
sum1 = 0

for v in range(1,1001):
    sum1 += v   # +=는 누적시킨다고 보면된다.   sum1 = sum1 + v 의 축약 형태이다.

print('1~1000 sum : ', sum1)

# 또 다른 방법
print('1~1000 sum(using range) : ', sum(range(1,1001))) # range가 1~1000까지 목록을 다 불러옴

# cf, 4의 배수 합
print('1~1000까지 4의 배수의 합 : ', sum(range(4,1001,4)))




## Iterables 자료형 반복 : 이러한 형식이면 전부 for문을 사용할 수 있다.
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
name1 = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in name1:
    print('You are : ', n)



# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print('Current number : ', n)

# 예제3
word = 'beautiful'

for s in word:
    print('You are : ', s)


# 예제4
my_info = {
    'Name' : 'Park',
    'Age' : 30,
    'City' : 'Ulsan'
}

for d in my_info:
    print('key : ', d)  #  이렇게 하면 키만 가져온다

print('>>>>>>>>>>>>' *8)

for d in my_info :
    print('key : ', my_info[d])

print('>>>>>>>>>>>>' *8)

for d in my_info :
    print('key : ', my_info.get(d))  # get 메쏘드를 써도 밸류를 가져올 수 있다.


print('>>>>>>>>>>>>' *8)

for v in my_info.values() : # 여기서 .values()를 써서 밸류만 가져올 수도 있다.
    print('value : ', v)




# if, for문 같이 써보기
name = 'FineAppLE'  # 여기서 대문자로 다 바꾸고 싶다면?

for n in name :
    if n.isupper():
        print(n)
    else :
        print(n.upper())

print('>>>>>>>>>>>>' * 7)

# 대문자로 고쳐서 일렬로 다시 단어를 만들고 싶다면?
w = ''

for a in name :
    if a.isupper():
        w += a
    else :
        w += a.upper()

print(w)


## break  목적한 바를 얻고 불필요한 반복이 필요없는 경우 for문을 탈출하는 명령

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers :
    if num == 34:
        print('Found : 34!')
    else :
        print('Not found : ', num)   # 뒤에까지 다 찾아봄

print('>>>>>>>>>>' * 8)

for num in numbers :
    if num == 34:
        print('Found : 34!')
        break
    else :
        print('Not found : ', num)



# continue   이 명령은 해당 명령 아래 것들을 실행하지 않고 다시 처음으로 돌아감.
        # 음악으로 치면 도돌이표 같은 것
        # 용례는 출력을 할 때 내가 원치 않는 것이 출력되지 않게 하려할때 등 쓸 수 있다.

lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print('current type : ', v, type(v)) # 불린 형이 출력되지 않는다.
    print('multiply by 2', v * 2)



# for - else 구문
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print('Found : 24')
        break
else:
    print('Not found : 24') # for문 반복을 모두 실행하고 해당되는게 있으면 이것만 실행하고 else는 실행x

print('>>>>>>>' *8)

for num in numbers:
    if num == 49:
        print('Found : 49')
        break
else:
    print('Not found : 49') # for문 반복을 모두 실행하고 해당되는게 없으면 else를 실행한다.



# 구구단 출력 - 내가 한거
for i in range(2,10):
    for e in range(1,10):
        print(i * e, end=' ')   # 값 하나 나오고 줄바꿈을 하지 않고 구분만 하기 위해 end를 씀
    print()    # n단 구구단임을 구분하기 위해 씀



# 구구단 출력 - 전문가
for i in range(2,10):
    for e in range(1,10):
        print('{:4d}'.format(i*e), end='') # 4자리 정수형에다가 포맷은 i*e 형태. 4자리 단위수를 맞춰줘서
                                            # end에 따로 띄어쓰기 넣을 필요 없음
    print()    # 4자리 정수형을 설정해주는 이유는 숫자의 정렬은 오른쪽정렬인데 그것을 해주기 위함.


# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))  # 이렇게 하면 주소값만 나온다 형변환을 해줘야함
print('list', list(reversed(name2)))
print('tuple', tuple(reversed(name2)))
print('set', set(reversed(name2)))  #순서가 없고 중복이 안됨. 계속실행해보면 순서가 바뀌어서 나옴




# 글자 거꾸로 쓰기
c=''
name5 = 'banana'
reversed(name5)
list(reversed(name5))
print(list(reversed(name5)))
for v in list(reversed(name5)):
    c += v
    continue
print(c)
