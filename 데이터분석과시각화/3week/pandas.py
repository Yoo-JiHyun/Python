# pandas 패키지의 주요 특징 및 장점
# DataFrame, Series 객체로 구성됨
# 다양한 파일 포맷 입출력 가능
# 빠른 속도
# 데이터 셋트의 유연한 형상 조작 및 피봇팅 가능

# 설치 : pip install pandas
# 삭제 : pip uninstall pandas
# 사용 : import pandas as pd

# 패키지를 사용하기 위한 최초 1회 실행
import pandas as pd

# Create
sample_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
df1 = pd.DataFrame(sample_list)
print(df1)

df2 = pd.DataFrame(sample_list, columns=['no1', 'no2', 'no3'])
print(df2)

# Create
sample_dict = {
    'col1': [11,12,13,14],
    'col2': [21,22,23,24],
    'col3': [31,32,33,34],
}
df = pd.DataFrame(sample_dict)
df

# Create
sample_dict = {
    'col1': [11,12,13,14],
    'col2': [21,22,23,24],
    'col3': [31,32,33,34],
}
df = pd.DataFrame(sample_dict)
print(df)

# Create
pd.DataFrame(np.random.randn(6, 4))

# Read
import pandas as pd

sample_dict = {
    'col1': [11,12,13,14],
    'col2': [21,22,23,24],
    'col3': [31,32,33,34],
}
df = pd.DataFrame(sample_dict)
print(df)

df.loc[2] # 2번째 행
df.loc[2:] # 2번째 행부터 끝까지
df.loc[:2] # 처음부터 2번째 행까지
df[df.col1 == 13] # 첫행이 13인 행
df.T # 트랜스포즈 효과 (행렬 뒤바꿈 변경, 전치)

# Read
sample_dict = {
    'col1': [22,22,33,14],
    'col2': [21,22,33,24],
    'col3': [11,12,56,67],
}
df = pd.DataFrame(sample_dict)

df.head()
df.tail()
df.shape
df.describe()

df.col1.value_counts()
df.col1.value_counts(normalize=True)

df.info()
df.info(verbose=True) # null 컬럼 출력

df['col1'].unique()
df['col1'].nunique()
df['col1'].isin([22,12])
df.loc[df['col1'].isin([22,12]), :]

# Update
sample_dict = {
    'col1': [22,22,33,14],
    'col2': [21,22,33,24],
    'col3': [11,12,56,67],
}
df = pd.DataFrame(sample_dict)

df.reset_index(drop=True)

# Update
df.columns = ['change_col1', 'change_col2', 'change_col3']
df

# Update
df = df.add_prefix('ks_')   # 컬럼 이름 추가
df

# Update
sample_dict = {
    'col1': [11,12,13,14],
    'col2': [21,22,23,24],
    'col3': [31,32,33,34],
}
df = pd.DataFrame(sample_dict)

df.loc[1] = [41, 51, 61] # 행 추가 방법

df = df.append({'col1': 41, 'col2': 51, 'col3': 61}, ignore_index=True) # 행 추가 다른 방법

df['col_sum'] = 0 # 열 추가 방법

df

# Update
sample_dict = {
    'col1': [11,12,13,14],
    'col2': [21,22,23,24],
    'col3': [31,32,33,34],
}
df = pd.DataFrame(sample_dict)

df.loc[1, 'col1'] = 99 # 행,렬접근으로 변경
df['col1'] = [91, 92, 93, 94] # 특정 열 전체 변경
df.loc[1] = [99, 99, 99] # 특정 행 전체 변경

df

# Delete
sample_dict = {
    'col1': [11,12,13,14],
    'col2': [21,22,23,24],
    'col3': [31,32,33,34],
}
df = pd.DataFrame(sample_dict)

# del df['col1']

df.drop(columns=['col2', 'col3'], axis=0, inplace=True)

df = df.drop([df.index[1]]) # index 기준으로 삭제

target_index = df[df.col1 == 13].index # 특정 데이터 조회결과에 따라 삭제
df = df.drop(target_index)

df

# Delete
sample_dict = {
    'col1': [11,12,13,np.NaN],
    'col2': [21,None,23,24],
    'col3': [31,32,np.nan,34],
}
df = pd.DataFrame(sample_dict)

df.isnull()
df.notnull()

df = df.fillna(value=99.99) # 결측치 채우기

df = df.dropna(how='any')   # 결측치 행/열 삭제
df = df.dropna(how='all')

df

# Delete
sample_dict = {
    'col1': [11,22,22,24],
    'col2': [21,22,22,24],
    'col3': [31,22,22,34],
}
df = pd.DataFrame(sample_dict)

df.duplicated()
df.duplicated(keep='first') # first, last, False

df = df.drop_duplicates(keep='first') # first, last, False

df

# 데이터 이해
'''
Domain Knowledge
타이타닉 데이터셋을 이용한 데이터 전처리
전처리 아이디어
전처리 아이디어를 실행하기 위한 pandas 패키지 활용
'''

# 문제
'''
불필요한 데이터 삭제
범주형 데이터 수치형 변환
수치형 데이터 평준화(정규화)
결측치 처리
이상치 처리
자료형 통일
중복데이터 처리
'''

# 분석에 필요한 패키지 로드
import pandas as pd

# 분석에 필요한 데이터 로드
titanic = pd.read_csv('/Users/lyujihyun/Python/데이터분석과시각화/data/titanic.csv')
titanic

# 불필요한 컬럼 제거
titanic = titanic.drop(columns=['PassengerId'], axis=0)
titanic

# 데이터의 컬럼정보, 결측치, 데이터 타입 등 확인
titanic.info()

# 결측치 데이터 행 삭제
titanic = titanic.dropna()
titanic

# 중복 데이터 존재여부 확인
titanic[titanic.duplicated()]

# Embarked 컬럼의 종류와 각각의 갯수 확인
titanic.Embarked.value_counts()

# Embarked 컬럼 값을 치환
map_value = {'S': 0, 'C': 1, 'Q': 2}
titanic['Embarked'] = titanic.Embarked.map(map_value)
titanic