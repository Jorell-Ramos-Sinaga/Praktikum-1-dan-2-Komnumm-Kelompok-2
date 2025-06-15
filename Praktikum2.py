import numpy as np

# Fungsi yang akan diintegrasikan
def f(x):
    return np.sin(x)

# Nilai eksak untuk perbandingan
def exact_integral(a, b):
    return -np.cos(b) + np.cos(a)

# Metode Trapezoidal
def trapezoidal(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return h * s

# Metode Romberg
def romberg_integration(f, a, b, max_k):
    R = [[0.0 for _ in range(max_k)] for _ in range(max_k)]
    for k in range(max_k):
        n = 2**k
        R[k][0] = trapezoidal(f, a, b, n)
    for j in range(1, max_k):
        for k in range(j, max_k):
            R[k][j] = (4**j * R[k][j-1] - R[k-1][j-1]) / (4**j - 1)
    return R

# Bandingkan hasil
a = 0
b = np.pi
n = 4  # Jumlah iterasi trapezoidal = 2^n
true_value = exact_integral(a, b)

trap_result = trapezoidal(f, a, b, n)
romberg_table = romberg_integration(f, a, b, n+1)
romberg_result = romberg_table[n][n]

print(f"Nilai eksak:        {true_value:.10f}")
print(f"Trapezoidal (n={n}):  ``                                                                                                                                                                                                                                {trap_result:.10f} \tError: {abs(true_value - trap_result):.2e}")
print(f"Romberg (iter={n}):   {romberg_result:.10f} \tError: {abs(true_value - romberg_result):.2e}")
