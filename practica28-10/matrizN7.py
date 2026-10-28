import numpy as np # type: ignore


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# SUMA DE ELEMENTOS
suma = A + B
print("---Suma A+B---")
print(suma)

# MULTIPLICACIÓN DE ELEMENTOS
prod_elem = A * B
print("---Multiplicacion A*B---")
print(prod_elem)

# TRANSPUESTA
transpuesta = A.T
print("---TRANSPUESTA DE A---")
print(transpuesta)

# DETERMINANTE E INVERSA
det = np.linalg.det(A)
inv = np.linalg.inv(A)  # Se usa np.linalg.inv para la inversa

print("Determinante A")
print(det)
print("Inversa de A")
print(inv)