
'''명령어와 데이터
▶ 명령어
컴퓨터의 특정 작업 또는 데이터를 이용하여 문제를 해결하기 위한 작업
▶ 데이터
명령어가 실행될 때 사용하기 위한 자료

자료형
변수와 상수
변수 : 자료(데이터)를 저장하는 기억장소의 위치
상수 : 기억장소에 저장되는 자료(데이터)'''

# a1 : 변수
# 100 : 상수
a1 = 100  
print(a1) # a1변수가 가지고 있는 값 출력
     

# 주기억장소(메모리)에서의 a1변수 값의 위치(주소, address)
print(id(a1))
     

# b1변수에 100을 저장한 후 변수 값과 변수 값이 저장된 주기억장소 주소(address)를 출력 (위와 동일)
b1 = 100
print(b1, id(b1))
     

# b1변수 값을 변경하고 b1변수 값과 변수 값의 주소를 다시 출력하면 주소가 변경된 것을 알 수 있습니다.
b1 = 200
print(b1, id(b1))
     

# a1변수에 200을 저장한 후 변수 값과 변수 값의 주소를 출력 (위와 동일)
a1 = 200
print(a1, id(a1))
     
'''따라서 동일한 데이터를 여러 변수에 할당해도 메모리에는 하나의 데이터만 저장된다.'''

# 자료형
# 숫자형
# 0~9 및 소수점(.), 언더바(_)로 구성된 데이터

n1 = 100
n2 = 20.2
n3 = 100_000_000
print(n1)
print(n2)
print(n3)
     
# 문자형

# 따옴표에 들어가는 모든 데이터
# 따옴표는 큰 따옴표와 작은 따옴표를 일관되게 사용
# 단, 큰 따옴표안의 작은 따옴표는 문자로 인식하고 반대로 작은 따옴표안의 큰 따옴표도 문자로 인식
s1 = '100'
s2 = '20.2'
s3 = '100_000_000'
s4 = '"식사하세요"라고 말했다.'
s5 = "'식사하세요'라고 말했다."
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
     

# 숫자형 변수의 더하기
n1 + n2
     

# 문자형 변수의 더하기
s1 + s2
     
# 논리형

# 참, 거짓을 의미하는 데이터
b1 = True
b2 = False

print(b1, b2)
     

# True 값이 숫자와 연산을 하게 된다면 ?
b1 = True   # 값이 1
n1 = 3

print(b1 + n1)
     

# False 값이 숫자와 연산을 하게 된다면 ?
b1 = False  # 값이 0
n1 = 3

print(b1 + n1)
     

# False 값이 문자와 연산을 하게 된다면 ?
b1 = False
s1 = '3'

print(b1 + s1)
# TypeError: unsupported operand type(s) for +: 'bool' and 'str'
     
# ❓ 잠깐 ! 이런 생각을 해봅시다.
# 실험정신을 가지고 아래 코드의 실행결과를 예상하고 실행해 보세요.

# 만약 숫자와 문자를 더 한다면 ?
1 + 'a'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
     

# 만약 숫자와 문자를 더 한다면 ?
1 + '1'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
     

# 만약 숫자와 논리형을 더 한다면 ?
1 + True
     

# 만약 숫자와 논리형을 더 한다면 ?
1 + False
     

# 만약 숫자와 논리형을 더 한다면 ?
1 + True + False
     

# 만약 숫자와 논리형을 더 한 결과의 자료형은 ?
type(1 + True)
     

# 만약 문자와 논리형을 더 한다면 ?
'1' + True
# TypeError: can only concatenate str (not "bool") to str
     

# 만약 문자와 논리형을 더 한다면 ?
'a' + True
# TypeError: can only concatenate str (not "bool") to str
     
# 시퀀스 (문자열)

# Create
a = 'hello world'
a
     

# Create
a = 'hello world'
b = a + ' !!!!'
b
     

# Read
    # 01234567890
    #-10987654321
a = 'hello world'
b = a[:-2]  # 처음부터 ~ -2번 전 인덱스까지
b
     

# Read
a = 'hello world'
b = a[-2:]  # -2번 인덱스 ~ 끝까지
b
     

# Read
a = 'hello world'
b = a[2:5]  # 2번 인덱스 ~ 5번 인덱스 전까지
b
     

