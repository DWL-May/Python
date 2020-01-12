import re
string = "The quick brown fox jumps over the lazy dog"
string_list = string.split()
pattern = re.compile(r"The", re.I) #원시 문자열임을 표기하는 r / re.compile함수는 텍스트 기반의 패턴을 정규 표현식으로 컴파일
#re.I는 대소문자 구분을 없애준다.
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1

print("Output #38: {0:d}".format(count))