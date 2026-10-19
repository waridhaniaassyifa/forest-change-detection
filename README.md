# Forest Change Detection

Proyek *machine learning* sederhana untuk mengklasifikasikan indikasi perubahan tutupan hutan berdasarkan persentase tutupan vegetasi sebelum dan sesudah pengamatan serta persentase tanah terbuka.

Proyek ini dibuat sebagai studi kasus pembelajaran berdasarkan materi **“Deforestation Alerts Using Satellite Imagery and Artificial Intelligence”** oleh Dr. Bart Slater dari Wageningen University & Research, Belanda.

## 📌 Deskripsi Studi Kasus

Perubahan tutupan hutan merupakan salah satu permasalahan lingkungan yang perlu dipantau. Berkurangnya tutupan vegetasi dan meningkatnya area tanah terbuka dapat menjadi indikasi awal perubahan kondisi suatu wilayah.

Dalam studi kasus ini, algoritma *Decision Tree* digunakan untuk mempelajari pola dari data simulasi dan mengklasifikasikan suatu lokasi ke dalam dua kategori:

- **Tidak terindikasi:** lokasi tidak diklasifikasikan sebagai indikasi perubahan tutupan hutan oleh model.
- **Indikasi perubahan:** lokasi diklasifikasikan sebagai indikasi perubahan tutupan hutan dan perlu diperiksa lebih lanjut.

Program menerima tiga masukan, yaitu persentase tutupan vegetasi sebelum pengamatan, persentase tutupan vegetasi sesudah pengamatan, dan persentase tanah terbuka saat ini.

**Catatan:** Proyek ini menggunakan data simulasi, bukan citra satelit atau data deforestasi nyata. Hasil klasifikasi hanya untuk pembelajaran dan tidak dapat dijadikan bukti deforestasi.

## 🎯 Tujuan

1. Memahami penerapan *machine learning* untuk klasifikasi sederhana.
2. Mengimplementasikan algoritma *Decision Tree* menggunakan Python.
3. Mengukur performa model menggunakan akurasi, precision, recall, dan F1-score.
4. Menunjukkan bagaimana perubahan persentase tutupan vegetasi dapat digunakan sebagai masukan dalam studi kasus pemantauan hutan.

## ⚙️ Teknologi yang Digunakan

- Python
- Scikit-learn
- Decision Tree Classifier
- Visual Studio Code

## 🗂️ Struktur Proyek

```text
forest-change-detection/
├── main.py
```

## 🚀 Cara Menjalankan Program

### 1. Persiapan

Pastikan Python telah terpasang di komputer. Periksa instalasi melalui terminal VS Code:

```bash
python --version
```

Jika perintah tersebut tidak berfungsi di Windows, coba:

```bash
py --version
```

### 2. Instalasi library

Buka terminal di VS Code, kemudian jalankan:

```bash
python -m pip install scikit-learn
```

Jika menggunakan perintah `py`, jalankan:

```bash
py -m pip install scikit-learn
```

### 3. Jalankan program

Pastikan terminal berada di folder proyek, kemudian jalankan:

```bash
python main.py
```

Atau, jika menggunakan launcher Python Windows:

```bash
py main.py
```

### 4. Masukkan data lokasi

Ketika diminta oleh program, masukkan tiga nilai persentase. Contoh:

```text
Tutupan vegetasi sebelum pengamatan (%): 90
Tutupan vegetasi sesudah pengamatan (%): 60
Persentase tanah terbuka saat ini (%): 35
```

Program kemudian menampilkan perubahan tutupan vegetasi, status klasifikasi, dan saran untuk pemeriksaan lebih lanjut.

## 🧠 Cara Kerja Program

