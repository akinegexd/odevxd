gerceksayi=int(input('atm için 1, hesap makinesi için 2, ortalama hesaplama için 3, sayı tahmin için 4, yazdığınız sayının tek mi çift mi olduğunu öğrenmek için 5 yazınız'))
if gerceksayi==1:
    kredisifre = 1234
    bakiye=500
    sayac=3
    login=False

    while True:
        if login == False:
            sifre=int(input('şifre giriniz:'))
        if sifre == kredisifre:
            login = True
            print('1-para çek,2-para yatır,3-bakiye görme')
            secim=int(input('hangisini istiyorsunuz?'))
            if secim ==1:
                miktar = int(input('kaç tl çekeceksiniz?'))
                if miktar > bakiye:
                    print('yeterli bakiyeniz yoktur:')
                    continue
                bakiye -= miktar
            elif secim == 2:
                miktar=int(input('kaç para yatırmak istiyorsunuz?'))
                bakiye += miktar
            elif secim == 3:
                print('bakiyeniz {} TL'.format(bakiye))
                break
            else:
                print('lütfen geçerli bir rakam seçiniz')
elif gerceksayi==2:
    numara1=int(input('1.sayıyı giriniz:'))
    numara2=int(input('2.sayıyı giriniz'))
    hesap=int(input('toplama için 1 çıkarma için 2 çarpma için 3 bölme için 4 yazınız'))


    if numara1>numara2:
        num1=numara1
        num2=numara2
    else:
        num1=numara2
        num2=numara1


    if hesap=='1':
        sayi=num1+num2
    elif hesap=='2':
        sayi=num1-num2
    elif hesap=='3':
        sayi=num1*num2
    elif hesap=='4':
        sayi=num1/num2
    else:
        print('lütfen geçerli bir sayı girin')



    print(sayi)
elif gerceksayi==3:
    print('geçerli bir not girmezseniz ortalamanız 0 olarak gözükür')
    liste=[]
    sinav=int(input('kaç sınav oldunuz:'))
    for i in range (sinav):
        i=float(input('notunuzu giriniz:'))
        if 100 >= i >= 0:
         liste.append(i)
        else:
            print('geçerli bir değer giriniz')
            break
    toplam=sum(liste)
    ortalama=toplam/sinav
    print(ortalama)
elif gerceksayi==4:
    import random
    sayi=random.randint(1,15)
    hak=5
    while hak>0:
        hak-=1
        tahmin=int(input('1 ile 15 arasında sayı tuttum.tahmininiz:'))
        if tahmin==sayi:
            print('doğru')
            break
        elif hak==0:
            print('doğru sayi')
            print(sayi)
        elif tahmin>sayi:
            print('aşağı in')
            continue
        elif sayi>tahmin:
            print('yukarı çık')
            continue
elif gerceksayi==5:
    sayi==int(input('bir sayı giriniz:'))
    if sayi % 2==0:
        print('çift sayıdır')
    elif sayi % 2==1:
        print('tek sayıdır')
else:
    print('lütfen geçerli bir sayı giriniz')






