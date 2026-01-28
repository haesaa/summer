# 02Exception.py
num = 0 #변수 = variable = local 지역변수
try :
    num = int(input('숫자를 기술>>> '))
except Exception as ex :
    print('정지', ex)
else:
    print('결제금액 =', num*5, '원')
finally :
    print('가나디')  
    print('멍멍')  
    print('와오앙')  

