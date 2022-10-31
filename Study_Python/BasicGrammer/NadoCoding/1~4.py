# 나도코딩 파이썬 1-1 ~ 4-6

# 숫자형 자료
print(5, -10, 3.14, 1000, 5+3, 2*8, 3*(3+1))


# 문자형 자료
print('풍선', "나비", "ㅋㅋㅋ", "ㅋ"*3)


# boolean 자료형
print(5 > 10, 5 < 10, True, False, not True, not False, not (5 > 10))


# 변수
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3
print("우리집" + animal + "의 이름은 " + name + "예요.")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요.") # ,는 뒤에 무조건 띄어쓰기
print(name + "는 어른일까요? " + str(is_adult)) # +로 할 경우 띄어쓰기 X

# 연산자
print(1+1, 3-2, 5*2, 6/3, 2**3, 5%3, 5//3, 10 > 3, 4 >= 7, 3 == 3, 1 != 3)
print((3 > 0) and (3 < 5), (3 > 0) & (3 < 5), (3 > 0) or (3 > 5), (3>0) | (3>5))

# 수식
print(2 + 3 * 4, (2 + 3) * 4)
num = 2 + 3 * 4
print(num)
num = num + 2
print(num)
num += 2
num *= 2
num /= 2
num -= 2
num %= 2
print(num)

# 숫자처리함수
print(abs(5))
print(pow(4, 2)) # 4^2
print(max(5, 12))
print(min(5, 12))
print(round(3.14))

from math import *
print(floor(4.99)) # 내림
print(ceil(4.99)) # 올림
print(sqrt(16)) # 제곱근

# 랜덤함수
from random import *

print(random())
print(random() * 10)
print(int(random() * 10))
print(randrange(1, 46)) # 1이상 46미만
print(randint(1, 45)) # 1이상 45이하

# 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 ="파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 :" + jumin[7])
print("연 :" + jumin[0:2])
print("월 :" + jumin[2:4])
print("일 :" + jumin[4:6])

print("생년월일 :" + jumin[:6])
print("뒤 7자리 :" + jumin[7:])
print("뒤 7자리 (뒤에부터) :" + jumin[-7:])

# 문자열처리함수
python = "Python is Amazing."
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # find는 없으면 -1출력, index는 없으면 오류
print(python.count("n"))

# 문자열포맷
print("a" + "b")
print("a", "b")

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살 입니다." .format(20))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에 \가 있는 경우
print("Red Apple\rPine") # \r : 커서를 맨 앞으로 이동
print("Redd\bApple") # \b : 백스페이스 (한 글자 삭제)
print("Red\tApple") # \t : 탭