# Read
a = 'www.naver.com'
a.split('.')
     

# Read
a = 'hello world'
a.index('l')
     

# Read
a = 'hello world'
a.count('o')
     

# Update
a = 'hello world'
result = a.replace('ll', 'L')
result
     

# Update
a = 'hello world'
a.upper()
     

# Update
program_version = '20.3'
seed = 42

fname = f'submit_{program_version}_{seed}'
print(fname)
     

# Delete
a = 'hello world'
result = a.replace('l', '')
result
     
# 시퀀스 (리스트)

# Create
a = [1, 2, 3, 4, 5]
a
     

# Create
a = ['a', 'b', 'c', 'd', 'd']
a
     

# Create
a = [1, 2, 'a', 'b', 5]
a
     

# Create
a = [1, 2, 'a', 'b', True, False, 5]
a
     

# Create
a = [1, 2, 'a', 'b', True, False, 5, 6, [11, 12, 13], 8]
a
     

# Create
a = 'hello world'
a = list(a)
a
     

# Read
a = [1, 2, 'a', 'b', True, False, 5, 6, [11, 12, 13], 8]
a[0]
     

# Read
a = [1, 2, 'a', 'b', True, False, 5, 6, [11, 12, 13], 8]
a[8]
     

# Read
a = [1, 2, 'a', 'b', True, False, 5, 6, [11, 12, 13], 8]
a[:-2]
     

# Read
a = [1, 2, 'a', 'b', True, False, 5, 6, [11, 12, 13], 8]
a[-2:]
     

# Read
a = [1, 2, 'a', 'b', True, False, 5, 6, [11, 12, 13], 8]
a[2:5]
     

# Read
a = [1, 3, 6, 9, 12]
a.index(3)
     

# Read
a = [1, 2, 3, 4, 5, 10]
b = 10

b in a
     

# Read
a = [75, 55, 100, 95, 65]
a.sort()

a
     

# Read
a = [75, 55, 100, 95, 65]
b = sorted(a)
print(b)
     

# Update
a = [1, 2, 3, 4, 5]
a[2] = 10_000

print(a)
     

# Update
a = [1, 2, 3, 4, 5]
a.append(9)

print(a)
     

# Update
a = [1, 2, 3, 4, 5]
a.insert(0, 9)

print(a)
     

# Update
a = [1, 2, 3]
b = ['a', 'b', 'c']

a.extend(b)
print(a)
     

# Update
a = [1, 2, 3]
b = ['a', 'b', 'c']

a += b
print(a)
     

# Delete
a = [1, 2, 3, 4, 5]
a.remove(3) # 값을 이용한 삭제
print(a)
     

# Delete
original = [1, 2, 3, 4, 5]
pop_value = original.pop(2)

print(original)
print(pop_value)
     
# 시퀀스 (튜플)

# Create
a = (1, 2, 3, 4, 5)
a
     

# Create
a = (1, 2, True, 4, 5)
a
     

# Create
a = (1, 2, True, 'hello world', 5)
a
     

# Create
a = [1, 2, 'a', 'b', True, False, 5, 6, [11, 12, 13], 8]
b = tuple(a)
b
     

# Read
a, b, c, d = 100, 200, 300, 400
print(a, b, c, d)
print(b)
     

# Read
a = (1, 2, 'a', 'b', True, False, 5, 6, [11, 12, 13], 8)
a[2:5]
     
# 시퀀스 (range())
# 일정한 간격의 정수를 발생시키는 함수 또는 자료형

for x in range(5):
  print(x)
     

for x in range(1, 5):
  print(x)
     

for x in range(1, 5, 2):
  print(x)
     
# 딕셔너리

# Create
d1 = {'k1' : 'value1'}
print(d1)
     

# Create
d1 = {1 : 'value'}
print(d1)
     

# Create
# 오류가 발생한다. 단, k1변수가 값을 가지고 있는 경우 오류가 발생하지 않는다.
d1 = {k1 : 'value1'}
print(d1)
# NameError: name 'k1' is not defined. Did you mean: 'b1'?
     

# Create
# 오류가 발생한다. 단, value1변수가 값을 가지고 있는 경우 오류가 발생하지 않는다.
d1 = {'k1' : value1}
print(d1)
# NameError: name 'value1' is not defined
     

