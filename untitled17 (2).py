# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pDvWUqtmxrdsaHXQT-Vmaq_mWtMhQKsh
"""

def tashxis(belgi):
  if belgi == "istima":
    return "Parasetamol iching"
  elif belgi == "bosh og'riq":
    return "Trimol iching"
  elif belgi== "Tish og'riq":
    return "Quepen iching"
  else:
    return "Shifokorga murojaat qiling"
belgi=input("Kasallik belgisini kiriting ")
natija=tashxis(belgi)
print(natija)

from google.colab.patches import cv2_imshow
import cv2
def kampyuter(nomi):
  if nomi == "acer":
    rasm=cv2.imread("images.jpg")
    cv2_imshow(rasm)
    return "core 5i 8 pakaleniya 11 avlod"
  elif nomi == "Lenovo":
    rasm1=cv2.imread("image.webp")
    cv2_imshow(rasm1)
    return "inter celeron 4020"
  elif nomi == "MacBookAir":
    rasm2=cv2.imread("87.png")
    cv2_imshow(rasm2)
    return "13 pakaleniya core 5i DDR3"
  elif nomi == "hp":
    rasm3=cv2.imread("89.png")
    cv2_imshow(rasm3)
    return "rayzin 5 pakaleniya"
  elif nomi == "hp":
    rasm4=cv2.imread("images(1).jpg")
    cv2_imshow(rasm4)
    return "rayzin 6 pakaleniya"
  elif nomi == "Zifler":
    rasm5=cv2.imread("zd9o37ig6bxav9glb6djttua5m2j5zb4")
    cv2_imshow(rasm5)
    return "rayzin 7 pakaleniya"
  elif nomi == "acer":
    rasm6=cv2.imread("f6a130d9-e553-4495-b7c5-1a04dd8c26c8")
    cv2_imshow(rasm6)
    return "core 5i 8 pakaleniya"
  else:
    return "boshqa kampuyuter kormoqchi bolsangiz Abdulvosidga murojat qiling"
nomi=input("kampuyuter nomini kiriting ")
natija=kampyuter(nomi)
print(natija)