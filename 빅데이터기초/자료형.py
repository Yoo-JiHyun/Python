# 컬랙션 자료형
'''
- 여러가지 요소를 하나로 묶어서 사용하는 데이터 타입
    - 문법적인 요소들 빼고는 모두 다 담을 수 있다.
    - lst, set, dict, tuple
'''
# lst
'''
- 인덱싱
    - 데이터의 순번을 이용하여 특정 값을 선택할 수 있다.
- 슬라이싱
    - 데이터의 특정 범위를 선택할 수 있다.
- Mutable 자료형
    - 변경 가능하다.
- 중복 데이터 저장이 가능하다.
- []를 이용해서 만들 수 있다.
'''
lst = []
lst

lst = [1, 2, 3, "four", None, 7.0, True]
lst

type(lst)
# 자료 갯수
len(lst)

# 인덱싱(indexing)
'''
- 순번을 이용하여 데이터의 값을 선택할 수 있다.
- 파이썬의 인덱스는 두 종류가 있다.
- 양수 인덱스
    - 0 부터 시작
    - 왼쪽에서 오른쪽으로 1씩 감소
- 음수 인덱스
    - -1 부터 시작
    - 오른쪽에서 왼쪽으로 1씩 감소
- 인덱스는 무조건 정수이다.
'''
lst = [1, 2, 3, "four", None, 7.0, True]
lst

print(lst[0])
print(lst[4])

print(lst[-1])
print(lst[-3])

# 슬라이싱(Slicing)
'''
- 인덱스를 사용하여 데이터의 특정 범위를 선택할 수 있다.
- [start : end : step]
    - start, end, step은 생략이 가능하다.
    - start를 생략하면 자동으로 0이 들어간다.
    - end를 생략하면 자동으로 데이터의 길이가 들어간다.
    - 지정한 범위에서 step만큼 건너 뛰면서 슬라이실
    - step을 생략하면 기본적으로 1이 주어진다.
'''

lst = ["a","b","c","d","e","f","g"]
lst

lst[0:3]           # 0번 인덱스부터 3번 인덱스 까지
lst[-4:-1]         # 역방향
lst[:]             # 전체
lst[0:len(lst)]   # 0번 인덱스부터 자료 갯수 만큼 (전체)
lst[3:]            # 3번 인덱스부터 끝까지
lst[:5]            # 처음부터 4번 인덱스까지
lst[::]            # 전체
lst[0:len(lst):1] # 전체
lst[::2]           # 2번씩 건너뛰어 출력
lst[::-1]          # 역방향 출력
lst[-1:-5:-1]

# 수정 가능
lst[0] = "z"
lst

# tuple
'''
- 인덱싱 : 데이터의 순번을 이용하여 특정 값을 선택할 수 있다.
- 슬라이싱 : 데이터의 특정 범위를 선택할 수 있다.
- Immutable 자료형 : 변경 불가능 하다.
- 중복 데이터 저장이 가능하다.
- ()를 이용해서 만들 수 있다.
'''
tuples = ()
tuples

tuples = ("h","e","l","l","o")
tuples

tuples = "h","e","l","l","o"

type(tuples)

tuples[0]
tuples[::-1]

# 수정 불가
tuples[0] = "i"

num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
num_tuple[::2]  # 시작부터 2개 건뛰
num_tuple[1::2] # 1번 인덱스부터 2개 건뛰

# set
'''
- 데이터에 순번이 없어 인덱싱과 슬라이싱을 지원 안한다.
- mutable 자료형
- 중요한 특징으로 중복 데이터의 저장을 허용하지 않는다.
- {} 중괄호를 이용해서 만든다.
'''

sets= set()
type(sets)

sets = {1001, 1001, 1001, 1003, 1003, 1004, 3, 3, 3}
sets

# dict
'''
- mutable 자료형
- Key-Value 구조 자료형
- key는 중복을 허용하지 않는다.
- value는 중복 저장을 허용한다.
'''

