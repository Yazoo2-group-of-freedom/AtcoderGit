import time
import random

"""
print(1)
time.sleep(5)
print(2)
"""

"""
for test in range(1000):
    a = random.randint(1,10)
    print(a)
    time.sleep(0.01)
"""
#許される入力形式->"[int] [int]"
init = input()
#print(type(init) is str)   #inputの入力はstr型
sp = init.find(" ")
tow_val = [int((init[:sp])),int((init[sp+1:]))]
#print(tow_val)

x = int((sum(tow_val))/2)#sumはリストの場合リストの要素すべてを足し合わせる
y = int((tow_val[0] - tow_val[1])/2)

print(str(x) + " " +str(y))


