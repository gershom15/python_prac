## 파일 읽기 및 쓰기

# 읽기 모드 : r / 쓰기 모드 : w / 추가모드 : a / 텍스트 모드 : t(t는 보통 기본값) / 바이너리 모드 : b
# 상대 경로(내가 현재 있는 위치 기준으로 따짐) (../, ./), 절대경로(C:|Django|example..)

# 파일 읽기(read)

#예제1
# open 함수 : 내부와 외부를 연결해주는 파이프같은 역할

f = open('./resource/it_news.txt', 'r', encoding='UTF-8')  # 'r'해도 되고 'rt'해도된다. t는 어차피 기본값

#속성 확인
print(dir(f))
print(f.encoding)
#파일이름
print(f.name)
# 모드 확인
print(f.mode)

cts = f.read()
print(cts)
#반드시 close
f.close()



# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(iter(c))
    print(list(c))     # with 문을 쓰면 close()를 따로 쓰지 않아도 내부적으로 리소스가 닫힘

print()


# read() : 전체 읽기 / read(10) : 10byte만 읽어온다.
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)      # 커서가 있어서 어디까지 현재 읽어왔는지를 기억한다.
    print(c)
    f.seek(0,0) # 커서가 처음으로 돌아감
    c = f.read(20)
    print(c)



# 예제 4
# readline : 한 줄씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()


# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장(많이씀)
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')    # 다시 형식을 복원

print()




## 파일 쓰기(write)
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')


# 예제2
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python2\n')   # 이러면 내용이 바뀜

with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python3\n')  # 이러면 내용 추가됨


# 예제3
# wrihtelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)


# 예제4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)  # print문이 콘솔(하단)에 출력되지 않는 대신에 파일로 출력해줌


print()
