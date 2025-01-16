from market import Market

# Kullanıcı menüsü
def menu():
    market = Market()

    while True:
        print("\n*** Çevrimiçi Market Alışveriş Sepeti ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")

        choice = input("Lütfen bir seçenek seçin (1-4): ")

        if choice == "1":
            market.list_product()
        elif choice == "2":
            market.add_product()
        elif choice == "3":
            market.delete_product()
        elif choice == "4":
            print("Çıkış yapılıyor...")
            del market  # Market nesnesini yok eder (dosya kapanır)
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

# Menüyü başlat
menu()
