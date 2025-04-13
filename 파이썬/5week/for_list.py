# 리스트를 선언합니다.
array = [273, 32, 103, 57, 52]

# 리스트에 반복문을 적용합니다.
for element in array:
    # 출력합니다.
    print(element)
    
    
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