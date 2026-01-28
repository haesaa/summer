# 05testfor.py

# 해결1] 중첩없이 for반복문 or while 반복문
# 1~300 사이 출력
a,b,c = 0,0,0
# 해결2] 한 줄에 10개씩 * 30줄 출력
for a in range(1,301,1) :
    print(a, end = '\t')
    if a % 10 == 0 : 
    #ㄴ10단위로 나눴을때 나머지가 0이되게 해
        print('\n')

while True :
    b += 1
    if b % 10 == 0 :
        print(b, end = '\t')
    if b == 300 :
        print(b, end = '\t')
        break