# Read
d1 = {1: 456.45, 2: 378.56, 3: 568.78, }
print(d1)
print(d1[1])
print(d1.values())
     

# Update
d2 = {1: 99}
d1.update(d2)
print(d1.values())
     

# Delete
del d1[1]
print(d1.values())
     
# 세트형

# Create
a = {1,2,3,4,5,6,7}
print(a)
     

# Create
a = {1,1,2,3,3,4,5,6,7}
print(a)
     

# Create
# 중복 값이 제거되는 효과가 있다.
a = (1,1,2,3,3,4,5,6,7)
print(a)

a = (1,1,2,3,3,4,5,6,7)
print(set(a))
     

# Read
a = {1, 2, 3}
b = {2, 3, 4}

print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a.difference(b)) # 차집합
print(a.issubset(b)) #부분 집합
     

# Read
for x in b:
    print(x)
     

# Read
3 in b
     

# Update
a = {'a', 'b', 'c'}
b = {1, 2, 3}

a.update(b)
print(a)
     

# Update
a = {2, 3, 4}
a.add(99)
a
     

# Update
a = {2, 3, 4}
a.update([99, 10])
a
     

# Delete
# remove()는 없는 값을 삭제하려는 경우 오류가 발생한다.
a = {2, 3, 4}
a.remove(3)
a
     

# Delete
# discard()는 없는 값을 삭제하려해도 오류가 발생하지 않는다.
a = {2, 3, 4}
a.discard(3)
a.discard(3)
a
     
# 변수 값 교환

# 숫자형 변수의 값 교환
a = 1
b = 2
a, b = b, a
a
     

# 문자형 변수의 값 교환
a = 'b'
b = 'a'
a, b = b, a
a
     
# 데이터별 자료형

# 텍스트 파일 데이터 불러오기
# 일반적으로 텍스트 형식의 데이터를 주기억장치로 불러오면 숫자와 문자형 데이터로 구성된다.
import pandas as pd
data = pd.read_csv('/Users/lyujihyun/Python/데이터분석과시각화/data/건강데이터.csv', encoding='euc-kr')
data
     

# 이미지 데이터 파일 불러오기 #1
# 일반적으로 이미지 데이터를 주기억장치로 불러오면 숫자형 데이터로 구성된다.
import imageio
data = imageio.imread('/Users/lyujihyun/Python/데이터분석과시각화/data/티라노.jpg')
print('이미지 크기 (행, 열, 색상)', data.shape)
print('이미지 파일 내용\n', data)
     

# 이미지 데이터 파일 불러오기 #2
# Pillow 패키지를 이용하여 이미지 데이터 로드 후 변수 값을 출력하면 이미지가 출력된다.
from PIL import Image
data = Image.open('/Users/lyujihyun/Python/데이터분석과시각화/data/티라노.jpg')
data
     

# 오디오 데이터 파일 불러오기 #1
# IPython 패키지를 이용하여 오디오 파일을 로드 후 재생 함수로 출력
import IPython.display as ipd
ipd.Audio('/Users/lyujihyun/Python/데이터분석과시각화/data/common_voice_en_africa_10053.wav')
     

# 오디오 데이터 파일 불러오기 #2
# librosa 패키지를 이용하여 오디오 파일을 로드 후 파일 크기와 sampling rate 출력
# sampling rate : 초당 획득한 소리의 갯수 (단위 Hz, 헤르츠)
import librosa
x, sr = librosa.load('/Users/lyujihyun/Python/데이터분석과시각화/data/common_voice_en_africa_10053.wav')
print('오디오 파일 크기 : ', x.shape)
print('sampling rate : ', sr)
     

# 오디오 파일을 로드 후 시각화 방법 #1
import matplotlib.pyplot as plt
import librosa.display

librosa.display.waveshow (x, sr=sr)
plt.show()
     

# 오디오 파일을 로드 후 시각화 방법 #2
import matplotlib.pyplot as plt
plt.plot(x)
plt.show()
     
'''위의 첫번째 오디오 파일 시각화는 x축이 시간이며, 두번째는 배열(array)의 index값이다.'''


# 오디오 데이터 파일 불러오기 #3
# scipy 패키지를 이용하여 오디오 파일을 로드 후 파일 크기와 sampling rate 출력
# librosa 패키지를 이용하여 오디오 파일을 로드 결과값이 반대이다.
from scipy.io import wavfile

