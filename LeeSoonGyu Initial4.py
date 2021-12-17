# 이순규
# 1.
result = [90, 25, 67, 45, 80]
print(result)
print(type(result))
result2 = len(result)
for i in range(result2):
    if result[i] >= 60:
        grade = '합격입니다'
        print(grade, end=' ')
    else:
        if i < 60:
            grade = '불합격'
            print(grade, end=' ')


# 2. 과락부분 수정해보자!!

a = int(input('국어 점수를 입력하세요 : '))
b = int(input('수학 점수를 입력하세요 : '))
c = int(input('영어 점수를 입력하세요 : '))
total = a+b+c
print('총 점수는',total,'점 입니다.')
if a < 40 and b < 40 and c < 40:
    print('과락입니다.')
else:
    if total >= 180 :
        print('합격입니다.')
    else :
        print('불합격입니다.')

# 3. 무한루프사용해보자!!

for i in range(0,5):
    money = int(input('돈을 넣어주세요 :'))
    if money == 5000 :
        print('식권 발급')
    elif money >= 5000 :
        print('잔돈은 %d 입니다.'%(money - 5000))
    else :
        print('금액이 부족합니다.')

print('식권 소진')

def conuter(n):
    if n == 0:
        return 0
    else:
        conuter(n-1)

while True :
    n = int(input('식권 입력 : '))
    if n < 1 == 0 : # 종료
        print('식권이 부족합니다.')
        break
    else:
        print(n)
