import numpy as np
import matplotlib.pyplot as plt

# buat fungsi dari string
def buat_fungsi(expr):
    def f(x):
        return eval(expr)
    return f

# metode regula falsi
def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Fungsi tidak memenuhi syarat f(a) * f(b) < 0\n")
        return None

    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'x':<10} {'f(x)':<10}")
    for i in range(1, max_iter + 1):
        x = b - f(b) * (b - a) / (f(b) - f(a))
        fx = f(x)
        print(f"{i:<5} {a:<10.6f} {b:<10.6f} {x:<10.6f} {fx:<10.6f}")
        
        if abs(fx) < tol:
            print(f"\nAkar ditemukan: x = {x:.6f} dalam {i} iterasi\n")
            return x

        if f(a) * fx < 0:
            b = x
        else:
            a = x

    print("\nMetode tidak konvergen setelah iterasi maksimum.\n")
    return None

# grafik fungsi
def plot_function(f, a, b, root=None):
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)

    plt.figure(figsize=(8, 5))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.plot(x, y, label='f(x)', color='blue')
    if root is not None:
        plt.plot(root, f(root), 'ro', label=f"Akar ~ {root:.6f}")
    plt.title("Grafik Fungsi f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

while True:
    print("Ketik 'exit' untuk keluar.")
    expr = input("Masukkan fungsi f(x): ")
    if expr.lower() == 'exit':
        break

    try:
        a = float(input("Batas bawah a: "))
        b = float(input("Batas atas b: "))
        f = buat_fungsi(expr)
        akar = regula_falsi(f, a, b)
        if akar is not None:
            plot_function(f, a, b, akar)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}\n")
