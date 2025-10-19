import random
list=[*range(1,101)]
sayi =random.choice(list)
tahmin=int(input("1 ile 100 arasında bir sayı tahmininde bulununuz:"))

while not (sayi==tahmin) :
    if tahmin > sayi:
        print("Tahmininiz fazla büyük...")
    elif tahmin < sayi:
        print("Tahmininiz fazla küçük")
    tahmin=int(input("1 ile 100 arasında bir sayı tahmininde bulununuz:"))
else :
   print("Tebrikle doğru tahmin!")

#Kullanıcı hesap girş test-1 örnek-1
def Hesap_giris():
   kullanici_adi=input("Bir kullanıcı adı oluşturunuz:")
   sifre=input("Bir şifre oluşturunuz:")
   while not (len(kullanici_adi)>=5 and len(sifre)>=5):
       print("Malesef geçersiz Kullanıcı adı ve şifre...")
       kullanici_adi = input("Bir kullanıcı adı oluşturunuz:")
       sifre = input("Bir şifre oluşturunuz:")

   else :
      print("Tebrikler doğru kullanıcı adı ve şifre...")

   kullanici_bilgileri ={
       "Kullanıcı Adı":kullanici_adi,
       "Şifre":sifre
   }
   print(kullanici_bilgileri)