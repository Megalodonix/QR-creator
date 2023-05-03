import qrcode
qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=4)

data = input("Text to QR code: ")

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="#333333")
img.save("qrcode.png")