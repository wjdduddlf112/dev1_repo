#list
# - 컨테이너 자료형
# - list, tuple, dict, set ...
# 저장된 순서를 기억 (인덱스)
# - 슬라이싱 제공

lst = [1,2,3]
print(lst, type(lst))

print(lst[0],lst[1], lst[2])

#list는 요소를 추가.삭제 가능한 mutable(가변) 자료형

lst.append(4)
print(lst, id(lst))

#원하는 인덱스에(위치)에 요소를 추가
lst.insert(1,1.5)
lst.insert(0,0)
print(lst)

#값 변경
lst[0] = -1
print(lst)

#특정 인덱스 값 삭제
lst.pop(2)
print(lst)

del lst[1]
print(lst)
