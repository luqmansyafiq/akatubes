import streamlit as st
import time
import random
import sys

# Set recursion limit to a higher value
sys.setrecursionlimit(3000)

# Class untuk menyimpan data produk
class Produk:
    def __init__(self, id, nama, kategori, kadar_pengawet):  # Penulisan __init__ benar
        self.id = id
        self.nama = nama
        self.kategori = kategori
        self.kadar_pengawet = kadar_pengawet

# Fungsi untuk mencetak daftar produk dalam bentuk tabel
def print_produk(produk_list):
    table_data = []
    for produk in produk_list:
        table_data.append({
            "ID": produk.id,
            "Nama": produk.nama,
            "Kategori": produk.kategori,
            "Kadar Pengawet (%)": f"{produk.kadar_pengawet * 100:.2f}%"
        })
    return table_data

# Algoritma bubble sort iteratif
def bubble_sort_descending(produk_list):
    n = len(produk_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if produk_list[j].kadar_pengawet < produk_list[j + 1].kadar_pengawet:
                produk_list[j], produk_list[j + 1] = produk_list[j + 1], produk_list[j]

# Algoritma bubble sort rekursif
def recursive_bubble_sort_descending(produk_list, n):
    if n <= 1:
        return
    for i in range(n - 1):
        if produk_list[i].kadar_pengawet < produk_list[i + 1].kadar_pengawet:
            produk_list[i], produk_list[i + 1] = produk_list[i + 1], produk_list[i]
    recursive_bubble_sort_descending(produk_list, n - 1)

# Streamlit interface
st.title("Aplikasi perbandingan waktu eksekusi antar produk dengan bubble sort")
jumlah_data = st.selectbox(
    "Pilih jumlah data yang ingin diurutkan:",
    options=[i for i in range(100, 1001, 100)]  # Kelipatan 100 dari 100 hingga 1000
)

# Membuat data produk secara acak
produk_list = [
    Produk(i + 1, f"Produk {random.choice(['A', 'B', 'C', 'D', 'E'])}-{i+1}", 
           random.choice(["Makanan", "Minuman", "Snack", "Bumbu", "Cokelat", "Permen"]),
           round(random.uniform(0.005, 0.07), 3))
    for i in range(jumlah_data)
]

# Produk sebelum diurutkan
st.subheader("Produk Sebelum Diurutkan")
produk_sebelum = print_produk(produk_list)
st.table(produk_sebelum)

# Mengukur waktu eksekusi untuk berbagai ukuran input
sizes = list(range(100, jumlah_data + 1, 100))  # Kelipatan 100
iterative_times = []
recursive_times = []

for size in sizes:
    sample_data = produk_list[:size]

    # Iterative sort
    iter_sample = sample_data[:]
    start_iter = time.perf_counter()
    bubble_sort_descending(iter_sample)
    end_iter = time.perf_counter()
    iterative_times.append(end_iter - start_iter)

    # Recursive sort
    rec_sample = sample_data[:]
    start_rec = time.perf_counter()
    recursive_bubble_sort_descending(rec_sample, len(rec_sample))
    end_rec = time.perf_counter()
    recursive_times.append(end_rec - start_rec)

# Menampilkan hasil pengurutan terakhir (untuk ukuran data penuh)
st.subheader("Produk Setelah Diurutkan (Data Terakhir)")
produk_setelah_iter = print_produk(iter_sample)
st.table(produk_setelah_iter)

# Menampilkan waktu eksekusi
st.write(f"### Waktu Eksekusi Bubble Sort Iteratif: {iterative_times[-1]:.6f} detik")
st.write(f"### Waktu Eksekusi Bubble Sort Rekursif: {recursive_times[-1]:.6f} detik")
