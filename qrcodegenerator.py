#program to create QRCode generator
import qrcode
img = qrcode.make("this is a test qrcode")
img.save("qrtest.png")
