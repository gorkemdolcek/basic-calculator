#Basic Calculator

sayı1 = int(input("1. Sayıyı giriniz: "))
sayı2 = int(input("2. Sayıyı giriniz: "))
islem = input("Toplama için (+) Çıkarma için (-) Çarpma için (*) Bölme için (/)")
if islem == "+":
    sonuc = sayı1 + sayı2
    print("Toplam: ", sonuc)
elif islem == "-":
    sonuc = sayı1 - sayı2
    print("Fark: ", sonuc)
elif islem == "*":
    sonuc = sayı1 * sayı2
    print("Çarpım:", sonuc)
elif islem == "/":
    sonuc = sayı1 / sayı2
    print("Bölüm: ", sonuc)
else:
    print("Hatalı giriş yaptınız, Lütfen tekrar deneyin.")