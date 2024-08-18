# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:28:40 2024

@author: zehra
"""

import random

# Oyunun açıklamasını yaptık:
def tas_kagit_makas_zehranurcelik():
    print("Oyun Açıklaması:")
    print("Bu oyun Python, Java ve PHP seçenekleriyle taş-kağıt-makas oyunudur.")
    print("Python: Taş")
    print("Java: Kağıt")
    print("PHP: Makas")
    print("İlk iki raundu kazanan oyunu kazanır. Kullanıcı veya bilsisayar geçersiz bir seçim yaparsa, tekrar seçmesi istenir.")
    print("Her raund sonunda skorlar gösterilir.\n")

def compare_choices(kullanici_secimi, bilsisayar_secimi):
    global kullanici_skor, bilsisayar_skor
    if kullanici_secimi == bilsisayar_secimi:
        return "Berabere!"
    elif (kullanici_secimi == "Python" and bilsisayar_secimi == "PHP") or \
         (kullanici_secimi == "Java" and bilsisayar_secimi == "Python") or \
         (kullanici_secimi == "PHP" and bilsisayar_secimi == "Java"):
        kullanici_skor += 1
        bilsisayar_skor -= 1
        return "Siz Kazandınız!"
    else:
        kullanici_skor -= 1
        bilsisayar_skor += 1
        return "Bilsisayar kazandı!"

def oyun_oyna():
    global kullanici_skor, bilsisayar_skor
    kullanici_skor = 0
    bilsisayar_skor = 0

    while kullanici_skor < 2 and bilsisayar_skor < 2:
        print(f"\nSkor: Kullanıcı {kullanici_skor} - Bilsisayar {bilsisayar_skor}")
        kullanici_secimi = input("Seçiminizi yapın (Python, Java, PHP): ")
        
        # Kullanıcı geçerli bir seçim yapana kadar sorduk:
        while kullanici_secimi not in ["Python", "Java", "PHP"]:
            kullanici_secimi = input("Geçersiz seçim! Lütfen size belirtilen karakterlerden birini seçin. (Python, Java, PHP): ")
        
        bilsisayar_secimi = random.choice(["Python", "Java", "PHP"])
        print(f"Bilsisayarın seçimi: {bilsisayar_secimi}")
        
        result = compare_choices(kullanici_secimi, bilsisayar_secimi)
        print(result)
    
    print("\nOyun Sonucu:")
    if kullanici_skor == 2:
        print("Tebrikler, oyunu siz kazandınız:)")
    elif bilsisayar_skor == 2:
        print("Üzgünüm, oyunu kaybettiniz:(")

# Tekrar oynama seçeneği ekledik:  
def tekrar_oyna():
    while True:
        tekrar = input("Başka bir oyun oynamak ister misiniz? (Evet/Hayır): ").strip().lower()
        if tekrar == "evet":
            return True
        elif tekrar == "hayır":
            return False
        else:
            print("Geçersiz yanıt, lütfen 'Evet' veya 'Hayır' yazınız.")

# Oyunu başlatıyoruz:
tas_kagit_makas_zehranurcelik()  

while True:
    oyun_oyna()
    if not tekrar_oyna():
        print("Teşekkürler, oyun bitti!")
        break