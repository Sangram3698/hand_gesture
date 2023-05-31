import qrcode

data='The information may not be valid'

img=qrcode.make(data)
img.save('qr.png')