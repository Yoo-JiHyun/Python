# numpy 패키지의 주요 장점
# 매우 빠른 데이터 생성 및 처리가 가능
# list자료형보다 효율적으로 저장하고 사용할 수 있는 자체 내장 데이터 구조(array)
# 반복문 없이 데이터 배열 처리 가능

# 설치 : pip install numpy
# 삭제 : pip uninstall numpy
# 사용 : import numpy as np

# 패키지를 사용하기 위한 최초 1회 실행
import numpy as np

# Create
# list 자료형을 numpy array 로 변환

a_list = [1,2,3,4,5]
a1 = np.array(a_list)
a1, type(a1)

# Create
sample_list = [1, 2, 3]
np_array = np.array(sample_list)
print(np_array)
print(type(np_array))

# Create
sample_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
np_2d_array = np.array(sample_list, dtype='str')
print(np_2d_array)
print(type(np_2d_array))

# Create
np.arange(0,5) # array([0, 1, 2, 3, 4])

np.arange(1,11,2) # array([1, 3, 5, 7, 9])

np.zeros(4) # array([0., 0., 0., 0.])

np.ones(5) # array([1., 1., 1., 1., 1.])

np.zeros((2,2)) # array([[0., 0.], [0., 0.]])

# Create
np.linspace(0, 1, 10) # 0 - 1 사이 구간 숫자를 같은 간격의 숫자 10개를 표현

# Create
np.eye(1)
np.eye(2)
np.eye(3)

# Create
np.full((3,3), 99)  # 임의의 숫자로 채움 (99)

# list vs np.array()
a = [1,2]
a*10

a = np.array([1,2])
a*10

# Create
# 난수 생성
sample_size = 7
np.random.seed(10)  # 같은 난수 반복 (재현)
np.random.rand(sample_size)

# Create
# 평균 0, 표준편차 1을 가지는 표준 정규 분포에서 난수 생성
sample_size = 7
data = np.random.randn(sample_size)
data

# Create
# 3 ~ 9사이의 정수를 7개 추출
np.random.randint(3, 10, 7)

# Read
simple_array = np.array([1, 2, 3, 4])

# 요소 값 중 최대, 최소값 출력
print(simple_array.max())
print(simple_array.min())

# 요소 값 중 최대, 최소값의 index 출력
print(simple_array.argmax())
print(simple_array.argmin())

# Read
# python의 ragne()와 유사한 함수
# 3번째 인덱스 값 변경
x = np.arange(10)
x[3] = 100
print(x)

# Read
# 2차원 데이터 인덱싱과 슬라이싱
mat = np.array([[5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]])

print(mat)
print('-' * 20)
print(mat[0])
print('-' * 20)
print(mat[0][-1])
print('-' * 20)
print(mat[1:][:2])

# Update
arr = np.array([0,1,2,3,4,5])
arr.reshape(2, 3)

# Read
x = np.arange(24)
print(x)

# Read
x = np.arange(24).reshape(3, 4, 2)  # reshape 형태 변경
print(x)
x[:1, :2]

# Update
arr = np.arange(4)
# 덧셈 (np.add)
2 + arr
#Returns array([2, 3, 4, 5])
arr + arr
#Returns array([0, 2, 4, 6])


arr = np.arange(4)
# 뺄셈 (np.subtract)
arr - 10
#Returns array([-10,  -9,  -8,  -7])
arr - arr
#Returns array([0, 0, 0, 0])


arr = np.arange(4)
# 곱셈 (np.multiply)
6 * arr
#Returns array([ 0,  6, 12, 18])
arr * arr
#Returns array([0, 1, 4, 9])

arr = np.arange(4)
# 나눗셈 (np.divide)
arr / 2
#Returns array([0. , 0.5, 1. , 1.5])
arr / arr
#Returns array([nan,  1.,  1.,  1.])

# Update
# 제곱근 연산
arr = np.arange(4)
np.sqrt(arr)
# array([0.        , 1.        , 1.41421356, 1.73205081])

# 지수연산
arr = np.arange(4)
np.exp(arr)
# array([ 1.        ,  2.71828183,  7.3890561 , 20.08553692])

# 삼각함수연산 (sine)
arr = np.arange(4)
np.sin(arr)
# array([0.        , 0.84147098, 0.90929743, 0.14112001])

# 삼각함수연산 (cosine)
arr = np.arange(4)
np.cos(arr)
# array([ 1.        ,  0.54030231, -0.41614684, -0.9899925 ])

# 삼각함수연산 (logarithm)
arr = np.arange(4)
np.log(arr)
# array([      -inf, 0.        , 0.69314718, 1.09861229])

# 반올림
arr = np.random.rand(5)
np.round(arr, 2)
# array([0.13, 0.05, 0.89, 0.7 , 0.91])

# Read
# Pillow 패키지를 이용한 이미지 데이터 불러오기
from PIL import Image

data = Image.open('/Users/lyujihyun/Python/데이터분석과시각화/data/티라노.jpg')
data

# 이미지 데이터를 numpy array 로 변환
data_np = np.array(data)
data_np.shape

# 이미지 데이터의 일부를 crop (짤라내다)
part_img = data.crop((0, 0, 150, 150))  # (0, 0) 위치와 (150, 150) 위치의 사각영역을 짤라내기
part_img

# 원본 이미지를 흑백이미지로 변경
data_gray = data.convert('L')
data_gray

# 원본 이미지를 numpy array 로 변경 후 데이터 크기 확인
# 3차원 데이터가 2차원 데이터로 변경 (컬러 이미지 -> 흑백 이미지)
np.array(data_gray).shape

# 흑백 이미지 출력
import matplotlib.pyplot as plt
plt.imshow(data_gray)
# 원본 이미지 출력
plt.imshow(data)
# 짜른 이미지 출력
plt.imshow(part_img)