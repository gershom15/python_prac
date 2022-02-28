### 파이썬 변수

# 기본 선언
n = 700

 #출력
print(n)

print(type(n))

# 동시 선언
x =y = z = 700
print(x,y,z)

# 선언
var =75

# 재선언
var ='change value'

#출력
print(var)
print(type(var)) # 가장 마지막 것이 할당됨


# Object Reference
#변수 값 할당 상태
 # 1. 타입에 맞는 오브젝트 생성
 # 2. 값 생성
 # 3. 콘솔 출력

# 예1
print(300)  # 쉽게 말해 파이썬이 어련히 알아서 변수없이도 출력함
print(int(300))  # 원래라면 이렇게 써줘야 함


# 예2
n = 777

print(n, type(n))

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))

print()


# id(identity)확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print()

print(id(m) == id(n))

# 같은 오브젝트 참조
m = 800
n = 800
print(id(m))
print(id(n))
print()

print(id(m) == id(n)) # 같은 값을 다른 변수로 할당해도 값이 같으면 그 값의 오브젝(일종의 주소)는 같다

# 다양한 변수 선언
## Camel Case : numberOfColleageGraduates -> 매 단어의 첫글자를 대문자로 -> Method를 주로 선언할 때
## Pascal Case : NumberOfColleageGraduates -> 카멜캐이스에 첫글자도 대문자로 -> Class를 주로 선언할 때
## Snake Case : number_of_colleage_graduates -> 주로 변수 선언시


# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
1AGE = 9  # 숫자가 맨 앞에 오는 변수 선언은 안됨


# 예약어는 변수명으로 불가능
for = 3  # 안됨
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not
class	from	or
continue	global	pass
""" # 안되는 것들
