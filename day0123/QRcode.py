# QRcode.py

import qrcode
import cv2
url = 'http://www.google.com'
qr_img = qrcode.make(url)
qr_img.save(stream='./images/gg_QR.png')
print('QRtesting~~~')

image = cv2.imread('./images/gg_QR.png')
cv2.imshow('title', image)
cv2.waitKey(0) #키 입력까지 대기
# cv2.destroyAllWindows() #메모리상에 남아있는 cv2관련창 close()

print('QRtesting~~~ 이미지 오픈')

# 에러 ModuleNotFoundError: No module named 'qrcode'
# C:\dongaAI\day0123> pip install qrcode
# Installing collected packages: qrcode
# C:\dongaAI\day0123> pip install opencv- python

