"""
Install pip install pywhatkit
"""
import pywhatkit as kit
import os
import cv2

os.environ['DISPLAY'] = ':0'

Handwritten = input("Enter your text to convert into handwriting:")
kit.text_to_handwriting(Handwritten, save_to="pythonhandwriting.png")
img = cv2.imread("pythonhandwriting.png")
cv2.imshow("Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