city = {
    "한국" : "부산",
    "일본" : "교토",
    "캐나다" : "오타와"
}

city["한국"]

city
# 값 추가 가능
city["중국"] = "베이징"
city

# 수정 가능
city["일본"] = "도쿄"
city

# 함수와 메서드(Method)
'''
𝑓(𝑥)=2𝑥 

함수

코드의 반복을 줄이거나 어떠한 용도를 위해 특정 코드들을 모아둔 것
어떠한 결과를 만들어내는 코드의 집합
메소드: 객체에 소속된 형태의 함수
'''

lst = [10, 25, 2, 4]
max(lst)       # 최대값
min(lst)       # 최솟값
sum(lst)       # 합계
len(lst)       # 길이 반환
sorted(lst)    # 정렬

s = "ABCD"
s_lower = s.lower()
s_lower

# list 활용

# list의 메소드
'''
append()
리스트의 제일 뒤에 값을 추가한다.
'''
lst = [1, 2, 3, 4]
lst.append(0)
lst

'''
sort()
기본적으로 오름차순 정렬
reverse=True 설정하면 내림차순 정렬
'''
lst.sort()
lst.sort(reverse=True) # 내림차순

'''
pop()
제일 뒤에 있는 데이터를 꺼내고 삭제
인덱스 값을 줄경우 해당 인덱스의 값을 꺼내고 삭제(default : lastindex)
'''
lst = [1, 2, 3, 4]
print(lst.pop())
print(lst)

print(lst.pop())
print(lst)

print(lst.pop())
print(lst)

print(lst.pop(0))  # 0번 인덱스부터 삭제
print(lst)

'''
extend()
리스트와 리스트 합친다.(연결한다.)
'''
lst = [1, 2, 3]
lst.extend([4, 5, 6])
lst

'''
insert()
인덱스 위치에 값을 추가한다.
'''
lst = [1, 2, 3]
lst.insert(0, 9)   # (index, 값)
lst

'''
remove()
리스트에서 값을 찾아 삭제한다.
'''
lst = [1, 2, 3]
lst.remove(2)

'''
del 키워드
특정 인덱스 값을 삭제
'''
lst = [1, 2, 3]
del lst[0]

'''
count()
리스트안에 객체(요소)의 빈도수를 반환해준다.
'''
lst = [1, 2, 3, 3, 3, 3, 4, 5, 5]
lst.count(3)

# lst의 연산
'''
더하기 연산을 이용한 리스트 연결
extend 와 같은 결과
다른 점은 원본 리스트를 변경하지 않고 새로은 리스트가 생기는 개념
'''
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst1 + lst2

lst1 + [6]

lst1 * 3

2 in lst1

100 in lst1

100 not in lst1

lst1 == [1, 2, 3]
lst1 != [1, 2, 3]

# tuple 활용
# tuple의 메소드
'''
count()
튜플 안에 객체(요소)의 빈도수를 반환해준다.
'''
tup = (1, 2, 3, 3, 3, 2, 1, 1, 1)
tup.count(2)

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup1 + tup2

3 in tup1
3 not in tup1
tup1 == tup2
tup1 != tup2

# set 활용
# set의 메소드
A = {1, 2, 3}
B = {2, 3, 4}
A
B
'''
intersection()
교집합을 반환한다.
'''
A.intersection(B)

'''
union()
합집합을 반환한다.
'''
A.union(B)

'''
difference()
차집합을 반환환다.
'''
A.difference(B)

'''
add()
객체(요소)를 추가할수 있다.
중복 요소 일 경우 추가 되지 않는다.
'''
a = {1, 2, 3}
a.add(4)
a

'''
update()
여러 객체(요소)들을 추가할수 있다.
중복 요소는 제외되고 추가 된다.
'''
a.update([1, 2, 3, 4, 5, 6])
a


'''
remove()
값을 기준으로 삭제한다.
'''
a.remove(4)
a

# dict 활용
# dict의 메소드
city = {
    "한국" : "부산",
    "일본" : "교토",
    "캐나다" : "오타와"
}

