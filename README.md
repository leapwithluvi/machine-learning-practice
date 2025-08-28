# Machine Learning Practice

Kumpulan latihan dan eksperimen Machine Learning menggunakan Python dan Jupyter Notebook.   Semua project disusun berdasarkan jenis algoritma, dimulai dari regresi sederhana hingga model yang lebih kompleks.

---

## Struktur Folder
- `linear_regression/`
  - `simple/`
    - `datasets/` : dataset untuk regresi linear sederhana
    - `.ipynb` : notebook latihan
    - `.py` : script Python versi standalone
  - `multiple/`
    - `datasets/` : dataset untuk regresi linear berganda
    - `.ipynb`
    - `.py`
  - `polynomial/`
    - `datasets/` : dataset untuk regresi polinomial
    - `.ipynb`
    - `.py`

> Setiap folder algoritma memiliki dataset sendiri agar lebih rapi dan mudah dikelola.

---

## Cara Menggunakan

### 1. Clone Repository
```bash
git clone https://github.com/leapwithluvi/machine-learning-practice.git
```
### 2. Gunakan di Google Colab
Buka Google Colab.
Pilih File → Open Notebook → Upload dan unggah file .ipynb dari folder project.
Jalankan setiap cell untuk melihat hasil latihan.
### 3. Jalankan secara Lokal (Opsional)
1. Masuk ke folder project:
```bash
cd machine-learning-practice
```
2. Jalankan Jupyter Notebook:
```bash
jupyter notebook
```
3. Buka notebook yang diinginkan dan jalankan cell.

## Catatan
- Semua dataset yang digunakan hanya untuk pembelajaran.
- File tersedia dalam format .ipynb (Jupyter Notebook) dan .py (Python script).
- Pastikan memiliki Python 3.x dan package berikut jika ingin menjalankan lokal:

```bash
pip install numpy pandas matplotlib
```

## Tujuan
- Membantu memahami algoritma Machine Learning dari dasar.
- Latihan implementasi manual (scratch) dan menggunakan library.
- Membiasakan diri dengan workflow analisis data di Python dan Jupyter Notebook.