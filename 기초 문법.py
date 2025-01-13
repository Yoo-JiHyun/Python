print("hello world!")
'''
- 값
    - 객체
    - 프로그래밍에서 처리(연산)하는 대상
    - 수, 문자, 이미지, 음성 등등
- 변수
    - 값(객체)을 담을수 있는 공간
    - 객체의 위치(주소)를 갖고 있는 공간
- 키워드
    - 파이썬에서 이미 예약되어있는 예약어
    - 코드를 제어할 수 있는 조건문이나 반복문, 함수나 클래스 등을 만들기 위해 파이썬 문법적인 요소로 정의되어 있다.
'''
# 객체 생성
1004

# 변수, 객체 생성
x = 1004
x

y = x
y

# id값
id(x), id(y)

# 변수 활용
n=9
print(n*1)
print(n*2)
print(n*3)
print(n*4)
print(n*5)
print(n*6)
print(n*7)
print(n*8)
print(n*9)

# 대소문자 구분
A = 3
a = 1
A,a

a = 100
print(a)

# 자료형
a = 1
type(a)
b = 3.14
type(b)
c = True
d = False
type(c) , type(d)
e = "hello"
type(e)

int_value = 3
float_value = 3.14
bool_value = True
str_value = "3"

# 자료형변환
int(float_value)
float(int_value)
str(float_value)
bool(int_value)
bool(0)

# None 값
a = None
a

# 산술 연산자
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2)
print(5%2)
print(5**2)

# 대입 + 산술
num = 3
# num = num - 3
num -= 3
num

# 비교 연산자
a = 5
b = 3
print(a > b)
print(a < b)
print(a >= 5)
print(b <= 3)
print(a == b)
print(a != b)

# 논리 연산자
1 < 3 and 3 > 1
False or False
False or True

# 포함 연산자
"a" in "abcd"
"a" not in "abcd"

