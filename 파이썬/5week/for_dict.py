# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# for 반복문을 사용합니다.
for key in dictionary:
    # 출력합니다.
    print(key, ":", dictionary[key])
    
#----------------------------------------------------------------

print("# 동일 요소 개수 출력")
numbers = [1, 2, 3, 2, 1, 2, 4, 2, 3, 4, 5, 3, 2, 3, 4, 2, 3, 2, 3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] =+ 1
    else:
        counter[number] = 1
print(counter)