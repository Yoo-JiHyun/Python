# 리스트를 선언합니다.
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 출력합니다.
print("# 리스트")
print("list_a = ", list_a)
print("list_b = ", list_b)
print()

# 기본 연산자
print("# 리스트 기본 연산자")
print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

# 함수
print("# 길이 구하기")
print("len(list_a) = ", len(list_a))

#----------------------------------------------------------------

# 리스트를 선언합니다.
list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

#----------------------------------------------------------------

list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거 방법[1] – del
del list_a[1]
print("del list_a[1]:", list_a)

# 제거 방법[2] – pop()
list_a.pop(2)
print("pop(2):", list_a)

del list_a[3]
print("list_a : ", list_a)

#----------------------------------------------------------------

list_c = [1, 2, 1, 2]
print("# 리스트.remove(값)")
list_c.remove(2)
print("list_c : ", list_c)

list_e = [52, 273, 103, 32, 275, 1, 7]
print("# 오름차순")
list_e.sort()
print("list_e : ", list_e)
print("# 내림차순")
list_e.sort(reverse=True)
print("list_e : ", list_e)
