# 나도코딩 파이썬 8-1

# 표준입출력
import sys
print("Python", "Java", "JavaScript", sep=",", end = "?")
print("무엇이 더 재밌을까요?")

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 {}입니다.".format(answer))

# 다양한 출력 포멧
print("{: >10}".format(500))
print("{: >+10}".format(500))
print("{: >+10}".format(-500))
print("{:_<+10}".format(500))
print("{:,}".format(100000000000))
print("{:+,}".format(100000000000))
print("{:^<+30,}".format(100000000000))
print("{:f}".format(5/3))
print("{:.2f}".format(5/3))

# 파일입출력
