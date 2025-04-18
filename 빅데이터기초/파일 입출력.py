# 파일 입출력
'''
open 함수: 파일을 열수 있는 함수, 파일 객체를 반환한다.
파일열기 모드는 대표적으로 다음과 같다.
    w: 쓰기 모드
    a: 추가 모드
    r: 읽기 모드
open 함수로 열면 파일 객체가 반환 되는데 파일에 대한 처리가 종료되면 항상 close 메소드를 이용해서 닫아줘야한다.
'''
# 쓰기 모드

# 추가 모드

# 읽기 모드
# read 메소드
# 파일 내용 전체를 문자열로 반환한다.

# readline 메소드
# 한줄씩 문자열로 반환한다.(한줄에 포함되어있는 개행문자 포함)

# readlines 메소드
# 한줄씩 리스트에 담아 반환한다.(각줄에 개행문자 포함)

# with문
# 자동으로 파일을 닫아준다.

# for 문을 이용해서 한줄씩 출력하기

# JSON(JavaScript Object Notation)
'''
자바스크립트에서 사용되는 객체 표현식
데이터를 저장하거나 전송할때 많이 사용
서버와 클라이언트간의 데이터 전송과정에서 많이 사용
파이썬의 딕셔너리와 매우 유사
'''

# pickle 모듈
'''
우리가 사용하는 다양한 객체들을 파일로 저장하고 싶다면?
객체의 구조를 직렬화해서 파일로 저장한다.
보통 딕셔너리, 리스트 등을 저장하고 불러올때 사용한다.
'''

