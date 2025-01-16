class Market:
    def __init__(self):
        """Market sınıfı yapıcı metodu: product.txt dosyasını kontrol eder ve yoksa oluşturur."""
        try:
            self.file = open("product.txt", "a+")
            self.file.seek(0)  # Dosyanın başına gider
        except Exception as e:
            print(f"Dosya oluşturulurken bir hata oluştu: {e}")

    def __del__(self):
        """Market sınıfı yıkıcı metodu: Dosyayı kapatır."""
        if hasattr(self, 'file'):
            self.file.close()
            print("product.txt dosyası kapatıldı.")

    def list_product(self):
        """Dosyadaki ürünleri listeler."""
        self.file.seek(0)  # Dosyanın başına gider
        products = self.file.readlines()  # Tüm satırları okur

        if not products:
            print("Ürün listesi boş!")
        else:
            print("Mevcut Ürünler:")
            print("-" * 30)
            for product in products:
                name, category, price, stock = product.strip().split(",")  # Ürünü ayırır
                print(f"Ad: {name}, Kategori: {category}, Fiyat: {price}, Stok: {stock}")
            print("-" * 30)

    def add_product(self):
        """Kullanıcıdan ürün bilgilerini alıp dosyaya ekler."""
        name = input("Ürün adı: ")
        category = input("Kategori: ")
        price = input("Fiyat: ")
        stock = input("Stok miktarı: ")

        new_product = f"{name},{category},{price},{stock}\n"
        self.file.write(new_product)
        self.file.flush()  # Veriyi hemen dosyaya yazar
        print(f"{name} ürünü başarıyla eklendi!")

    def delete_product(self):
        """Kullanıcıdan ürün adını alıp dosyadan siler."""
        self.file.seek(0)  # Dosyanın başına gider
        products = self.file.readlines()  # Tüm ürünleri okur

        if not products:
            print("Ürün listesi boş, silinecek bir şey yok!")
            return

        # Kullanıcıdan silinecek ürün adı alınır
        product_name = input("Silmek istediğiniz ürünün adını girin: ").strip()

        # Ürünleri filtreler
        updated_products = [p for p in products if not p.startswith(product_name + ",")]

        if len(updated_products) == len(products):
            print(f"{product_name} adlı ürün bulunamadı.")
        else:
            # Dosyayı günceller
            self.file.close()  # Mevcut dosyayı kapatır
            with open("product.txt", "w") as file:
                file.writelines(updated_products)
            self.file = open("product.txt", "a+")  # Dosyayı yeniden açar
            print(f"{product_name} ürünü başarıyla silindi!")