1. **Menyiapkan data:** program menggunakan 24 data simulasi yang berisi persentase tutupan vegetasi sebelum pengamatan, tutupan vegetasi sesudah pengamatan, tanah terbuka, dan label kelas.
2. **Membagi data:** data dibagi menjadi 18 data pelatihan dan 6 data pengujian.
3. **Melatih model:** algoritma *Decision Tree Classifier* mempelajari pola dari data pelatihan.
4. **Mengevaluasi model:** performa model dihitung menggunakan akurasi, precision, recall, dan F1-score.
5. **Memeriksa lokasi baru:** pengguna memasukkan persentase kondisi vegetasi dan tanah terbuka untuk mendapatkan prediksi model.
6. **Menampilkan hasil:** program menampilkan indikasi perubahan tutupan vegetasi berdasarkan klasifikasi model.

## 📊 Hasil Pengujian

Berdasarkan salah satu hasil eksekusi program, diperoleh hasil berikut:

| Komponen | Hasil |
|---|---:|
| Jumlah data pelatihan | 18 |
| Jumlah data pengujian | 6 |
| Akurasi pengujian | 100% |
| Precision kelas Tidak terindikasi | 1,00 |
| Recall kelas Tidak terindikasi | 1,00 |
| F1-score kelas Tidak terindikasi | 1,00 |
| Precision kelas Indikasi perubahan | 1,00 |
| Recall kelas Indikasi perubahan | 1,00 |
| F1-score kelas Indikasi perubahan | 1,00 |

Nilai tersebut menunjukkan bahwa seluruh enam data pengujian pada eksekusi tersebut berhasil diklasifikasikan sesuai labelnya. Namun, hasil ini belum membuktikan bahwa model dapat mendeteksi perubahan hutan secara akurat di dunia nyata karena jumlah data terbatas dan seluruh data berasal dari simulasi.

## 🔎 Contoh Pemeriksaan Lokasi

Data yang dimasukkan:

- Tutupan vegetasi sebelum pengamatan: 90%
- Tutupan vegetasi sesudah pengamatan: 60%
- Tanah terbuka saat ini: 35%

Perubahan tutupan vegetasi dihitung sebagai berikut:

```text
90% - 60% = 30 poin persentase
```

Hasil program:

```text
Perubahan tutupan vegetasi: 30.0%
Status: INDIKASI PERUBAHAN TUTUPAN HUTAN
Saran: periksa lokasi lebih lanjut.
```

Hasil tersebut merupakan prediksi berdasarkan pola data simulasi yang dipelajari model. Nilai perubahan sebesar 30 poin persentase merupakan perhitungan selisih masukan, sedangkan status akhir ditentukan oleh model klasifikasi.

## 🌱 Hubungan dengan Materi

Materi *Deforestation Alerts Using Satellite Imagery and Artificial Intelligence* membahas pemanfaatan citra satelit dan kecerdasan buatan untuk mendukung pemantauan perubahan hutan.

Proyek ini mengadaptasi gagasan tersebut ke dalam bentuk sederhana dengan menggunakan data numerik dan algoritma *machine learning*. Proyek ini belum menerapkan pengolahan citra satelit, analisis citra dari waktu ke waktu, maupun sistem peringatan deforestasi nyata.

## ⚠️ Keterbatasan

- Dataset masih berupa data simulasi.
- Jumlah data hanya 24 sampel.
- Pengujian hanya menggunakan 6 sampel.
- Model belum diuji pada data hutan atau citra satelit yang sebenarnya.
- Hasil prediksi tidak dapat dijadikan bukti terjadinya deforestasi.

## 🔮 Pengembangan Selanjutnya

Proyek ini dapat dikembangkan dengan menggunakan data citra satelit yang tersedia secara publik, membandingkan kondisi vegetasi pada waktu yang berbeda, menambah jumlah data pengujian, serta memvalidasi prediksi dengan data lapangan.

## 👩‍💻 Tujuan Pembelajaran

Proyek ini dibuat untuk mempelajari dasar penerapan *machine learning* dalam klasifikasi indikasi perubahan tutupan hutan menggunakan Python.

**Disclaimer:** Hasil program merupakan simulasi pembelajaran, bukan alat pemantauan deforestasi yang telah tervalidasi.