'''
get()
dict 자료형에 없는 key의 value 를 가져오면 에러가 발생한다.
에러를 방지하기 위해 유용하다.
'''
city["중국"]
city.get("중국")
city.get("중국", "없음")

'''
update()
dict 자료형에 dict 자료형을 추가할때 사용한다.
동일한 key가 있을 경우 value 가 수정되고, 없을 경우 추가된다.
'''
add_city = {"중국": "상하이", "미국" : "워싱턴"}
city.update(add_city)
city

'''
pop()
key의 value 를 반환 하면서 지정한 key와 value를 삭제한다.
'''
print(city.pop("중국"))
city

'''
keys()
dict 자료형의 전체 key 를 확인할수 있다.
'''
city.keys()

'''
values()
dict 자료형의 전체 value 를 확인할수 있다.
'''
city.values()

'''
items()
dict 자료형의 전체 key 와 value 를 확인할수 있다.
key 와 value는 튜플 형태로 묶인다.
'''
city.items()
"한국" in city.keys()
"서울" not in city.values()

num_dict = {
    0:"제로",
    3.14:"원주율"
}
num_dict[3.14]
num_dict[0]

info_dict = {
    "name" : "유지현",
    "score" : [100, 100, 100, 100, 100],
    "etc" : {
        "my_dream" : "hecker",
    }
}
info_dict

num_dict = {
    "mean" : 80,
    "std" : 3.5,
}
num_dict["avg"] = num_dict.pop("mean")
num_dict

# 컬렉션 자료형의 변환

#  lst -> tuple
lst = [1, 2, 3]
tuple(lst)

# tuple -> lst
tup = 1, 2, 3
list(tup)

# lst -> set
lst = [1, 1, 2, 3, 4, 4, 5, 6, 6]
set(lst)

# set -> lst
sets = {"Apple", "Banana", "Mango"}
list(sets)

# dict -> list
city = {
    "한국" : "부산",
    "일본" : "교토",
    "캐나다" : "오타와"
}
list(city)
list(city.keys())
list(city.values())

city.items()
tup_list = list(city.items())
tup_list
dict(tup_list)

text = "hello"
list(text)

# str 활용
'''
큰따옴표로 문자열을 생성한경우
문자열안에 큰따옴표를 넣고 싶을때는 \ 기호를 따옴표 앞에 붙이면 문법오류가 발생하지 않는다.
작은 따옴표도 동일한 방식으로 하면 된다.
'''
text = "빅데이터 기초 \"프로그래밍\" 강의"
print(text)

text = """ '빅데이터' 기초 "프로그래밍" 강의"""
print(text)

text = "hello"
text[-1]
text[::-1]

text1 = "hello"
text2 = "world"
print(text1 + text2)

text1 * 10

"d" in text2
"d" not in text2

'''
문자열 포매팅(String Formatting)
문자열 내의 특정한 값을 변수로 부터 동적으로 문자열을 생성
'''
name = "철수"
age = 25

text = "제 이름은 " + name + '입니다. 나이는 ' + str(age) + "입니다."
print(text)

text = "제 이름은 {}입니다. 나이는 {}입니다."
print(text.format(name, age))

text = f"제 이름은 {name}입니다. 나이는 {age}입니다."
print(text)

# str의 메소드
# 대문자 or 소문자 변환
text = "hello Python"
text.upper()
text.lower()

# 문자열 치환
text = "Hello Python"
text.replace("P", "C")

# 문자열 분리
text = "Hello Python"
text.split()

text = "Hello#Python"
text.split("#")

# 문자열의 좌우 공백 제거
text = "    Hello Python   "
print(text.strip())

# 문자열 연결하기
lst = ['오늘', '하루', '너무', '행복하다']
"#".join(lst)

# 시작 여부 반환
text = "빅데이터 기초 프로그래밍 강의"
text.startswith("빅데이터")

# 종료 여부 반환
text = "빅데이터 기초 프로그래밍 강의"
text.endswith("강의")