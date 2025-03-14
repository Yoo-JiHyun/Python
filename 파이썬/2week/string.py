# format()
string_a = "{}".format(10)

print(string_a)
print(type(string_a))

format_a = "{}만 원".format(5000)
format_b = "열심히 공부하여 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

"{} {}".format(1, 2, 3, 4, 5)
"{} {} {}".format(1, 2)
'''IndexError: Replacement index 2 out of range for positional args tuple'''

# :d -> 정수
output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

# 기호와 함께 출력하기
output_f = "{:+d}".format(52)   # 양수
output_g = "{:+d}".format(-52)  # 음수
output_h = "{: d}".format(52)   # 양수 : 기호 부분 공백 (양수일 경우 공백)
output_i = "{: d}".format(-52)  # 음수 : 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

# 조합하기
output_h = "{:+5d}".format(52)      # 기호를 뒤로 밀기: 양수
output_i = "{:+5d}".format(-52)     # 기호를 뒤로 밀기: 음수
output_j = "{:=+5d}".format(52)     # 기호를 앞으로 밀기: 양수
output_k = "{:=+5d}".format(-52)    # 기호를 앞으로 밀기: 음수
output_l = "{:+05d}".format(52)     # 0으로 채우기: 양수
output_m = "{:+05d}".format(-52)    # 0으로 채우기: 양수

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

# :f -> 실수
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)      # 15칸 만들기
output_c = "{:+15f}".format(52.273)     # 15칸에 부호 추가하기
output_d = "{:+015f}".format(52.273)    # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)

output_a = "{:15.3f}".format(52.273)    # 소수점 3자리
output_b = "{:15.2f}".format(52.273)    # 소수점 2자리
output_c = "{:15.1f}".format(52.273)    # 소수점 1자리 (반올림)

print(output_a)
print(output_b)
print(output_c)

# :g -> 의미없는 소수점 제거
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)

# strip() -> 의도하지 않은 줄바꿈 등 제거
input_a = """
    안녕하세요
문자열 함수를 알아봅시다.
"""
print(input_a)
print(input_a.strip())

# is__() -> 문자열이 각각 소문자, 알파벳, 숫자로만 구성되어 있는지 확인함
# Boolean
print("Lst0531".isalnum())
print("0531".isdigit())

# find() -> 왼쪽부터 처음 등장 위치 찾음
# rfind() -> 오른쪽부터 처음 등장 위치 찾음
output_a = "안녕안녕하세요".find("안녕")
print(output_a)
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

# in 연산자 -> 내부에 변수가 포함되어있는지 확인
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

# split() -> 문자열을 특정한 문자로 자름
a = "10 20 30 40 50".split(" ")
print(a)    # list 형태로 출력
