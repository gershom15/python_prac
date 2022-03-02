### 파이썬 반복문
## while 문

# if문과 비슷하며, 조건이 만족하면 계속 반복한다.

# while <expr>:
#   <statement(s)>


# 예제1
n = 5
while n > 0:
    n = n - 1
    print(n)


# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())


n = 5
while n > 0 :
    n -= 1
    if n ==2 :
        break
    print(n)
print('Loop Ended')



m = 5
while m > 0 :
    m -= 1
    if m ==2 :
        continue
    print(m)
print('Loop Ended')


# if 중첩
# 예제5
i = 1

while i <= 10:
    print('i : ', i)
    if i ==6 :
        break
    i += 1



# while - else 구문

# 예제6
n = 10
while n > 0 :
    n -= 1
    print(n)
    if n == 5:
        break
else :
    print('else out')   # break 가 있는 경우 else는 실행되지 않음

print('>>>>>>>>>>>>' * 5)

n = 10
while n > 0 :
    n -= 1
    print(n)
else :
    print('else out')   # break 문이 없으면 else는 실행되지 않는다.
                    # else의 용도는 마지막 마무리 출력을 자신이 원하는 바로 하기 위해서 쓴다.


# 예제7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'

i = 0

## 목록 중에서 원소를 찾고 싶을 때
while i < len(a):
    if a[i] == s:
        break
    i += 1
else :
    print(s, 'not found in list')


# 무한반복
    # while True:
    #   print('Foo')        while문이 트루면 무한으로 하기 때문에 컴퓨터가 다운된다. 조심할 것.
                            # 혹은 break 문을 반드시 삽입해야한다.



# 예제8
a = ['foo', 'bar', 'baz', 'qux']

while True :
    if not a:   # 머리좋다... a를 pop으로 다 뺴면 비어 있게 되고 이것은 False 이기 때문에
                # not a 가 true 가 되어 while True라는 무한 루프를 빠져나올 수 있게 된다. 캬
        break
    print(a.pop())
