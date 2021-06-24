# 나도코딩 파이썬 5-1 ~ 5-6

# 리스트
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))
subway.append("하하")
subway.insert(1, "정형돈")
print(subway.pop())
print(subway)
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
num_lst = [5,2,4,3,1]
num_lst.sort()
print(num_lst)
num_lst.reverse()
print(num_lst)
num_lst.clear()
print(num_lst)
mix_lst = ["조세호", 20, True]
print(mix_lst)
num_lst = [1,2,3,4,5]
num_lst.extend(mix_lst)
print(num_lst)

# 사전 Dict
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet)
print(cabinet[3], cabinet[100]) # key가 없을 경우 오류 발생
print(cabinet.get(5, "사용 가능")) # key가 없으면 None으로 출력
print(3 in cabinet)
print(5 in cabinet)
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"], cabinet["B-100"])
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)
del cabinet["A-3"]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()
print(cabinet)

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0], menu[1])
# menu.add("생선까스") 튜플은 추가 제거 불가
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 집합 (set) - 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])
print(java & python) # 교집합
print(java.intersection(python))
print(java | python) # 합집합
print(java.union(python))
print(java - python) #차집합
print(java.difference(python))
python.add("김태호")
print(python)
java.remove("김태호")
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu,type(menu))
menu = list(menu)
print(menu,type(menu))
menu = tuple(menu)
print(menu,type(menu))
menu = set(menu)
print(menu,type(menu))
