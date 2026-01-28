# testfaker.py

import qrcode
import cv2
from faker import Faker

my = Faker()
for k in range(10) :
    print(my.name())

print()
for k in range(10) :
    print(my.ipv4_private())

data = Faker('ko_KR')
for k in range(20) :
    print(data.name())
print()

# 에러 ModuleNotFoundError: No module named 'qrcode'
# C:\dongaAI\day0123> pip install qrcode
# Installing collected packages: qrcode
# C:\dongaAI\day0123> pip intstall faker

