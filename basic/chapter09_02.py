### 파일 읽기 및 쓰기

## CSV : MEME - text/csv

import csv

# 예제1
with open('./resource/test1.csv', 'r', encoding = 'UTF-8') as f:
    reader = csv.reader(f)
    # next(reader)  # Header를 스킵
    # next(reader)  # 이것도 커서개념이라 계속 쓰면 다음줄이 사라짐
    # 객체 확인
    print(reader)
    # 타입확인
    print(type(reader))
    # 속성 확인
    print(dir(reader))   # __iter__ 존재!
    print()

    for c in reader:
        print(c)
        # print(type(c))
        # list to str 바꾸고 싶다면?
        # print('   '.join(c))



# # 예제2
with open('./resource/test2.csv', 'r', encoding = 'UTF-8') as f:
    reader = csv.reader(f, delimiter='|') # 이 구분자로 되어있는 것으로 리스트 가져와줘

    for c in reader:
        print(c)


# 예제3
with open('./resource/test1.csv', 'r', encoding = 'UTF-8') as f:
    reader = csv.DictReader(f)  # Reader에도 대문자임에 주의
    # 확인
    # print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    # for c in reader:
    #     print(c)

    for c in reader:
        for k, v in c.items():
            print(k,v)
        print('--------------')     # 이러면 각 행마다 헤더를 살릴 수 있게 표현 가능


# 예제4 : 리스트를 하나의 csv로 만들기
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    print(dir(wt))
    print(type(wt))

    for v in w:
        wt.writerow(v)   # 각 원소가 row단위로 write됨을 확인할 수 있다.



# 예제5  : 헤더 만들기
with open('./resource/write2.csv', 'w', encoding='UTF-8') as f:
    # 필드명
    fields = ['one', 'two', 'three']

    # Dic Writer
    wt = csv.DictWriter(f, fieldnames=fields)
    # Header writer
    wt.writeheader()


    for v in w:
        wt.writerow({'one':v[0], 'two':v[1], 'three':v[2]})
