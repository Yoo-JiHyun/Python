print(109)
print(type(109))    # 정수

print(78.25)
print(type(78.25))  # 실수

print("4 + 5 =", 4 + 5)
print("4 - 5 =", 4 - 5)
print("4 * 5 =", 4 * 5)
print("4 / 5 =", 4 / 5)

print("6 / 3 =", 6 / 3)
print("6 // 3 =", 6 // 3)   # 정수 값만 출력

print("7 % 3 =", 7 % 3)

print("2 ** 1 =", 2 ** 1)
print("2 ** 2 =", 2 ** 2)
print("2 ** 3 =", 2 ** 3)
print("2 ** 4 =", 2 ** 4)

# 연산자의 우선순위
# *, / > +, -
print(2 + 2 - 2 * 2 / 2 * 2)
print(2 - 2 + 2 / 2 * 2 + 2)

# 괄호를 활용하여 우선순위 조정
print((5 + 3) * 2)

# 서로 다른 자료를 연산할 경우
string = "문자열"
number = 109
string + number
'''TypeError: can only concatenate str (not "int") to str'''

# 복합 대입 연산자
# 숫자 (+=, -=, *=, /=, %=, **=)
number = 100
number += 10
number += 20
number += 30
print("number : ", number)

# 문자열 (+=, *=)
string = "안녕하세요"
string += "!"
string += "?"
print("string : ", string)
