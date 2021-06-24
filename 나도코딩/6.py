# 나도코딩 파이썬 6-1 ~ 6-6

# if
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요.")

# 반복문 for
for waiting_no in range(1,6):
    print("대기번호 : {}".format(waiting_no))
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{}, 커피가 준비되었습니다.".format(customer))

# 반복문 while
customer = "토르"
index = 5
while index >= 1:
    print("{}, 커피가 준비되었습니다. {}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{}, 커피가 준비되었습니다. {}번 남았어요.".format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print("{}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요.")

# continue 와 break
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지, {}은 교무실로 따라와".format(student))
        break
    print("{}, 책을 읽어봐.".format(student))

# 한줄 for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)
students = ["Iron man", "Thor", "groot"]
students = [len(i) for i in students]
print(students)
students = ["Iron man", "Thor", "groot"]
students = [i.upper() for i in students]
print(students)