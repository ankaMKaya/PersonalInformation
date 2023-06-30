with open("deneme.txt", "r+") as dosya:
   print(dosya.read())
   print("http://", "www.", "google.", "com.", "tr", sep="", file=dosya)
   print("Merhaba dunya ben python", file=dosya)
   print("Temel Dosya İslemleri - Yazbel", file=dosya)

dosya.close()

import os
os.getcwd()

b = open("kisisel_bilgilerim.txt", "w+")

print("Muhammed Kaya", file=b, flush=True) # True oldugu icin buffer'da tutmayacak direkt ya
print("Ankara", file=b)
print("Linux", file=b)

b.close()

basligimiz="Programlama dili olan pitonumuz :)) Python"
print(basligimiz, "\n", "-"*len(basligimiz), sep="")

import os 
os.mkdir("newpaper2")
os.system("cd newpaper2")
os.mkdir("ikinci_klasör")

isim = "muhammed"
soyisim = "kaya"
işsis = "linux"
şehir = "ankara"
isim2 = input("Göbek adiniz nedir? ")

print("isim     : ", isim,  "\n",
"soyisim     : ", soyisim,  "\n",
"işletim sistemim     : ", işsis,  "\n",
"şehrimiz     : ", şehir,  "\n",
"göbek adi  : ", isim2, "\n",
sep=""
)

dilekçe = """
                                                    tarih: {}


T.C.
{} ÜNİVERSİTESİ
{} Fakültesi Dekanliğina


Fakülteniz {} Bölümü {} numarali öğrencisiyim. Ekte sunduğum belgede
belirtilen mazeretim gereğince {} Eğitim-Öğretim Yili  {}.
yariyilinda öğrenime ara izni (kayit dondurma) istiyorum.

    Bilgilerinizi ve gereğini arz ederim.

        İmza

Ad              : {}
Soyad           : {}
T.C. Kimlik No. : {}
Adres           : {}
Tel.            : {}
Ekler           : {}
"""


tarih           = input("tarih: ")
üniversite      = input("üniversite adi: ")
fakülte         = input("fakülte adi: ")
bölüm           = input("bölüm adi: ")
öğrenci_no      = input("öğrenci no. :")
öğretim_yili    = input("öğretim yili: ")
yariyil         = input("yariyil: ")
ad              = input("öğrencinin adi: ")
soyad           = input("öğrencinin soyadi: ")
tc_kimlik_no    = input("TC Kimlik no. :")
adres           = input("adres: ")
tel             = input("telefon: ")
ekler           = input("ekler: ")

print(dilekçe.format(tarih, üniversite, fakülte, bölüm,
                     öğrenci_no, öğretim_yili, yariyil,
                     ad, soyad, tc_kimlik_no,
                     adres, tel, ekler))

d = open("kişisel_bilgilerim2.txt", "w")

print("Batuhan TArsalan", file=d, flush=False)
print("Ankara", file=d)
print("Ubuntu", file=d)
print("Merhaba Dünya!", file=d)

d.close()