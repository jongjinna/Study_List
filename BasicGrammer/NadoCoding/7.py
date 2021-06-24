# 나도코딩 파이썬 7-1

# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {}원이며, 잔액은 {}원 입니다.".format(commission, balance))

# 기본값
def profile(name, age, main_lang):
    print("이름 : {}\t나이 : {}\t주 사용 언어 : {}" \
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

def profile2(name, age=17, main_lang="파이썬"):
    print("이름 : {}\t나이 : {}\t주 사용 언어 : {}" \
        .format(name, age, main_lang))

profile2("유재석")
profile2("김태호")

# 키워드값
def profile3(name, age, main_lang):
    print("이름 : {}\t나이 : {}\t주 사용 언어 : {}" \
        .format(name, age, main_lang))

profile3(name = "유재석", main_lang = "파이썬", age = 20)
profile3(main_lang= "파이썬", age = 25, name = "김태호")

# 가변인자
def profile4(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile4("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile4("김태호", 25, "Kotlin", "Swift","","","")

def profile5(name, age, *language):
    print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile5("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile5("김태호", 25, "Kotlin", "Swift")

# 지역변수와 전역변수
gun = 10
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun

print("전체 총 : {}".format(gun))
checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {}".format(gun))