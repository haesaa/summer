# workGame.py

def zerg() :
    print('zerg() 종족')
    print('Drone, Zergling, Hydralisk, Brood Lord\n')
    
def maple(season,cnt) :
    print('메이플 시즌은', season)
    print('메이플 총 참여인원 수', cnt)
    print('카이저, 제논, 카데나, 아크, 일리움\n')

# 376~377p return 참고
def add(a, b) :
    # 출력금지 계산만 처리
    total = a + b
    return total

# 같은문서에서 정의 = 구현 = implement = 기술 = 구현 후 같은 문서에서 호출
data = add(11,22)
print('총금액 =', data)
print('총금액 =', add(11,22))
print(data)

# print('총금액 =', total) #def안의 total변수기때문에 로컬변수임



def myTsetpass(x, y) : #계산 후 if 제어문으로 축합격/재시험
    message = '합격여부메세지'
    avg = 0
    total = x + y
    avg = total//2
    if avg >= 70 :
        message = '축합격'
    else:    
        message = '재시험'
    return message #숫자, 문자 다 됌

x = 90
y = 80
data = myTsetpass(x,y)
print(f'당신의 시험결과는{data}입니다.')



