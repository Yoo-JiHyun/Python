# 변수
pi = 3.14159265
pi + 2
pi - 2
pi * 2
pi / 2
pi % 2
pi * pi

# input()
input("인사말을 입력하세요 >> ")

string = input("인사말을 입력하세요 >> ")
print(string)

print(type(string))
number = input("숫자를 입력하세요 >> ")
print(number)
print(type(number))

# Cast 자료형변환
# int()
string_a = input("입력A")
int_a = int(string_a)

string_b = input("입력B")
int_b = int(string_b)

print("문자열 자료 : ", string_a + string_b)
print("숫자형 자료 : ", int_a + int_b)

# str()
output_a = str(52)
output_b = str(52.273)
print(type(output_a), output_a)
print(type(output_b), output_b)

# inch -> cm
raw_input = input("inch 단위의 숫자를 입력해주세요.>> ")

inch = int(raw_input)
cm = inch * 2.54

print(inch, "inch는 cm 단위로", cm, "cm입니다.")