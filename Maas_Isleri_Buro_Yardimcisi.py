ogrenci_say=kadin_ogrenci_say=erkek_ogrenci_say=0
basarisiz_say=basarili_say=ortalama_say=ustun_basarili_say=0
kadin_agirlikli_not_ort_toplam=erkek_agirlikli_not_ort_toplam=0
toplam_agirlikli_not_ort=0
toplam_kredi_say=0
ders_uc_kredi_on=0
basari_yuzdesi_yetmis_bes=0
tum_dersleri_basarili_ogrenci_say=0
uc_yuzden_fazla_burs_say=0
okul_birinci_ad_soyad=""
okul_birinci_ders_say=0
okul_birinci_kredi_say=0
okul_birinci_agirlikli_not_ort=0
okul_birinci_burs=0
max_ad_soyad=""
max_ders_say=0
max_kredi_say=0
max_agirlikli_not_ort=0
max_alinan_burs=0
ogrencilere_Odenen_Toplam_Burs=0
evde_kalan_say=yurtta_kalan_say=aileyle_kalan_say=0
basarili_ev=basarili_yurt=basarili_aile=0
min_ikamet=""

ogrenci_No=int(input("Lutfen Oğrenci Numaranizi Giriniz:"))
while ogrenci_No<1:
    ogrenci_No = int(input("Hatali giris yaptiniz.. Lutfen numaranizi dogru giriniz:"))

