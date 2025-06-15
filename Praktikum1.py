import numpy as np
import matplotlib.pyplot as plt

# Definisikan fungsi f(x) yang ingin dicari akarnya
def f(x):
    return x**3 - x - 2  # Contoh fungsi, kamu bisa ubah sesuai kebutuhan

# Fungsi Regula Falsi
def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Fungsi tidak memenuhi syarat f(a) * f(b) < 0")
        return None

    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'x':<10} {'f(x)':<10}")
    for i in range(1, max_iter + 1):
        # Hitung titik baru menggunakan Regula Falsi
        x = b - f(b) * (b - a) / (f(b) - f(a))
        fx = f(x)

        print(f"{i:<5} {a:<10.6f} {b:<10.6f} {x:<10.6f} {fx:<10.6f}")

        if abs(fx) < tol:
            print(f"\nAkar ditemukan: x = {x:.6f} dalam {i} iterasi")
            return x
        
        # Perbarui interval
        if f(a) * fx < 0:
            b = x
        else:
            a = x

    print("\nMetode tidak konvergen setelah iterasi maksimum.")
    return None

# Fungsi untuk menampilkan grafik
def plot_function(f, a, b, root=None):
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)

    plt.figure(figsize=(8,5))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.plot(x, y, label='f(x)', color='blue')
    if root:
        plt.plot(root, f(root), 'ro', label=f"Akar ~ {root:.6f}")
    plt.title("Grafik Fungsi f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Contoh penggunaan
a = 1
b = 2
akar = regula_falsi(f, a, b)
if akar:
    plot_function(f, a, b, akar)
