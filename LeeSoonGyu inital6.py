# 빅데이터 A조(2차) 이순규
# 1.
# f = open('foo.txt', '_1번빈칸_', encoding = 'utf-8)
# f.write('Life is too short, you need python')
# f.close()
# _2번빈칸_ open('foo.txt', _3번빈칸_) as f :
# line = f.readline()
# print(line)
# 1,3번빈칸 = mode = 'w','r' 어떤적용을 시킬지, 2번빈칸 with open적용으로
import os
os.getcwd()
f = open('foo.txt', mode='w', encoding='utf-8')
f.write('Life is too short, you need python')
f.close()
try:
    with open('foo.txt', mode='r', encoding='utf-8')as f:
        line = f.readline()
        print(line)
except Exception as e:
    print('Error 발생 : ', e)


# 2.
# 기존잔액 : 10,000원
# 입금액 : 5,000원
# 출금액 : 3,000원
# 한달동안의 이자율 : 2%
# 처리조건
# 1). 클래스 객체로 작성
# 2). 클래스 내 멤버 변수 설정
# 3). 클래스 내 생성자 작성
# 4). 클래스 내 기존잔액, 입금액, 출금액 이용 신규잔액 계산 메스드 작성
# 5). 객체 메서드 내 실행 결과 변수가 다른 객체 메서드에서 사용될 수 있도록 작성
# 6). 한달 이자액 계산 객체 메서드 이자 = 잔액 * 이자율 (12,000*240)
# 7). 기존잔액, 입금액, 출금액, 이자율 입력 객체 생성
# 8). 생성 객체에서 객체메서드 사용 현재잔액 보여주기
# 9). 한달 이자액 보여주기

class bank:
    getbalance = 0  # 기존잔액
    deposit = 0  # 입금액
    withdraw = 0  # 출금액
    money = 0  # 이자율
    def __init__(self, getbalance, deposit, withdraw, money):
        self.getbalance = getbalance
        self.deposit = deposit
        self.withdraw = withdraw
        self.money = money
    def money1(self):
        self.result = self.getbalance + self.deposit - self.withdraw
        money2 = self.result
        return money2
    def money3(self):
        self.money4 = self.result * (self.money / 100)
        money5 = self.money4
        return money5
    def display(self):
        print('계좌 잔액 : %d원 입니다.' % bank.money1(self))
        print('한달 이자액 : %d원 입니다.' % bank.money3(self))
leesoongyu = bank(10000, 5000, 3000, 2)
leesoongyu.display()