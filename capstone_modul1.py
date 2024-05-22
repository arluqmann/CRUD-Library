### Capstone Project Modul 1 (Python Programming Fundamental)
### JCDS 2404005 - Arief Luqman Hakiem
### Studi Kasus: Peminjaman Buku pada Perpustakaan


# Import Library
import tabulate as tb
import datetime as dt
import random as rd
import os


# Referensi Tabel Data
## Daftar buku yang tersedia untuk dipinjam di perpustakaan
books = [{"isbn": 0, "title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "category": "Personal Development", "language": "English", "pages": 304, "published year": 2008, "publisher": "Jossey-Bass Inc.", "availability": "Available", "quantity": 6},
         {"isbn": 0, "title": "Negeri Para Bedebah", "author": "Tere Liye", "category": "Novels", "language": "Indonesian", "pages": 440, "published year": 2018, "publisher": "Gramedia Pustaka Utama", "availability": "Available", "quantity": 4},
         {"isbn": 0, "title": "Laut Bercerita", "author": "Leila S. Chudori", "category": "Novels", "language": "Indonesian", "pages": 380, "published year": 2017, "publisher": "Kepustakaan Populer Gramedia", "availability": "Available", "quantity": 4},
         {"isbn": 0, "title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "category": "Philosophy", "language": "English", "pages": 165, "published year": 2006, "publisher": "Beacon Press", "availability": "Available", "quantity": 3},
         {"isbn": 0, "title": "The Things You Can See Only When You Slow Down", "author": "Haemin Sunim", "category": "Personal Development", "language": "English", "pages": 288, "published year": 2017, "publisher": "Penguin Life", "availability": "Borrowed", "quantity": 0},
         {"isbn": 0, "title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "category": "Personal Development", "language": "English", "pages": 372, "published year": 2004, "publisher": "Free Press", "availability": "Available", "quantity": 3},
         {"isbn": 0, "title": "Catatan Seorang Demonstran", "author": "Soe Hok Gie", "category": "History", "language": "Indonesian", "pages": 386, "published year": 2005, "publisher": "Pustaka LP3ES Indonesian", "availability": "Borrowed", "quantity": 0},
         {"isbn": 0, "title": "Applied Geophysics", "author": "W. M. Telford", "category": "Academic", "language": "English", "pages": 792, "published year": 1990, "publisher": "Cambridge University Press", "availability": "Available", "quantity": 1},
         {"isbn": 0, "title": "Introduction to Electrodynamics", "author": "David J. Griffiths", "category": "Academic", "language": "English", "pages": 618, "published year": 2017, "publisher": "Cambridge University Press", "availability": "Available", "quantity": 2},
         {"isbn": 0, "title": "Python Data Science Handbook", "author": "Jake Vanderplas", "category": "Academic", "language": "English", "pages": 546, "published year": 2017, "publisher": "O'Reilly Media", "availability": "Available", "quantity": 5},
         {"isbn": 0, "title": "The Guns of August", "author": "Barbara W. Tuchman", "category": "History", "language": "English", "pages": 608, "published year": 2014, "publisher": "Random House Trade Paperbacks", "availability": "Available", "quantity": 3},
         {"isbn": 0, "title": "Habis Gelap Terbitlah Terang", "author": "Raden Adjeng Kartini", "category": "Biography", "language": "Indonesian", "pages": 205, "published year": 2004, "publisher": "Balai Pustaka", "availability": "Borrowed", "quantity": 0},
         {"isbn": 0, "title": "Sang Pemimpi", "author": "Andrea Hirata", "category": "Novels", "language": "Indonesian", "pages": 276, "published year": 2020, "publisher": "Bentang Pustaka", "availability": "Available", "quantity": 8},
         {"isbn": 0, "title": "The Giving Tree", "author": "Shel Silverstein", "category": "Childrens", "language": "English", "pages": 64, "published year": 2010, "publisher": "Penguin Books UK", "availability": "Available", "quantity": 4},
         {"isbn": 0, "title": "Charlotte's Web", "author": "E. B. White", "category": "Childrens", "language": "English", "pages": 184, "published year": 2012, "publisher": "Harper Collins", "availability": "Available", "quantity": 7}
         ]

## Daftar buku yang sedang dipinjam
borrowed_books = [{"account id": 1874, "isbn": 0, "title": "Laut Bercerita", "quantity": 1, "borrowed date": "20-05-2024", "returned date": "04-05-2024"},
                  {"account id": 2576, "isbn": 0, "title": "The Things You Can See Only When You Slow Down", "quantity": 1, "borrowed date": "13-05-2024", "returned date": "27-05-2024"},
                  {"account id": 6423, "isbn": 0, "title": "Catatan Seorang Demonstran", "quantity": 1, "borrowed date": "14-05-2024", "returned date": "28-05-2024"},
                  {"account id": 4635, "isbn": 0, "title": "Habis Gelap Terbitlah Terang", "quantity": 1, "borrowed date": "15-05-2024", "returned date": "29-05-2024"},
                  {"account id": 4635, "isbn": 0, "title": "The Giving Tree", "quantity": 1, "borrowed date": "05-05-2024", "returned date": "19-05-2024"}
                  ]

## Daftar pengunjung perpustakaan
pengunjung = [{"name": "Tyler Durden", "account id": 1874},
              {"name": "Hermione Granger", "account id": 2576},
              {"name": "Arief Luqman", "account id": 6423},
              {"name": "Gracie Abrams", "account id": 4635}
              ]

# Fungsi Bagian Pertama
## Fungsi tampilan menu utama administrator
def menu_admin():
    print("""
    -----------------------------------------
       MENU UTAMA PENGELOLAAN PERPUSTAKAAN
    -----------------------------------------
    Daftar Menu:
    1. Menampilkan Daftar Buku Perpustakaan
    2. Membuat Daftar Buku Baru
    3. Memperbarui Daftar Buku
    4. Menghapus Daftar Buku 
    5. Ganti Pilihan Kuasa
    0. Keluar dari Program
          """)

## Fungsi tampilan menu utama pengunjung
def menu_customer():
    print("""
    -----------------------------------------------
       SELAMAT DATANG DI PERPUSTAKAAN GOOD NIGHT
    -----------------------------------------------
    Daftar Menu:
    1. Menampilkan Daftar Buku Perpustakaan
    2. Meminjam Buku
    3. Mengembalikan Buku 
    4. Ganti Pilihan Kuasa
    0. Keluar dari Program
          """)

## Fungsi tampilan menu pada baca data bagian administrator
def read_menu_admin():
    print("""
    -------------------------------
               READ MENU 
    -------------------------------
    Daftar Read Menu:
    1. Menampilkan Seluruh Daftar Buku Perpustakaan
    2. Menampilkan Seluruh Daftar Buku yang sedang Dipinjam
    3. Menampilkan Daftar Pengunjung Perpustakaan
    4. Melakukan Pencarian Daftar Buku Berdasarkan ISBN
    5. Kembali Ke Menu Utama
    0. Keluar dari Program
          """)

## Fungsi tampilan menu pada baca data bagian pengunjung
def read_menu_customer():
    print("""
    -------------------------------
               READ MENU 
    -------------------------------
    Daftar Read Menu:
    1. Menampilkan Seluruh Daftar Buku Perpustakaan
    2. Menampilkan Daftar Buku yang sedang Dipinjam
    3. Melakukan Pencarian Daftar Buku Berdasarkan ISBN
    4. Kembali Ke Menu Utama
    0. Keluar dari Program
          """)

## Fungsi tampilan menu pada membuat data (khusus administrator)
def create_menu():
    print("""
    -------------------------------
               CREATE MENU 
    -------------------------------
    Daftar Create Menu:
    1. Menambah Daftar Buku
    2. Kembali Ke Menu Utama
    0. Keluar dari Program
          """)

## Fungsi tampilan menu pada memperbarui data (khusus administrator)
def update_menu():
    print("""
    -------------------------------
               UPDATE MENU 
    -------------------------------
    Daftar Update Menu:
    1. Memperbarui Daftar Buku
    2. Kembali Ke Menu Utama
    0. Keluar dari Program
          """)

## Fungsi tampilan menu pada menghapus data (khusus administrator)
def delete_menu():
    print("""
    -------------------------------
               DELETE MENU 
    -------------------------------
    Daftar Delete Menu:
    1. Menghapus Baris Daftar Buku
    2. Menghapus Seluruh Daftar Buku
    3. Kembali Ke Menu Utama
    0. Keluar dari Program
          """)

## Fungsi tampilan menu pada fitur pertama (peminjaman buku)
def borrowed_book_menu():
    print("""
    ----------------------------------
            BORROWED BOOK MENU
    ----------------------------------
    Daftar Menu:
    1. Meminjam Buku
    2. Kembali Ke Menu Utama
    0. Keluar dari Program
          """)

## Fungsi tampilan menu pada fitur kedua (pengembalian buku)
def returned_book_menu():
    print("""
    ----------------------------------
            RETURNED BOOK MENU
    ----------------------------------
    Daftar Menu:
    1. Mengembalikan Buku
    2. Kembali Ke Menu Utama
    0. Keluar dari Program
          """)

## Fungsi tampilan menu pada pemilihan kuasa
def pilihan_menu():
    print("""
    -------------------------------
               PILIHAN AKSES
    -------------------------------
    Pilih Menu untuk Mengakses Perpustakaan:
    1. Administrator
    2. Pengunjung
    0. Keluar dari Program
          """)

## Fungsi tampilan ketika program berakhir bagian administrator
def exit_menu_admin():
    print("""
    Program telah diselesaikan.
    Terima kasih telah menggunakan program ini!
          """)

## Fungsi tampilan ketika program berakhir bagian pengunjung
def exit_menu_customer():
    print("""
    Program telah diselesaikan.
    Terima kasih telah berkunjung!
          """)


# Fungsi Bagian Kedua (tambahan: sorting dan filtering)
## Fungsi clearing layar sistem komputer
def clear():
    if os.name == "posix":  # Penggunaan sistem macos/linux
        os.system("clear")
    elif os.name == "nt":   # Penggunaan sistem windows
        os.system("cls")

## Fungsi generate ISBN
def generateISBN(pages, published_year, library_code = 22):
    year_suffix = str(published_year)[-2:]
    isbn = f"{library_code}{pages}{year_suffix}"
    return isbn

## Fungsi generate account secara acak
def generateAcc():
    account = str(rd.randint(1000, 9999))
    return account

## Fungsi membuat dan menambahkan account data ke dalam list pengunjung
def create_account():
    while True:
        name = input("Masukkan nama Anda (2 kata): ").title().strip()
        if len(name.split()) == 2:
            break
        else:
            print("Nama harus terdiri dari dua kata. Silakan coba kembali")
    
    number = generateAcc()
    add_pengunjung = {"name": name, "account id": number}
    pengunjung.append(add_pengunjung)
    print(f"Account anda berhasil dibuat dengan id: {number}")


## Fungsi melakukan filtering data
def filtering(books=books):
    isbn = input("Masukkan ISBN buku: ")
    filtered_data = [item for item in books if item["isbn"] == isbn]
    print(tb.tabulate(filtered_data, headers="keys", tablefmt="fancy_grid"))

# Fungsi Bagian Ketiga (Administrator)
## Fungsi read menu daftar buku
def read(books):
    for book in books:
        book["isbn"] = generateISBN(book["pages"], book["published year"])
    print(tb.tabulate(books, headers="keys", tablefmt="fancy_grid"))

## Fungsi read menu customer
def read_customer(customer):
    print(tb.tabulate(customer, headers="keys", tablefmt="fancy_grid"))

## Fungsi create menu
def create():
    while True:
        judul = input("Masukkan judul buku: ").title().strip()
        penulis = input("Masukkan penulis: ").title().strip()
        kategori = input("Masukkan kategori: ").title().strip()
        bahasa = input("Masukkan bahasa: ").title.strip()
        halaman = int(input("Masukkan halaman: "))
        tahun_terbit = int(input("Masukkan tahun terbit: "))
        penerbit = input("Masukkan penerbit: ").title().strip()
        status = input("Masukkan kesediaan buku: ").title().strip()
        jumlah = int(input("Masukkan jumlah buku: "))
        isbn = generateISBN(halaman, tahun_terbit)

        data = {"isbn": isbn,
                "title": judul,
                "author": penulis,
                "category": kategori,
                "language": bahasa,
                "pages": halaman,
                "published year": tahun_terbit,
                "publisher": penerbit,
                "availability": status,
                "quantity": jumlah}
        
        books.append(data)

## Fungsi update menu
def update():
    isbn_to_update = input("Masukkan ISBN buku yang ingin diupdate: ").strip()
    for book in books:
        if book["isbn"] == isbn_to_update:
            while True:
                kolom = input("Masukkan Kolom yang Ingin di Edit\n(Judul/Penulis/Kategori/Bahasa/Halaman/Tahun Terbit/Penerbit/Kesediaan/Stok): ").title().strip()
                
                if kolom == "Judul":
                    judulBaru = input("Masukkan Judul Buku baru: ").title().strip()
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["title"] = judulBaru
                            print("Data Judul Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                elif kolom == "Penulis":
                    penulisBaru = input("Masukkan Penulis Buku baru: ").title().strip()
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["author"] = penulisBaru
                            print("Data Penulis Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                elif kolom == "Kategori":
                    kategoriBaru = input("Masukkan Kategori Buku baru: ").title().strip()
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["category"] = kategoriBaru
                            print("Data Kategori Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                elif kolom == "Bahasa":
                    bahasaBaru = input("Masukkan Bahasa Buku baru: ").title().strip()
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["language"] = bahasaBaru
                            print("Data Bahasa Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                elif kolom == "Halaman":
                    halamanBaru = int(input("Masukkan Halaman Buku baru: ").strip())
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["pages"] = halamanBaru
                            print("Data Halaman Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                elif kolom == "Tahun Terbit":
                    tahunTerbitBaru = int(input("Masukkan Tahun Terbit Buku baru: ").strip())
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["published year"] = tahunTerbitBaru
                            print("Data Tahun Terbit Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                elif kolom == "Penerbit":
                    penerbitBaru = input("Masukkan Penerbit Buku baru: ").title().strip()
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["publisher"] = penerbitBaru
                            print("Data Penerbit Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                elif kolom == "Kesediaan":
                    kesediaanBaru = input("Masukkan Kesediaan Buku baru: ").title().strip()
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["availability"] = kesediaanBaru
                            print("Data Kesediaan Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                elif kolom == "Stok":
                    stokBaru = int(input("Masukkan Stok Buku baru: ").strip())
                    while True:
                        pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ").upper().strip()
                        if pertanyaan2 == "Y":
                            book["quantity"] = stokBaru
                            print("Data Stok Diupdate")
                            break
                        elif pertanyaan2 == "N":
                            print("Data Tidak Terupdate")
                            break

                else:
                    print("Kolom yang dimasukkan tidak valid.")

                pertanyaan = input("Ketik Y jika ingin update kolom lain atau N jika ingin selesai (Y/N): ").upper().strip()
                if pertanyaan != 'Y':
                    break
            break
    else:
        print("ISBN tidak ditemukan.")


## Fungsi delete menu
def delete():
    while True:
        id_to_delete = int(input("Masukkan isbn yang ingin dihapus: "))
        found = False
        for book in books:
            if book["isbn"] == id_to_delete:
                found = True
                books.remove(book)
                print(f"Data dengan ISBN {id_to_delete} berhasil dihapus.")
                break
        if not found:
            print("Maaf, ISBN tidak ditemukan.")

# Fungsi Bagian Keempat (Pengunjung)
## Fungsi read menu
def read_borrowedcustomer(books=borrowed_books):
    account_id = input("Masukkan account anda: ")
    filtered_data = [item for item in books if item["account id"] == account_id]
    print(tb.tabulate(filtered_data, headers="keys", tablefmt="fancy_grid"))

## Fungsi peminjaman buku menu
def borrowed_book():
    account_number = input("Masukkan account number anda: ")
    isbn = input("Masukkan ISBN buku: ")
    borrow_date_str = ("Masukkan tanggal peminjaman (dd-mm-yyyy)")
    borrow_date = dt.datetime.strptime(borrow_date_str, "%d-%m-%Y")
    for book in books:
        if book["isbn"] == isbn:
            if book["availability"] > 0:
                book["availability"] -= 1
                borrow_id = len(borrowed_books) + 1
                borrowed_books.append({
                    "account id": account_number,
                    "isbn": isbn,
                    "title": book["title"],
                    "quantity": 1,
                    "borrowed_date": borrow_date,
                    "returned_date": borrow_date + dt.timedelta(days=14)
                })
                print(f"Buku '{book['title']}' berhasil dipinjam.")
            else:
                print("Maaf, buku tidak tersedia untuk dipinjam.")
            return
    print("Buku dengan ISBN tersebut tidak ditemukan.")

## Fungsi pengembalian buku menu
def returned_book():
    account_number = input("Masukkan account number anda: ")
    isbn = input("Masukkan ISBN buku: ")
    borrow_date_str = ("Masukkan tanggal peminjaman (dd-mm-yyyy)")
    borrow_date = dt.datetime.strptime(borrow_date_str, "%d-%m-%Y")
    return_date = borrow_date + dt.timedelta(days=14)
    for borrowed_book in borrowed_books:
        if borrowed_book["account_number"] == account_number and borrowed_book["book"]["isbn"] == isbn:
            borrowed_books.remove(borrowed_book)
            for book in books:
                if book["isbn"] == isbn:
                    book["availability"] += 1
            print(f"Buku '{borrowed_book['book']['title']}' berhasil dikembalikan.")

            # Menghitung jumlah hari terlambat pengembalian
            due_date = borrowed_book["due_date"]
            late_days = (return_date - due_date).days
            if late_days > 0:
                fine = late_days * 500  # Denda Rp500 per hari terlambat
                print(f"Anda telat mengembalikan buku selama {late_days} hari.")
                print(f"Anda dikenakan denda sebesar Rp{fine}.")
            else:
                print("Buku dikembalikan tepat waktu.")
            return
    print("Buku dengan ISBN tersebut tidak ditemukan dalam daftar buku yang sedang dipinjam oleh akun Anda.")

# Start Program
clear()
while True:
    pilihan_menu()
    akses = input("Masukkan pilihan menu: ")

    if akses == "1":
        print("Berhasil masuk sebagai administrator")
        while True:
            menu_admin()
            menu = input("Masukkan pilihan menu: ")

            if menu == "1":
                while True:
                    read_menu_admin()
                    read_menu = input("Masukkan pilihan menu: ")
                    if read_menu == "1":
                        read(books)
                    elif read_menu == "2":
                        read(borrowed_books)
                    elif read_menu == "3":
                        read_customer(pengunjung)
                    elif read_menu == "4":
                        filtering()
                    elif read_menu == "5":
                        clear()
                        break
                    elif read_menu == "0":
                        clear()
                        exit_menu_admin()
                        exit()
                    else:
                        print("Pilihan menu tidak tersedia")
            
            elif menu == "2":
                while True:
                    create_menu()
                    create_menu = input("Masukkan pilihan menu: ")
                    if create_menu == "1":
                        create()
                    elif create_menu == "2":
                        clear()
                        break
                    elif create_menu == "0":
                        clear()
                        exit_menu_admin()
                        exit()
                    else:
                        print("Pilihan menu tidak tersedia")

            elif menu == "3":
                while True:
                    update_menu()
                    update_menu = input("Masukkan pilihan menu: ")
                    if update_menu == "1":
                        update()
                    elif update_menu == "2":
                        clear()
                        break
                    elif update_menu == "0":
                        clear()
                        exit_menu_admin()
                        exit()
                    else:
                        print("Pilihan menu tidak tersedia")

            elif menu == "4":
                while True:
                    delete_menu()
                    delete_menu = input("Masukkan pilihan menu: ")
                    if delete_menu == "1":
                        delete()
                    elif delete_menu == "2":
                        clear()
                        break
                    elif delete_menu == "0":
                        clear()
                        exit_menu_admin()
                        exit()
                    else:
                        print("Pilihan menu tidak tersedia")

            elif menu == "5":
                clear()
                break

            elif menu == "0":
                clear()
                exit_menu_admin()
                exit()

            else:
                print("Pilihan menu tidak tersedia")

    elif akses == "2":
        print("Berhasil masuk sebagai pengunjung")
        while True:
            menu_customer()
            menu = input("Masukkan pilihan menu: ")

            if menu == "1":
                while True:
                    read_menu_customer()
                    read_menu = input("Masukkan pilihan menu: ")
                    if read_menu == "1":
                        read(books)
                    elif read_menu == "2":
                        read_borrowedcustomer()
                    elif read_menu == "3":
                        filtering()
                    elif read_menu == "4":
                        clear()
                        break
                    elif read_menu == "0":
                        clear()
                        exit_menu_customer()
                        exit()
                    else:
                        print("Pilihan menu tidak tersedia")
            
            elif menu == "2":
                while True:
                    borrowed_book_menu()
                    borrowed_menu = input("Masukkan pilihan menu: ")
                    if borrowed_menu == "1":
                        borrowed_book()
                    elif borrowed_menu == "2":
                        clear()
                        break
                    elif borrowed_menu == "0":
                        clear()
                        exit_menu_customer()
                        exit()
                    else:
                        print("Pilihan menu tidak tersedia")

            elif menu == "3":
                while True:
                    returned_book_menu()
                    returned_menu = input("Masukkan pilihan menu: ")
                    if returned_menu == "1":
                        returned_book()
                    elif returned_menu == "2":
                        clear()
                        break
                    elif returned_menu == "0":
                        clear()
                        exit_menu_customer()
                        exit()
                    else:
                        print("Pilihan menu tidak tersedia")
            
            elif menu == "4":
                clear()
                break

            elif menu == "0":
                clear()
                exit_menu_customer()
                exit()

            else:
                print("Pilihan menu tidak tersedia")