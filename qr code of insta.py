import qrcode as qr
img=qr.make("https://www.instagram.com/?hl=en")
img.save("instagram link.png")