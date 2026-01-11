# Sanal Mantık Devresi Simülatörü (Proje Grubu 3)

Bu proje, **BLM101 - Bilgisayar Mühendisliğine Giriş** dersi final ödevi kapsamında hazırlanmıştır. Python dili kullanılarak temel mantık kapılarının simülasyonunu ve karmaşık mantık ifadelerinin doğruluk tablolarını oluşturmayı amaçlar.

## Öğrenci Bilgileri
* **Ad Soyad:** Enes Seçmen
* **Öğrenci No:** 25360859307
* **Proje Konusu: : Kullanıcının temel mantık kapılarını kullanarak basit bir devre tasarlamasını
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

## Algoritma Mantığı
Program `while` döngüsü ile sürekli çalışır ve kullanıcıdan seçim bekler.
* **Basit Hesaplama:** `logic_gate` fonksiyonu ile AND, OR ve XOR işlemleri bit düzeyinde (bitwise operations) yapılır.
* **Doğruluk Tablosu:** `itertools.product` kullanılarak 3 bitlik tüm kombinasyonlar (2^3 = 8 durum) otomatik oluşturulur ve kullanıcının girdiği ifade dinamik olarak hesaplanır.
