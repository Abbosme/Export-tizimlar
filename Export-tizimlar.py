# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PmhcSpVwiz8VzWPmdfHZa2JjMOai6scQ
"""

def tashxis(belgi):
    if belgi == "istima":
     return "Parasetamol iching "
    elif belgi == "bosh og'riq" :
     return "Trimol iching"
    elif belgi == "Tish og'riq":
     return "Qupen iching "
    elif belgi == "Oshqozon og'riq":
     return "NO-Shpa iching "
    elif belgi == "Tomoq og'riq":
     return "Romidon iching"
    elif belgi == "Spazm og'riq":
     return "Dufalak iching "
    elif belgi == "Jigar og'riq":
     return "Apkosul iching "
    elif belgi == "Yurak og'riq":
     return "Validol iching "
    elif belgi == "Tizza og'riq":
     return "Voltaren surting "
    elif belgi == "Burun og'riq":
     return "Naftizin quying "
    elif belgi == "Ko'z og'riq":
     return "Kamroq telefon o'ynang "
    else :
     return "Shifokorga murojaat qiling "
belgi=input("Kasallik belgisini kiriting ")
natija=tashxis(belgi)
print(natija)

from google.colab.patches import cv2_imshow
import cv2
def kino(a):
  if a=="Komediya":
    rasm=cv2.imread("Bin.jfif")
    cv2_imshow(rasm)
    return "Mister bin"
  elif a=="Poyga":
    rasm1=cv2.imread("tezlik.jfif")
    cv2_imshow(rasm1)
    return  "Tezlik zavqi"
  elif a=="Ujas":
    rasm2=cv2.imread("U.jfif")
    cv2_imshow(rasm2)
    return  "Masxaraboz U"
  elif a=="Multfilm":
    rasm3=cv2.imread("sonic.jfif")
    cv2_imshow(rasm3)
    return  "Sonik"
  elif a=="Serial":
    rasm4=cv2.imread("Super.jfif")
    cv2_imshow(rasm4)
    return  "Super kuchlar"
  elif a=="Anime":
    rasm5=cv2.imread("anime.jfif")
    cv2_imshow(rasm5)
    return  "Solo leveling"
  elif a=="Hind":
    rasm6=cv2.imread("hind.jfif")
    cv2_imshow(rasm6)
    return  "Urush va jang"
  elif a=="Zombi":
    rasm7=cv2.imread("zombi.jfif")
    cv2_imshow(rasm7)
    return  "Zombilar"
  elif a=="Godzilla":
    rasm8=cv2.imread("godzilla.jfif")
    cv2_imshow(rasm8)
    return  "Godzilla: Maxluqlar hukmdori"
  elif a=="Korea seriali":
    rasm9=cv2.imread("Voris.jfif")
    cv2_imshow(rasm9)
    return  "Vorislar"
a=input("Kino janrini kiriting: ")
natija=kino(a)
print(natija)