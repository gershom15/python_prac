### 파이썬 제어문
 ## IF 실습

 # 기본 형식  ;참 거짓 판별 기준
print(type(True)) # 0이 아닌 수, 'abc', [1, 2, 3...], (1, 2, 3, ...) ...
print(type(False)) # 0, "", [], {}, ()   -> 빈 것들

 # 예1

if True:
    print('Good')

if 'a':
    print('Good')  # 존재하는 값이 있으면 출력함

if '' :
    print('good')  # False나 비어 있으면 출력하지 않음

if False:
    print('good')

# 예2
if False:
    print('nice')
else :
    print('Nice!')

if True:
    print('nice')
else :
    print('Nice!')


# 관계 연산자 : >, >=, <, <=, ==, !=
x= 15
y = 10

print(x==y)
print(x != y)

print(x > y)
print(x <= y)


city = ''
if city :
    print('You are in:',city)
else :
    print('Please enter your city')

city = 'Seoul'
if city :
    print('You are in:',city)
else :
    print('Please enter your city')


# 논리 연산자 : and , or, not
a = 75
b = 40
c = 10

print('and : ', a > b and b > c)
print('or : ', a> b or b>c) # or 에서는 True 뜨면 뒤에 것은 실행안함
print('not : ', not a > b)
print(not True)
print(not False)


# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1 : ', 3+12 > 7+ 3)
print('e2 : ', 5 + 10 *3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 ==10)

print('e3 : ', 5 + 10 > 0 and not 7 + 3 == 10)


score1 = 80
score2 = 'A'

#예4
# 복수의 조건이 모두 참일 경우에 실행
if score1 >=90 and score2 == 'A':
    print('Pass')
else :
    print('Fail')


# 예5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade =='platinum':
    print('최상위 관리자')


# 다중 조건문

num = 75
if num >= 90:
    print('Grade : a')
elif num >= 80:
    print('Grade : b')
elif num >= 70:
    print('Grade : c')
else :
    print('과락')


# 중첩 조건문 : if문 안에 if문

grade = 'A'
total = 95

if grade == 'A':    #A 등급 받은 사람 ''중에서'' 라는 의미
    if total >= 90:
        print('장학금 100%')
    elif total >=80:
        print('장학금 80%')
    else :
        print('장학금 50%')
else :
    print('장학금 없음')



#  in, not in
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {'name' : 'Lee', 'city' : 'Seoul', 'grade' : 'A'}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)

print('name' in e)  # 키를 물어보는 것은 가능

print('Seoul' in e.values())  # 밸류를 물어보려면 .values()를 써야함
