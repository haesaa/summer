# 06mydictlast.py
mydict = {'code':2300, 'title':'kim'} 
mydict['grade'] = 'B'
mydict['jeju'] = '한라산'
#지원안되는 함수, append(), insert(), add() !!!아님!!!
k,v = 0,0
for k,v in mydict.items() : 
    #key, value 데이터 같이  출력됌
    print(f'{k} : {v}') 
print('-' * 25)
for i,k in enumerate(mydict) :
    print(i+1, ' ', k, mydict[k])
  # print(index숫자나열, ' ', keys, value)
     #enumerate - 값을 꼭 2개를 받아야함 순서를 매겨줌 열거. 0부터시작함          


# i j k l m n -> 쓰면 정수형으로 인식함

