import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

adunare = A + B
scadere = A - B

print("Suma:\n", adunare)
print("Diferența:\n", scadere)

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Verificarea dimensiunilor este gestionată automat de NumPy
produs = np.dot(A, B) # sau A @ B
print("Produsul matricelor:\n", produs)

import numpy as np

M = np.array([[1, 2, 3], [4, 5, 6]])
transpusa = M.T
print("Transpusa:\n", transpusa)

import numpy as np

m2x2 = np.array([[4, 3], [1, 2]])
m3x3 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

det2 = np.linalg.det(m2x2)
det3 = np.linalg.det(m3x3)

print(f"Determinant 2x2: {det2:.2f}")
print(f"Determinant 3x3: {det3:.2f}")

import numpy as np

M = np.array([[1, 2, 3], [4, 5, 6]])
este_patrata = M.shape[0] == M.shape[1]
print("Este pătrată?", este_patrata)

import numpy as np

M = np.array([[1, 0], [0, 1]])
# Creăm o matrice identitate de aceeași mărime și comparăm
identitate_teoretica = np.eye(M.shape[0])
este_id = np.array_equal(M, identitate_teoretica)

print("Este matrice identitate?", este_id)

import numpy as np

# Exemplu: 2x + 3y = 5 și 4x - y = 2
sistem = np.array([[2, 3, 5], [4, -1, 2]])
coeficienti = sistem[:, :-1] # Toate rândurile, toate coloanele minus ultima
print("Coeficienți:\n", coeficienti)

import numpy as np

import numpy as np

M = np.array([[1, 2], [3, 4]])
# k=-1 rotește în sensul acelor de ceasornic
rotita = np.rot90(M, k=-1)
print("Matrice rotită 90°:\n", rotita)

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
suma_diag = np.trace(M)
print("Suma diagonalei principale:", suma_diag)

import numpy as np

M = np.array([[1, 2], [2, 1]])
este_simetrica = np.array_equal(M, M.T)
print("Este simetrică?", este_simetrica)

import numpy as np

M = np.array([[1, 2], [0, 3]])
este_sup = np.array_equal(M, np.triu(M)) # triu = triangle upper
este_inf = np.array_equal(M, np.tril(M)) # tril = triangle lower

print("Este triunghiulară?", este_sup or este_inf)

import numpy as np

M = np.array([[4, 7], [2, 6]])
try:
    inversa = np.linalg.inv(M)
    print("Inversa:\n", inversa)
except np.linalg.LinAlgError:
    print("Matricea nu este inversabilă!")
    
    import numpy as np

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Selectăm rândurile 0-1 și coloanele 0-1
sub = M[0:2, 0:2]
print("Submatrice:\n", sub)

import numpy as np

M = np.array([[10, 20], [30, 40]])
element = 30
pozitie = np.where(M == element)
print(f"Elementul {element} se află la rândul {pozitie[0][0]} și coloana {pozitie[1][0]}")

import numpy as np

M = np.array([[1, 5], [10, 2]])
# axis=1 înseamnă operație pe orizontală (rânduri)
sume_randuri = np.sum(M, axis=1)
max_suma = np.max(sume_randuri)
print("Sumele pe rânduri:", sume_randuri)
print("Suma maximă găsită:", max_suma)

import numpy as np

M = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

# Un graf neorientat are matrice simetrică, valori de 0 și 1, și 0 pe diagonală
conditii = [
    np.array_equal(M, M.T),
    np.all(np.isin(M, [0, 1])),
    np.all(np.diag(M) == 0)
]

print("Este matrice de adiacență validă?", all(conditii))s