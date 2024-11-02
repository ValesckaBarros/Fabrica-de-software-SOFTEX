import numpy as np
from math import ceil

# Definindo as matrizes R, G e B
R = np.array([
    [255, 240, 200, 150, 120],
    [230, 220, 180, 160, 100],
    [210, 190, 170, 145, 90],
    [170, 160, 140, 130, 80],
    [185, 165, 155, 135, 122]
])

G = np.array([
    [255, 240, 230, 235, 210],
    [240, 245, 250, 255, 180],
    [240, 245, 250, 255, 180],
    [240, 245, 250, 255, 180],
    [255, 240, 230, 235, 210]
])

B = np.array([
    [255, 255, 200, 180, 160],
    [245, 230, 190, 140, 120],
    [245, 230, 190, 140, 120],
    [245, 230, 190, 140, 120],
    [255, 200, 180, 160, 160]
])

# Função para converter para tons de cinza pela média
def to_grayscale_average(R, G, B):
    return np.round((R + G + B) / 3).astype(int)

# Função para converter para tons de cinza com pesos
def to_grayscale_weighted(R, G, B):
    return np.round(0.299 * R + 0.587 * G + 0.114 * B).astype(int)

# Conversão para tons de cinza
gray_avg = to_grayscale_average(R, G, B)
gray_weighted = to_grayscale_weighted(R, G, B)

# Exibindo os resultados
print("Imagem em tons de cinza pela Média:")
print(gray_avg)

print("\nImagem em tons de cinza com Pesos:")
print(gray_weighted)
