import tkinter as tk

try:
        def show():
            print("Data pengeluaran makan dan minum Anda: Rp. %s\nData pengeluaran transportasi Anda: Rp. %s\nData pengeluaran edukasi Anda: Rp. %s\nData pengeluaran kesehatan Anda: Rp. %s\nData pengeluaran belanja Anda: Rp.%s" % (makanminum.get(),transportasi.get(), edukasi.get(),kesehatan.get(), belanja.get()))

except ValueError: 
    print("Program Ini Hanya Menerima Jenis Nilai Integer!")
    
finally:
    print("TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI!")

def total():
    y=sum(semua)
    print("jumlah pendapatan penjualan cilok adalah Rp"+int(y))

main_window = tk.Tk()
#labels
tk.Label(main_window, text="Pencatatan Keuangan", font=('Ailerons', 15, 'bold'), justify='center').grid(row=0, column=0)
tk.Label(main_window, text="Pilih kategori pengeluaran:", font=('Ailerons', 14, 'bold'), justify='center').grid(row=1, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran makan & minum : ").grid(row=2, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran transportasi : ").grid(row=3, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran edukasi : ").grid(row=4, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran kesehatan : ").grid(row=5, column=0)
tk.Label(main_window, text="Masukkan data pengeluaran belanja : ").grid(row=6, column=0)
tk.Label()

makanminum = tk.Entry(main_window)
transportasi = tk.Entry(main_window)
edukasi = tk.Entry(main_window)
kesehatan = tk.Entry(main_window)
belanja = tk.Entry(main_window)
semua = [makanminum,transportasi,edukasi,kesehatan,belanja]


#text input
makanminum.grid(row=2, column=1)
transportasi.grid(row=3, column=1)
edukasi.grid(row=4, column=1)
kesehatan.grid(row=5, column=1)
belanja.grid(row=6, column=1)


tk.Button(main_window, text="Click Me", command= show).grid(row=7, column=1)
tk.Button(main_window, text="Total", command= total).grid(row=7, column=2)

main_window.mainloop()
