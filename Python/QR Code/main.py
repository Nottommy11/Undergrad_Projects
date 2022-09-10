# """
# Need "pip install pyqrcode"
import pyqrcode
# import sys

# Input Website Link Here
url = pyqrcode.create("https://www.channingogden.com/")
# Name of QR Code File, Adjust Size
url.svg("ChanningQR.svg", scale = 8)

# url.svg("uca.svg", scale=4)
# number = pyqrcode.create(123456789012345)
# number.png("big-number.png")
# """

"""
import pyqrcode
# from pyqrcode import QRCode

# String which represents the QR Code
qr = "https://www.channingogden.com/"

# Generate the QR Code
url = pyqrcode.create(qr)

url.svg("qr.svg", scale = 8)
"""