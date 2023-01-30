from random import randint
import pyqrcode
from pyqrcode import QRCode


# building a Qr generator function that reads the URL from a file and creates a Qr png and save it in the path user had chosen.  
def Qr_generator():
    file = open('Qr_URLS.txt', 'r')
    y = str(input('\nEnter the Desired Path for the QR PNGS to be saved in: '))
    pngPath = y + '\\'
    # reading each line from the file and generating qr png for each URL
    for line in file:
        url = pyqrcode.create(line)
        x = randint(0, 10 ** 10)
        m = '.png'
        n = pngPath + str(x) + m
        url.png(n, scale=6)

    # closing the file that had been opened
    file.close()