while ogrenci_No>=1:
    alinan_kredi_say = 0
    alinan_Ders_Say = 0
    basarili_ders_say=0
    basarili_kredi_say=0
    agirlikli_not_say=0
    basari_Durumu=""
    aylik_Burs=0
    ogrenci_say+=1
    ad_Soyad = input("Adinizi ve Soyadinizi Giriniz:")
    cinsiyet = input("Cinsiyetinizi Giriniz(Kadin:K/k Erkek:E/e):")
    if cinsiyet not in "k,K,e,E":
        cinsiyet = input(
            "Cinsiyet icin Yanlis Karakter Girdiniz...Lutfen Tekrar Giriniz..\nCinsiyetinizi Giriniz(Kadin:K/k Erkek:E/e):")
    ikamet_Yeri = input("İkamet Ettiginiz Yeri Giriniz(Aile:A/a ,Yurt:Y/y ,Ogrenci Evi:E/e):")
    if ikamet_Yeri not in "e,E,y,Y,A,a":
        ikamet_Yeri = input("Ikamet Yeri icin Hatali Karakter Girisi Yaptiniz...\nIkamet Yerinizi"
                            " Seceneklere Gore Giriniz(Aile:A/a ,Yurt:Y/y ,Ogrenci Evi:E/e):")

    if ikamet_Yeri == "E" or ikamet_Yeri == "e":
        evde_kalan_say += 1
    elif ikamet_Yeri == "Y" or ikamet_Yeri == "y":
        yurtta_kalan_say += 1
    elif ikamet_Yeri == "A" or ikamet_Yeri == "a":
        aileyle_kalan_say += 1

    ders_Kredi = int(input("Aldiginiz Dersin Kredisini Giriniz:"))
    while ders_Kredi>0:
        alinan_Ders_Say+=1
        alinan_kredi_say+=ders_Kredi
        ders_Notu=int(input("Aldiginiz Dersin Notunu Giriniz:"))

        while ders_Notu<0 or ders_Notu>100:
            print("Ders Notunu 0-100 Arasında Girmelisiniz! ")
            ders_Notu = int(input("Aldiginiz Dersin Notunu Giriniz:"))

        agirlikli_not_say+=ders_Kredi*ders_Notu

        if 60<=ders_Notu:
            basarili_kredi_say+=ders_Kredi
            basarili_ders_say+=1

        ders_Kredi = int(input("Aldiginiz Dersin Kredisini Giriniz:"))
        if(ders_Kredi<=0): #eger ogrenci 0 veya küçük bir kredi girerse ders girdisi sonlanır ve bilgileri yazdırılır

            agirlikli_not_ortalama = agirlikli_not_say / alinan_kredi_say
            ders_basari_yuzdesi = 100 * basarili_ders_say / alinan_Ders_Say
            kredi_basari_yuzdesi = 100 * basarili_kredi_say / alinan_kredi_say

            if agirlikli_not_ortalama < 35:
                temel_Burs = 0
                ek_Katsayi = 0
                ek_Burs = ek_Katsayi * agirlikli_not_ortalama
                aylik_Burs = ek_Burs + temel_Burs
            elif 35 <= agirlikli_not_ortalama < 60:
                temel_Burs = 100
                ek_Katsayi = 0
                ek_Burs = ek_Katsayi * agirlikli_not_ortalama
                aylik_Burs = ek_Burs + temel_Burs
            elif 60 <= agirlikli_not_ortalama < 70:
                temel_Burs = 140
                ek_Katsayi = 1.2
                ek_Burs = ek_Katsayi * agirlikli_not_ortalama
                aylik_Burs = ek_Burs + temel_Burs
            elif 70 <= agirlikli_not_ortalama < 80:
                temel_Burs = 170
                ek_Katsayi = 1.3
                ek_Burs = ek_Katsayi * agirlikli_not_ortalama
                aylik_Burs = ek_Burs + temel_Burs
            elif 80 <= agirlikli_not_ortalama < 90:
                temel_Burs = 190
                ek_Katsayi = 1.5
                ek_Burs = ek_Katsayi * agirlikli_not_ortalama
                aylik_Burs = ek_Burs + temel_Burs
            else:
                temel_Burs = 200
                ek_Katsayi = 1.8
                ek_Burs = ek_Katsayi * agirlikli_not_ortalama
                aylik_Burs = ek_Burs + temel_Burs

            if agirlikli_not_ortalama>=60:
                if ikamet_Yeri == "e" or ikamet_Yeri == "E":
                    basarili_ev += 1
                elif ikamet_Yeri == "y" or ikamet_Yeri == "Y":
                    basarili_yurt += 1
                elif ikamet_Yeri == "a" or ikamet_Yeri == "A":
                    basarili_aile += 1

            if aylik_Burs>=max_alinan_burs:
                max_ad_soyad =ad_Soyad
                max_agirlikli_not_ort=agirlikli_not_ortalama
                max_alinan_burs=aylik_Burs
                max_ders_say=alinan_Ders_Say
                max_kredi_say=alinan_kredi_say

            if agirlikli_not_ortalama>=okul_birinci_agirlikli_not_ort:
                okul_birinci_ad_soyad=ad_Soyad
                okul_birinci_agirlikli_not_ort=agirlikli_not_ortalama
                okul_birinci_burs=aylik_Burs
                okul_birinci_ders_say=alinan_Ders_Say
                okul_birinci_kredi_say=alinan_kredi_say

            if aylik_Burs>300:
                uc_yuzden_fazla_burs_say+=1

            if alinan_Ders_Say==basarili_ders_say:
                tum_dersleri_basarili_ogrenci_say+=1

            if ders_basari_yuzdesi>=75 or kredi_basari_yuzdesi>=75:
                basari_yuzdesi_yetmis_bes+=1

            if alinan_Ders_Say<3 or alinan_kredi_say<10:
                ders_uc_kredi_on+=1
            if agirlikli_not_ortalama < 35:
                basari_Durumu = "Basarisiz"
                basarisiz_say += 1
            elif 35 <= agirlikli_not_ortalama < 60:
                basari_Durumu = "Ortalama"
                ortalama_say += 1
            elif 60 <= agirlikli_not_ortalama<85:
                basari_Durumu = "Basarili"
                basarili_say += 1
            elif 85 <= agirlikli_not_ortalama:
                basari_Durumu = "Ustun Basarili"
                ustun_basarili_say += 1

            if cinsiyet == "K" or cinsiyet == "k":
                kadin_ogrenci_say += 1
                kadin_agirlikli_not_ort_toplam+=agirlikli_not_ortalama
            elif cinsiyet == "E" or cinsiyet == "e":
                erkek_ogrenci_say += 1
                erkek_agirlikli_not_ort_toplam+=agirlikli_not_ortalama

            toplam_agirlikli_not_ort+=agirlikli_not_ortalama
            toplam_kredi_say+=alinan_kredi_say
            ogrencilere_Odenen_Toplam_Burs+=aylik_Burs
            print(ogrenci_No," numaralı"," Sayın ",ad_Soyad)
            print("Bu Donemde Aldiginiz Derslerin Sayisi:", alinan_Ders_Say, end=" ")
            print("Ve Kredi Toplamlari:", alinan_kredi_say)
            print("Basarili Oldugu Ders Sayisi:",basarili_ders_say,"ve Toplam Kredi Sayisi",basarili_kredi_say)
            print("Krediye Gore Basari Yuzdesi:",format(kredi_basari_yuzdesi,".2f"))
            print("Derse Gore Basari Yuzdesi:",format(ders_basari_yuzdesi,".2f"))
            print("Agirlikli Not Ortalamasi:",format(agirlikli_not_ortalama,".2f"))
            print("Basari Durumu:",basari_Durumu)
            print("Sonraki Dönem Alacagi Aylik Burs Miktari (TL):",format(aylik_Burs,".2f"))

    ogrenci_No = int(input("Lutfen Oğrenci Numaranizi Giriniz:"))

