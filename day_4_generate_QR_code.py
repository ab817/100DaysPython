#pip install pypng
#pip install pyqrcode

import pyqrcode
import png

link = "https://pypi.org/project/geopy/"
qr_code = pyqrcode.create(link)
qr_code.png("qr_code.png", scale=5)

