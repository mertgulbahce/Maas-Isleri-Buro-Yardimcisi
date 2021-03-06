# Maas_Isleri_Buro_Yardimcisi
# Analiz
Maaş işleri büro yardımcısı programında hedeflenen; iş yeri olan ve bünyesinde çalışanları olan insanlara yardımcı olabilmektir. 
Bu bağlamda çalışan insanların aldığı aylık maaşlar; engelli - engelsiz durumları ve buna göre değişen vergi indirimleri(engel derecelerine göre), medeni durumları çünkü eğer evliyse ek ödeneklere göre kullanıcıya sunulmuştur. Bu bilgiler sayesinde 
güzel bir istatistik çıkarılmış da olunur. Bu program her çalışandan; TC kimlik numarası, ad soyad, aylık brüt ücreti, medeni 
durumuyla beraber eşinin çalışıp çalışmadığı, engelli olup olmadığıyla beraber engelliyse derecesini girdi olarak kullanıcıdan 
alır. Kullanıcıdan alınan bu bilgiler doğrultusunda, her çalışan için özel ayrıca bütün çalışanlarla ilgili çıktılar istenmektedir. Ayrıca bütün girilen çalışanlar kapsamında ilgili çıktılar istenmektedir. Program bunların hepsini kullancıya sunar.

# Tasarım
Problemin tanımından yola çıkacak olursak bu uygulamaya girecek çalışan sayımız elimizde net bir sayı olarak belli değildir 
ve her çalışan için farklı farklı değerler girilecektir. Bunun için en başta evet/hayır sorusunu kapsayan bir WHİLE döngüsü oluşturmalıyız. Her çalışan girdilerinin sonunda kullanıcıya devam etmek isteyip istemeyeceği yani başka çalışan girişinin olup olmayacağı sorulacak eğer cevap 'evet' ise döngü devam edecek, 'hayır' ise döngüden çıkılacak ve tüm çalışanlar kapsamında istenen 
genel çıktılara geçilecektir. Yani kısaca bütün çalışan işlemleri ve hesaplamalar bu döngünün içinde gerçekleşecek, döngünün dışında 
ise tüm çalışanlar geneli çıktılar yer alacaktır. Eğer döngünün içine girecek olursak; döngünün içine ilk girilir girilmez tüm çalışanlar için girilen ortak girdiler kullanıcıdan istenecektir. Bunlar çalışanın adı-soyadı, TC kimlik numarası, aylık brüt ücret, medeni durumu ve evliyse eşinin çalışma durumu ve eğer evliyse çalışanın bakmakla yükümlü olduğu çocuk sayısı buna ilaveten  altı yaşından büyük çocuk sayısı, engel durumu ve çalışan eğer engelliyse engel oranı istenecektir. Bu girdilerden sonra çalışanın maaş işleri büro yardımcısı uygulaması kapsamına göre ayrı ayrı 'IF' koşul durumları açılıp içlerinde gerekli işlemleri yaptırılır.
Örneğin çalışanın medeni durumuna göre (if) evliyse eşinin çalışma durumu(if) bakmakla yükümlü olduğu çocuk sayısı(if) ve en son 
altı yaşından büyük çocuk sayısı için (if) ‘IF’ler açılarak girdiler sonucu istenen çıktıları sağlayacak işlemler bu ayrı ayrı koşul durumları içinde gerçekleştirilir. Yapılan işlemler sonrasında her çalışan için analiz bölümünde belirttiğimiz çıktılar ‘print’ aracılığıyla yazılır. 
Bunların dışında en başta koşul durumlarına ayırdığımız çalışanların; mesela evli olmayanları ve ya engel durumu olmayanları için döngüler devam eder çünkü ‘WHILE’ içinde ‘IF’ ler devam eder. Böylece döngü kullanıcı en son ‘Başka Çalışanınız Var Mı?’ diye sorana kadar devam eder ve cevap h/H girilirse program işlemeyi bitirir. Sonunda tüm çalışanlara ait girdilerin çıktıları son kısımda ‘print’ ile ekrana istenen şekilde yazdırılır ve program sonlanır.
