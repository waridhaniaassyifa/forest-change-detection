
# Forest Change Detection
# Studi kasus: Deforestation Alerts Using Satellite Imagery and AI
# Catatan: seluruh data di bawah adalah data simulasi.

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Fitur:
# 1. Persentase tutupan vegetasi sebelum pengamatan
# 2. Persentase tutupan vegetasi sesudah pengamatan
# 3. Persentase tanah terbuka sesudah pengamatan
#
# Label:
# 0 = Tidak terindikasi perubahan signifikan
# 1 = Indikasi perubahan tutupan hutan

data = [
    [90, 88, 5, 0],
    [85, 82, 8, 0],
    [80, 78, 10, 0],
    [95, 91, 4, 0],
    [75, 72, 12, 0],
    [88, 85, 7, 0],
    [70, 68, 15, 0],
    [92, 89, 6, 0],
    [83, 80, 9, 0],
    [78, 75, 11, 0],
    [87, 84, 8, 0],
    [72, 70, 14, 0],

    [90, 60, 35, 1],
    [85, 55, 40, 1],
    [80, 50, 45, 1],
    [95, 65, 30, 1],
    [75, 50, 38, 1],
    [88, 62, 32, 1],
    [70, 45, 50, 1],
    [92, 60, 37, 1],
    [83, 58, 34, 1],
    [78, 52, 42, 1],
    [87, 60, 36, 1],
    [72, 48, 46, 1],
]

# Memisahkan fitur dan label
X = [row[:3] for row in data]
y = [row[3] for row in data]

# Membagi data untuk pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Membuat dan melatih model Machine Learning
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
model.fit(X_train, y_train)

# Menguji performa model
prediksi_test = model.predict(X_test)
akurasi = accuracy_score(y_test, prediksi_test)

print("=" * 45)
print("SISTEM DETEKSI PERUBAHAN TUTUPAN HUTAN")
print("=" * 45)
print(f"Jumlah data pelatihan : {len(X_train)}")
print(f"Jumlah data pengujian : {len(X_test)}")
print(f"Akurasi pengujian     : {akurasi:.2%}")

print("\nLaporan evaluasi model:")
print(classification_report(
    y_test,
    prediksi_test,
    labels=[0, 1],
    target_names=[
        "Tidak terindikasi",
        "Indikasi perubahan"
    ],
    zero_division=0
))

# Meminta data lokasi baru dari pengguna
print("\n--- Pemeriksaan Lokasi Baru ---")

try:
    sebelum = float(input(
        "Tutupan vegetasi sebelum pengamatan (%): "
    ))
    sesudah = float(input(
        "Tutupan vegetasi sesudah pengamatan (%): "
    ))
    tanah_terbuka = float(input(
        "Persentase tanah terbuka saat ini (%): "
    ))

    nilai = [sebelum, sesudah, tanah_terbuka]

    if not all(0 <= x <= 100 for x in nilai):
        print("Error: semua nilai harus antara 0 dan 100.")
    else:
        hasil = model.predict([nilai])[0]
        perubahan = sebelum - sesudah

        print("\nHasil Pemeriksaan")
        print(f"Perubahan tutupan vegetasi: {perubahan:.1f}%")

        if hasil == 1:
            print("Status: INDIKASI PERUBAHAN TUTUPAN HUTAN")
            print("Saran: periksa lokasi lebih lanjut.")
        else:
            print("Status: TIDAK TERINDIKASI PERUBAHAN SIGNIFIKAN")
            print("Saran: lanjutkan pemantauan berkala.")

        print(
            "\nCatatan: hasil berasal dari model data simulasi, "
            "bukan bukti deforestasi nyata."
        )

except ValueError:
    print("Input tidak valid. Masukkan angka antara 0 dan 100.")
