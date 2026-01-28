# 06star.py

# 해결1] for문 안에 for 중첩사용
# 해결2] while 하나로도 가능
# 해결3] while 반복문안에 while 중첩 가능
'''
 ★
 ★★
 ★★★
 ★★★★
 ★★★★★
'''
a = 0
while a < 5 :
    a += 1
    print('★' * a)
print()
# i,j =0,0
# for i in range(1,6,1) :
#     for j in range(i):
#         i += 1
#         print('★', end = '  ')
#     print('\n')

print()
print()
for k in range(1,6,1) : #1부터 시작함
    for j in range(k) :
        print('☆', end = ' ')
    print()
print()
# 5~1개
# a = 0
# b = 5
# while a < 5 :
#     a += 1
#     print('🥨' * b)
#     b -= 1
#     if b == 0 :
#         break

# 피라미드만들기
i,c,m = 0,0,0
for i in range(0,11,1) :
    for c in range((10-i)//2) :
        print(" ", end = " ")
    for m in range(i) :
        print('ㅁ', end = ' ')
    print('\n')
    # print(end = '  ')