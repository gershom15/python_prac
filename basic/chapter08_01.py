### 파이썬 내장(Built-in) 함수
# 많이 쓰는 것 위주로
# str(), int() 등 형변환도 이 중 하나


# 절대값 : abs()

print(abs(-3))


# all : iterable 요소 검사(참, 거짓)
print(all([1,2,'']))  # 모든 요소가 다 참이어야 true를 띄움    like and


# any
print(any([1,2,'']))   # 하나라도 true값이 있으면 true이다. like or


# chr : 아스키 -> 문자  / ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))


# enumerate     : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i+1, name)


# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2

print(filter(conv_pos, [1, -3, 2, 0, -5, 6]))   # 값을 가져오려면 리스트를 씌워야한다.

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
 #  = print(list(filter(lambda x: abs(x) >2, [1, -3, 2, 0, -5, 6])))
    # 이 줄에만 쓸 함수인데 구태여 def써서 함수를 정의해주는 것보다 람다쓰는게 더 깔끔

print('>>>>>>>>>' *8)
print(list(filter(lambda x: abs(x) >2, [1, -3, 2, 0, -5, 6])))


# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))


# len 요소의 길이 반환
print(len('abcdefg') - 1)
print(len([1,2,3,4,5,6,7]))



# max, min : 최대값, 최소값
print(max([1,2,3]))
print(max('python study'))

print(min([1,2,3]))
print(min('python study'))




# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-3,2,0,-5,6])))



# pow : 제곱값 반환
print(pow(2, 10))


# range : 반복가능한 객체(iterable) 반환
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))


# round : 반올림 함수
print(round(6.5781, 2))

print(round(5.6))


# sorted : 반복가능한 객체(iterable) 정렬 후 반환
a = sorted([6,7,4,3,1,2])
print(a)

print(sorted(['p','y','t','h','o','n']))


# sum : 반복가능한 객체(iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))


# type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))


# zip : 반복가능한 객체(iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30],[40,50,60],[70,80,90]))) # 순서별로 하나씩 가져와서 튜플로 묶어줌

print(list(zip([10,20,30],[40,50,60],[70,80,])))  # 이렇게 짝이 안맞으면, 짝맞는것만 반환