basari_yuzde_ev=basarili_ev/evde_kalan_say
basari_yuzde_yurt=basarili_yurt/yurtta_kalan_say
basari_yuzde_aile=basarili_aile/aileyle_kalan_say
#basarili ikamet kıyas
if basari_yuzde_ev<basari_yuzde_yurt and basari_yuzde_ev<basari_yuzde_aile:
        min_ikamet = "Ev"
elif basari_yuzde_yurt<basari_yuzde_aile and basari_yuzde_yurt<basari_yuzde_ev:
        min_ikamet = "Yurt"
else:
        min_ikamet = "Aile"

print("*******")
print("Basarisiz Ogrencilerin Sayisi:",basarisiz_say,"Tum Ogrenciler Arasindaki Yuzdesi:",format(basarisiz_say*100/ogrenci_say,".2f"))
print("Ortalama Ogrencilerin Sayisi:",ortalama_say,"Tum Ogrenciler Arasindaki Yuzdesi:",format(ortalama_say*100/ogrenci_say,".2f"))
print("Basarili Ogrencilerin Sayisi:",basarili_say,"Tum Ogrenciler Arasindaki Yuzdesi:",format(basarili_say*100/ogrenci_say,".2f"))
print("Ustun Basarili Ogrencilerin Sayisi:",ustun_basarili_say,"Tum Ogrenciler Arasindaki Yuzdesi:",format(ustun_basarili_say*100/ogrenci_say,".2f"))
print("Kadinlar Icin Agirlikli Not Ortalamalarinin Ortalamasi:",format(kadin_agirlikli_not_ort_toplam/kadin_ogrenci_say,".2f"))
print("Erkekler Icin Agirlikli Not Ortalamalarinin Ortalamasi:",format(erkek_agirlikli_not_ort_toplam/erkek_ogrenci_say,".2f"))
print("Tum Ogrenciler Icin Agirlikli Not Ortalamalarinin Ortalamasi:",format(toplam_agirlikli_not_ort/ogrenci_say,".2f"))
print("Tum Ogrenciler Icin Toplam Kredi Ortalamasi:",format(toplam_kredi_say/ogrenci_say,".2f"))
print("O Donem Aldigi Ders Sayisi 3'ten Az veya Toplam Kredisi 10'dan Az Olan Ogrencilerin Sayisi ve Yuzdesi:",end=" ")
print("Sayisi:",ders_uc_kredi_on,"Yuzdesi:",format(100*ders_uc_kredi_on/ogrenci_say,".2f"))
print("O Donem Aldigi Derslerin Sayisina veya Toplam Kredisine Gore Basari Yuzdesi 75 ve Ustunde Olan Ogrencilerin Sayisi ve Yuzdesi:",end=" ")
print("Sayisi:",basari_yuzdesi_yetmis_bes,"Yuzdesi:",format(100*basari_yuzdesi_yetmis_bes/ogrenci_say,".2f"))
print("Tum Dersleri Basarili Olan Ogrencilerin Sayisi ve Yuzdesi:",end=" ")
print("Sayisi:",tum_dersleri_basarili_ogrenci_say,"Yuzdesi:",format(100*tum_dersleri_basarili_ogrenci_say/ogrenci_say,".2f"))
print("Sonraki Donem Alacagi Burs Miktari 300(TL)'den Fazla Olan Ogrencilerin Sayisi",format(uc_yuzden_fazla_burs_say,".2f"))
print("*******")
print("O Donem Okul Birincisi Olan Ogrencinin: ")
print("Adi-Soyadi:",okul_birinci_ad_soyad)
print("O Donem Aldigi Derslerin Sayisi:",okul_birinci_ders_say)
print("O Donem Aldigi Toplam Kredi:",okul_birinci_kredi_say)
print("O Donemki Agirlikli Not Ortalamasi:",format(okul_birinci_agirlikli_not_ort,".2f"))
print("Sonraki Donem Alacagi Burs Miktari(TL):",format(okul_birinci_burs,".2f"))
print("*******")
print("Sonraki Donem En Cok Aylik Burs Alacak Ogrencinin: ")
print("Adi-Soyadi:",max_ad_soyad)
print("O Donem Aldigi Derslerin Sayisi:",max_ders_say)
print("O Donem Aldigi Toplam Kredi:",max_kredi_say)
print("O Donemki Agirlikli Not Ortalamasi:",format(max_agirlikli_not_ort,".2f"))
print("Sonraki Donem Alacagi Aylik Burs Miktari(TL):",format(max_alinan_burs,".2f"))
print("*******")
print("Tum Ogrencilere Sonraki Donem Her Ay Odenecek Toplam Burs Miktari:",format(ogrencilere_Odenen_Toplam_Burs,".2f"))
print("Basarili Ogrencilerin Yuzdesinin En Dusuk Oldugu Ikamet Yeri:",min_ikamet)