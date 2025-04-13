# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 출력합니다.
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

# 값을 변경합니다.
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])

#----------------------------------------------------------------

# 딕셔너리를 선언합니다.
dictionary = {}

# 요소 추가 전에 내용을 출력해 봅니다.
print("요소 추가 이전:", dictionary)

# 딕셔너리에 요소를 추가합니다.
dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

# 출력합니다.
print("요소 추가 이후:", dictionary)

#----------------------------------------------------------------

# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

# 요소 제거 전에 내용을 출력해봅니다.
print("요소 제거 이전:", dictionary)

# 딕셔너리의 요소를 제거합니다.
del dictionary["name"]
del dictionary["type"]

# 요소 제거 후에 내용을 출력해봅니다.
print("요소 제거 이후:", dictionary)

#----------------------------------------------------------------

dictionary = {
    "name": "유부",
    "age": "3"
}
print("유부 정보 :", dictionary)

dictionary["breed"] = "진도믹스"
print("정보 업데이트 :", dictionary)