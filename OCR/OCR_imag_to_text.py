# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:48:42 2020

@author: Ayush
"""

import pytesseract	 
from PIL import Image	 

img = Image.open('pesticides/Bayer Aliette.jpg')	 
print(img)						 

pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

result = pytesseract.image_to_string(img,lang='eng') 
print(result) 
