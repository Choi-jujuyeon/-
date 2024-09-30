# 이진수에서는 정확한 실수 정보를 표현하는데 한계가 있다.

a = 0.3 + 0.6
print(a)

if a== 0.9:
    print(True)
else:
    print(False)
    
# 정확한 값을 측정하기 위해서 round()를 사용하자 !
a = 0.3 + 0.6
print(round(a,4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)