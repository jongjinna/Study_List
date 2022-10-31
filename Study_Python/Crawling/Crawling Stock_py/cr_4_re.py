import re #정규식 regular

p = re.compile("ca.e")
# . (ca.e): 하나의 문자를 의미 cafe, care | caffe(x)
# ^ (^de) : 문자열의 시작 desk | fade(x)
# $ (se$) : 문자열의 끝 case, base | face(x)


def print_match(m):     
    if m:
        print("m.group() :", m.group())
        print("m.string :", m.string)
        print("m.start() :", m.start())
        print("m.end() :", m.end())
        print("m.span() :", m.span())
    else:
        print("매칭되지 않음")

# m = p.search("good careless") 
# match : 주어진 문자열의 처음부터 일치하는지 확인 careless(o)
# search : 주어진 문자열 중에 일치하는게 있는지 확인 good care(o)
# findall : 일치하는 모든 것을 리스트 형태로 반환
lst = p.findall("good careless cafe in cave")
#print_match(lst)
print(lst)