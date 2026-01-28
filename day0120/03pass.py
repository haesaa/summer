# 03pass.py

def mypass(x, y) : #계산 후 if 제어문으로 축합격/재시험
    message = '합격여부메세지'
    avg = 0
    total = x + y
    avg = total//2
    if avg >= 70 :
        message = '축합격'
    else:    
        message = '재시험'
    return message #숫자, 문자 다 됌

data = mypass(80,80)
print('결과 내용을 아래에서 확인하세요')
print(f'{data}입니다.')
print()


