# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 조건문을 사용합니다.
if number % 2 == 0:
    # 조건이 참일 때, 즉 짝수 조건
    print("짝수입니다")
else:
    # 조건이 거짓일 때, 즉 홀수 조건
    print("홀수입니다")
    
#----------------------------------------------------------------
    
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구하고
# 쉽게 사용할 수 있게 월을 변수에 저장합니다.
now = datetime.datetime.now()
month = now.month

# 조건문으로 계절을 확인합니다.
if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")
    
#----------------------------------------------------------------

# 변수를 선언합니다.
score = float(input("학점 입력> "))

# 조건문을 적용합니다.
if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자")
elif 2.8 <= score < 3.5:
    print("일반인")
elif 2.3 <= score < 2.8:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자")
elif 1.0 <= score < 1.75:
    print("불가촉천민")
elif 0.5 <= score < 1.0:
    print("자벌레")
elif 0 < score < 0.5:
    print("플랑크톤")
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗")
    
#----------------------------------------------------------------

# 변수를 선언합니다.
score = float(input("학점 입력> "))

# 조건문을 적용합니다.
if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")