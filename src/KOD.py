import itertools

# Temel mantık kapılarını hesaplayan fonksiyon
def kapi_hesapla(kapi_turu, a, b):
    # Gelen değerleri sayıya çevirme
    a = int(a)
    b = int(b)
    
    # Kapı türüne göre işlem yap
    if kapi_turu == "AND":
        return a & b
    elif kapi_turu == "OR":
        return a | b
    elif kapi_turu == "XOR":
        return a ^ b
    else:
        return None

# Kullanıcının girdiği karmaşık ifadeyi (Örn: A and B or C) çözen fonksiyon
def ifadeyi_coz(ifade, A, B, C):
    try:
        # İfadeyi küçük harfe çevir (AND -> and)
        ifade = ifade.lower()
        
        #  sembol dönüşümü
        ifade = ifade.replace("xor", "^")
        
        # eval fonksiyonu a, b, c harflerini arayacak değerleri eşleştiriyoruz
        degerler = {'a': A, 'b': B, 'c': C}
        
        # İfadeyi hesapla 
        sonuc = eval(ifade, {}, degerler)
        
        # Sonuç True/False çıkarsa 1 veya 0 yap
        return 1 if sonuc else 0
    except:
        return "Hata"

# 3 değişkenli doğruluk tablosunu oluşturan fonksiyon
def dogruluk_tablosu(ifade_metni):
    print(f"\n--- Doğruluk Tablosu: {ifade_metni} ---")
    print("-" * 45)
    print("|  A  |  B  |  C  |         SONUÇ          |")
    print("-" * 45)
    
    # 3 bit için tüm kombinasyonlar (000, 001 ... 111)
    # itertools kütüphanesi bu kombinasyonları bizim için üretir
    tum_durumlar = list(itertools.product([0, 1], repeat=3))
    
    for durum in tum_durumlar:
        A, B, C = durum # Sırasıyla değerleri al
        
        # Fonksiyona gönderip sonucu alıyoruz
        sonuc = ifadeyi_coz(ifade_metni, A, B, C)
        
        # Tablo satırını yazdır
        print(f"|  {A}  |  {B}  |  {C}  |           {sonuc}            |")
    print("-" * 45)

# Programın ana kısmı
def main():
    print("=== BLM101 Mantık Devresi Projesi ===")
    
    while True:
        print("\n[MENÜ]")
        print("1. Basit Hesaplama (AND, OR, XOR)")
        print("2. Doğruluk Tablosu Oluştur (3 Değişkenli)")
        print("3. Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == '1':
            try:
                # Kullanıcıdan girişleri al
                g1 = input("1. Giriş (0/1): ")
                g2 = input("2. Giriş (0/1): ")
                kapi = input("Kapı (AND, OR, XOR): ").upper()
                
                # Girişler 0 veya 1 mi kontrol et
                if g1 not in ['0', '1'] or g2 not in ['0', '1']:
                    print("Hata: Sadece 0 veya 1 girebilirsiniz!")
                    continue
                
                sonuc = kapi_hesapla(kapi, g1, g2)
                
                if sonuc is None:
                    print("Hatalı kapı ismi girdiniz! (Sadece AND, OR, XOR)")
                else:
                    print(f"\n>>> SONUÇ: {sonuc}")
                    
            except ValueError:
                print("Lütfen sayı giriniz.")

        elif secim == '2':
            print("\nTablo Modu: A, B ve C değişkenlerini kullanın.")
            print("Örnek: A and (B xor C)")
            
            formul = input("İfadeyi yazın: ")
            
            if formul.strip() != "":
                dogruluk_tablosu(formul)
            else:
                print("Boş ifade girdiniz.")
                
        elif secim == '3':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Yanlış seçim yaptınız, tekrar deneyin.")

if __name__ == "__main__":
    main()