samplerate, data = wavfile.read('/Users/lyujihyun/Python/데이터분석과시각화/data/common_voice_en_africa_10053.wav')
print(f'- sampling rate: {samplerate}Hz')
print(f'- data shape : {data.shape}')
     

# 오디오 파일을 로드 후 시각화
import matplotlib.pyplot as plt
plt.plot(data)
plt.show()
     
# 제어문
# 반복문 - for

# 0 ~ 9까지 숫자를 생성하면서 10회 실행
for x in range(10):
  print(x)
     
# 반복문 - while

# 0 ~ 5까지 숫자를 생성하면서 5회 실행
a = 0
while a < 5:
  print(a)
  a = a + 1
     
# 조건문 - if (if ~ elif ~ else)

# a 값과 b 값을 비교
a = 100
b = 200
if a > b:
  print('big a')
  
     

# a 값과 b 값을 비교
a = 100
b = 200
if a < b:
  print('big b')
  
     
# 문제해결 활용
# 1부터 100까지 더한 결과를 출력하세요.

# 고전적인 1 ~ 100까지 더하는 프로그램
sum_value = 0
for i in range(101):
    sum_value = sum_value + i

print(sum_value)
     

# 함수를 생성하여 재사용이 가능하게 변경한 프로그램
def sum_1ton(n):
    sum_value = 0
    for i in range(1, n+1):
        sum_value += i
    return sum_value

print('1~10까지의 합', sum_1ton(10))
print('1~100까지의 합', sum_1ton(100))
     

# Bad Case
# 클래스를 생성하여 재사용이 가능하게 변경한 프로그램
class sum_1ton:
    def __init__(self, n):
        self.n = n
    def sum(self):
        sum_value = 0
        for i in range(1, self.n+1):
            sum_value += i
        return sum_value

obj_1 = sum_1ton(10)
obj_2 = sum_1ton(100)
print(obj_1.sum())
print(obj_2.sum())
     

# Good Case
# 클래스를 생성하여 재사용이 가능하게 변경한 프로그램
class sum_1ton:
    def sum(self, n):
        sum_value = 0
        for i in range(1, n + 1):
            sum_value += i
        return sum_value

obj_0 = sum_1ton()
print(obj_0.sum(10))
print(obj_0.sum(100))
     
'''Good Case인 이유는 객체를 한개만 생성하기 때문에 메모리 점유를 줄일 수 있기 때문'''

# id() 함수를 이용하여 확인해 보세요.

# 문자열 압축하기
# 입력 값 : abcccccdddd
# 기대 결과 값 : a1b1c5d4

# 고전적인 방법의 프로그램 코드
s = 'abcccccdddd'
a = '' 
cnt = 0 
for i in s: 
    if a == '':
        a = i 
        cnt += 1 
    else: 
        if a == i: 
            cnt += 1 
        else: 
            print(a + str(cnt), end='') 
            cnt = 0 
            a = i 
            cnt += 1 

print(a + str(cnt)) 

     
# s의 문자열 구성에 순서가 없다면 ? 아래와 같은 코드가 Good 코드

# python 언어에서 제공하는 자료형의 특성을 이용한 Good 코드
# set() 자료형의 중복제거 효과와 count()를 이용한 데이터 병합 응용
s = 'abcccccdddd'
a = set(s)

t = ''
for x in a:
    b = x + str(s.count(x))
    t = t + b
t
     

# 2개 이상의 시퀀스 자료형 데이터를 각 요소별 zip() 함수를 이용하여 데이터 병합(merge)
# 고전적인 for 문 사용
a = {'a', 'b', 'c'}
b = {1, 2, 4}

all_result = ''
for x in zip(a, b):
    result = str(x[0]) + str(x[1])
    all_result += result

''.join(all_result)
     

# 2개 이상의 시퀀스 자료형 데이터를 각 요소별 zip() 함수를 이용하여 데이터 병합(merge)
# python 언어의 list comprehension 사용 (가독성은 낮아지지만 코드가 간결해짐)
a = {'a', 'b', 'c'}
b = {1, 2, 4}

''.join([x[0]+str(x[1]) for x in zip(a, b)])
     