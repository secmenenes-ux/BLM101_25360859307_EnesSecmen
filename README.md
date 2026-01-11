# Sanal Mantık Devresi Simülatörü (Proje Grubu 3)

Bu proje, **BLM101 - Bilgisayar Mühendisliğine Giriş** dersi final ödevi kapsamında hazırlanmıştır. Python dili kullanılarak temel mantık kapılarının simülasyonunu ve karmaşık mantık ifadelerinin doğruluk tablolarını oluşturmayı amaçlar.

## Öğrenci Bilgileri
* **Ad Soyad:** Enes Seçmen
* **Öğrenci No:** 25360859307
* **Proje Konusu:** Kullanıcının temel mantık kapılarını kullanarak basit bir devre tasarlamasını
(veya metin olarak girmesini) sağlayan program.
* **Bölüm:** Bilgisayar Mühendisliği
* **Ders:** BLM101

## Proje Tanıtım Videosu
Projenin çalışma mantığını ve kod anlatımını içeren YouTube videosuna aşağıdaki linkten ulaşabilirsiniz:
[Buraya YouTube Video Linki]

##  Proje İçeriği ve Özellikler
Bu program iki ana modülden oluşmaktadır:

### 1. Temel Mantık Kapısı Hesaplayıcı
Kullanıcıdan iki adet binary giriş (0 veya 1) ve bir mantık kapısı türü alır. Seçilen kapıya göre işlemi gerçekleştirip sonucu ekrana basar.

* **Desteklenen Kapılar:** AND, OR, XOR.

### 2. 3 Değişkenli Doğruluk Tablosu Oluşturucu
Proje isterlerinde belirtildiği üzere, 3 değişkenli (A, B, C) mantıksal ifadelerin tüm olasılıklarını hesaplar.
* **Özelleştirilebilir İfade:** Kullanıcı `A and (B or C)` gibi karmaşık ifadeler girebilir.
* **Desteklenen Operatörler:** `and`, `or`, `not` ve parantez `()` işlemleri.
* Program, A, B ve C'nin tüm kombinasyonları (000'dan 111'e kadar) için döngü kurar ve her adımda sonucu tablo halinde listeler.

### 3. Proje Dokümantasyonu
Projemde Python'un kendi içerisinde gelen standart kütüphaneleri dışında herhangi bir ekstra kütüphane indirmedim.
**itertools**: Bu kütüphaneyi doğruluk tablosu oluştururken kullandım.Doğruluk tablosu kısmında 3 değişken olduğu için toplamda 8 farklı ihtimal oluşuyordu. Bunları elimle tek tek yazmak yerine itertools.product fonksiyonu ile otomatik ürettirdim.

**Algoritma ve Çalışma Mantığı** : Programım sonsuz bir döngü (while True) içerisinde çalışıyor, böylece işlem bitince kapanmıyor ve yeni işlem yapabiliyoruz. Algoritmayı **iki** ana parçaya böldüm:

**1. Basit Hesaplama Kısmı:** Kullanıcıdan input() ile iki tane sayı (0 veya 1) ve bir de kapı ismi istiyorum.
Aldığım kapı ismini if-elif-else bloklarıyla kontrol ediyorum.
Eğer kullanıcı `AND` dediyse **&** operatörünü, `OR` dediyse **|** operatörünü, `XOR` dediyse **^** operatörünü kullanıyorum .
Hatalı bir giriş yapılırsa program kullanıcıyı uyarıyor.

**2. Doğruluk Tablosu Kısmı :** Burada kullanıcıdan `A and (B or C)` gibi sözel bir ifade girmesi bekleniyor.
Kombinasyonların oluşturulması esnasında 3 değişken (A, B, C) olduğu için toplam 8 farklı durum (000, 001... 111 gibi) oluşuyor. Bu durumları tek tek elle yazmak yerine itertools kütüphanesiyle otomatik ürettirdim.
Kurulan bu döngü, bu 8 durumu sırasıyla geziyor. Her adımda A, B ve C'nin o anki değerlerini alıp, Python'un `eval()` fonksiyonu sayesinde kullanıcının yazdığı formülü matematiksel işleme döküyor ve sonucu tabloya yazdırıyor.
