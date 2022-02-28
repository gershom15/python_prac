# print 사용법


# 기본 출력
print('Python Start!')
print('''python start''')
print()    # print문 자체는 개행(줄바꿈)을 한다


# separator 옵션
print('p', 'y', 't', 'h', 'o', 'n')

print('p', 'y', 't', 'h', 'o', 'n', sep='|')
print('p', 'y', 't', 'h', 'o', 'n', sep='')

print('010', '5555','2222', sep='-')

print('python', 'gmail.com', sep='@')


# end 옵션
print('welcome to', end=' ') #원래 print는 줄바꿈이지만 이 옵션을 쓰면 end의 주문에 따라 연결해줌
print('IT News', end=' ')
print('Web site')


# file 옵션
import sys

print('Learn Python', file=sys.stdout)
print()


# % 또는 format 사용(d : 정수(digit) , s : 문자열(string), f : 실수(float))
print('%s %s' % ('one', 'two')) # %는 해당 위치 대신에 무엇인가를 집어넣을 수 있게 해주는듯하다
print('{} {}'.format('one', 'two')) # 위와 마찬가지 효과를 가진다. 가독성은 이게 더 좋다. 위의 것은 d,s,f 이렇게 짝을 맞춰줘야함
print('{1}{0}'.format('one','two')) # {}{} 사이의 띄어쓰기도 출력에 영향을 줌
print('{1} {0}'.format('one','two')) #순서를 지정해줌. 두번쨰 중괄호를 우선함
print('{} {}'.format('one','two'))

print()


# %s
print('%10s' % ('nice'))   # %는 할당한다는 뜻이다.
print('%10s' % ('nice1111'))
print('{:>10}'.format('nice'))  # 위와 결과는 같다. 다만 > 기호로 인해 왼쪽부터 할당


print('%-10s' % ('nice'))   # 음수로 하면 오른쪽부터 공백을 채우고 나머지를 채움
print('{:<10}'.format('nice')) # 방향은 곧 어느쪽부터 공백을 채우는가이다.


print('{:_>10}'.format('nice')) # : 앞에 뭔가를 붙이면 그것으로 채울 수 있다.

print('{:_>10}'.format('nice'))

print('{:^10}'.format('nice'))   # 중앙에 정렬함

print('%5s' % ('nice'))
print('%.5s' % ('niceguypsy'))  # .이 있으면 절삭.   . 자체가 절삭, 반올림, 여기까지 라는 뜻
print('%5s' % ('niceguypsy'))


print('{:10.5}'.format('pythonstudy'))   # 공간은 10개 확보 그러나 5글자만 절삭

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))


print('%4d' % (42))
print('{:4d}'.format(42))  # 정수에서 포맷함수 쓸 때는 d를 써준다



# %f
print('%f' % (3.141213431))  # 소수 여섯째자리까지만 출력된다
print('%1.8f' % (3.141213431))  # 정수부분 몇자리 소수 부분 몇자리 나와라고 설정가능
print('%1.18f' % (3.141213431))

print('{:f}'.format(3.142132))
print('%06.2f' % (3.141592653))  # 여섯자리 할당하고 소수부는 2자리만 이라는
print('{:06.2f}'.format(3.141592653)) # 위와 같은 표현을 포맷함수0
