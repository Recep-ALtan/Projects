while True :
  def islem(a,b,c) :
      if c == "+":
          return a+b
      elif c == "-":
          return a-b
      elif c == "*":
          return a*b
      elif c == "/":
          if b == 0:
              return "Tanımsız!"
          else:
              return a/b
      else:
          return "Mevcut olan işlemleri tercih ediniz."

  hesap =islem(a =float(input("Bir sayı giriniz:")),
               b =float(input("İkinci bir sayı giriniz:")),
               c =input("Yapmak istediğiniz işlemi seçiniz(+,-,*,/):"))
  print(hesap)