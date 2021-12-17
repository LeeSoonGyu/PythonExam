# 이순규
# 11번
# 리스트의 문자열을 인덱스로 접근하여 문자열 크기를 비교 / 출석 여부 확인 프로그램 구현
# 학생들의 등교시간 : 9시, 9시20분, 8시50분, 8시55분, 9시12분
# 지각시간 기준 : 9시10분 또는 그 이후
# enumerate 함수사용

from re import sub

lee = ['9시','9시 20분', '8시 50분', '8시 55분', '9시 12분']
soon = [sub('[가-힣]','',text) for text in lee]
gyu = [''.join(text.split()) for text in soon]
print(gyu)
for i,c in enumerate(gyu) :
    i = []
    if int(c[0:3]) >= 910 :
        print('지각')

    else:
        print('정상')

# 12번
# 주어진 자연수가 홀수인지 짝수인지 판별함수(is_odd)작성
# 람다와 조건부 표현식 사용 is_odd함수 작성
# is_odd함수 이용 숫자 입력하여 홀,짝 여부 확인

# 조건부 표현식
num = int(input('숫자를 입력하세요 : '))
is_odd = '짝수 입니다.' if num % 2 == 0 else '홀수 입니다.'
print(num, "는", is_odd)
# 람다와 조건부 표현식
# 12-1
num= int(input('숫자를 입력하세요 : '))
def is_odd(num):
    if num % 2 == 0 :
        return '짝수입니다.'
    else:
        return '홀수입니다.'
print(is_odd(num))
# 12-2
is_odd = lambda num: '짝수 입니다.' if num % 2 == 0 else '홀수 입니다.'
print(is_odd(num))

# 13번
# 메뉴 : 짬뽕(6000), 간짜장(5000), 짜장면(4000)
# 메뉴선택 입력창 나와서 메뉴 입력
# 메뉴 선택시 가격이 출력
menu = input('메뉴를 선택하세요 : ')
price = input('가격을 입력하세요 : ')
class total_calc :
    menu = price = 0
    def __init__(self, menu, price):
        self.menu = menu
        self.price = price
    def m_calc(self):
        a = self.menu + self.price
        return a

lee = total_calc(menu, price)
soon = lee.m_calc()
print('선택 메뉴 가격 : ', soon)