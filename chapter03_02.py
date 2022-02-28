## 파이썬 문자형

# 문자열 생성
str1 = 'I am Python'
str2 = "Python"
str3 = """HOw are you?"""
str4 = '''Thank you!''' # 큰따옴표나 작은 따옴표 세개도 된다

#글자수 세기 : len
print(len(str1), len(str2), len(str3), len(str4))


# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))



# 이스케이프 문자 사용
print("I'm a boy") #  I'm 이렇게 안에 작은 따옴표가 있으면 큰따옴표로 묶는게 좋다. 안그러면 에러남

print('I\'m a boy')
print('a \t b') # 탭 간격만큼 벌어짐

print('a\nb') # 줄바꿈이 됨

print('a\""b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

# 탭, 줄바꿈

t_s1 = 'Click \t Start!'
t_s2 = 'New Line \n Check!'

print(t_s1)
print(t_s2)



# Raw String (이스캐이프의 반대)
raw_s1 = r'D:\python\test'

print(raw_s1)  #앞에 r을 붙여주면 역슬래시를 있는 그대로 보여줌

# 멀티라인 입력
multi_str = '''
String
Multi Line
test
'''

print(multi_str)  # 줄이 너무길어서 줄바꿈으로 해야할 떄

multi_str2 = \
'''
String
Multi Line
test
'''

print(multi_str2) # 위의 것은 '''를 = 옆에 붙여야했다. 반면 이번 것은 = 옆에 \ 만 붙여주면 다음 줄에서 '''로 전개할 수 있다.
                    # 파이썬은 \ 를 특별하게 여긴다. \가 나오면 뒤의 것이 뭔가 바운딩 되는구나로 판단한다.
                    # 글자 옆에 \를 붙이면 줄바꿈을 해도 이어져서 나온다.



# 문자열 연산
str_o1 = 'python'
str_o2 = 'apple'
str_o3 = 'How are you doing'
str_o4 = 'Seoul Daejeon Busan Jinju'

print(str_o1 * 3)  # 파이썬은 특이하게 문자열 연산이라는 기능이 있는데 반복이 되서 출력된다.

print(str_o1 + str_o2)
print('y' in str_o1) # in 연산자는 시퀀스에서 사용이 가능한데 문자열을 하나하나의 리스트라고 생각할 수 있따.
print('P' not in str_o2)


# 문자열 형 변환
print(str(66), type(str(66)))

print(str(10.1))
print(str(True), type(str(True)))


# 문자열 함수(upper, isalnum, startwith, count, endswith, isalpha...)
print('capitalize : ', str_o1.capitalize())  # 앞글자를 대문자로 바꿔줌

print('endswith? : ', str_o2.endswith('d')) # 끝글자가 d로 끝나는지를 물어봄

print('replace : ', str_o1.replace('thon', 'good thing')) # 앞에 언급한 부분을 뒤에 언급한 부분으로 바꿔 줌

print('sorted : ', sorted(str_o1)) # 문자열을 입력받아서 리스트 형태로 정렬함

print('split : ', str_o4.split(' ')) # 배열형태로 쪼개서 보여줌. '' 안에는 무엇을 기준으로 쪼갤건지를 쓰는 것.
                                    # 여기서는 띄어쓰기 1번 임. 만약 !였으면 '!'으로 쓰면됨



#반복(시퀀스)
im_str = 'Good Boy!'

print(dir(im_str))  # dir은 변수 안에 어떤 클라스가 있는지 알 수 있게 하는데 그 중에
                    # '__iter__'가 있다. 이게 있으면 시퀀스라는 뜻이며 반복이 가능하다는 뜻

# ex.출력
for i in im_str:
    print(i)



# 슬라이싱 연습
str_sl = 'Nice Python'

print(len(str_sl))


# 슬라이싱 연습
print(str_sl[0:3]) # 0부터 2까지 나옴

print(str_sl[:len(str_sl)])   # 끝부분까지 하고 싶을 경우 :다음에 비워도 되고 len함수로 써도 됨

print(str_sl[:len(str_sl)-1])  # str_sl[:10]과 같은 의미임
print(str_sl[1:4:2])  # 1부터 3까지 가져오는데 2칸 간격으로 가져와라. 즉 세번쨰 인수는 단위이다.

print(str_sl[-5:])
print(str_sl[1:-2])

print(str_sl[::2])
print(str_sl[::-1])   # 역방향으로 출력되게 한다.


# 아스키 코드 or 유니코드
a = 'z'
print(ord(a))  # z의 아스키 코드 번호 묻는것

b = 'ㅁ'
print(ord(b))

print(chr(122))   # 이번엔 반대로 아스키코드 번호가 무슨 문자인가를 보여줌
