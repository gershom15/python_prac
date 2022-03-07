### 파이썬 사용자 입력
# Input 사용법
# 기본타입(str)


# 예제1
name = input('Enter Your Name : ')
grade = input('Enter Your Grade : ')
company = input('Enter Your Company name : ')

print(name, grade, company)


# 예제2
number = input('Enter number : ')
name = input('Enter name : ')

print('type of number', type(number)) # 해보면 숫자를 입력했음에도 sdt로 뜬다. input의 기본 타입은 str이다
print('type of name', type(name))


# 예제3(그렇다면 계산을 어떻게 하면 되는가?)
first_number = int(input('Enter number1 : '))
second_number = int(input('Enter number2 : '))

total = first_number + second_number

print('first_number + second_number : ', total)



# 예제4
float_number = float(input('enter a float number : '))

print('input float : ', float_number)
print('input type : ', type(float_number))



# 예제5
print('FirstName -{0}, LastName -{1}'.format(input('Enter first name : '), input('Enter Last name : ')))
