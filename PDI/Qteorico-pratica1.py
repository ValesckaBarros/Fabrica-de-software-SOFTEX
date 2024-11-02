import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregar a imagem em escala de cinza
img = cv2.imread('cameraman.bmp', cv2.IMREAD_GRAYSCALE)

# Definir os filtros h1 e h2
h1 = np.array([[1, 1, 1]]) / 3  # Filtro horizontal
h2 = np.array([[1], [1], [1]]) / 3  # Filtro vertical

# Aplicar os filtros de forma sequencial
img_h1 = cv2.filter2D(img, -1, h1)  # Primeiro filtro h1
img_sequencial = cv2.filter2D(img_h1, -1, h2)  # Depois aplicar o filtro h2

# Aplicar o filtro combinado (h1 * h2)
h_combined = cv2.filter2D(h1, -1, h2)  # Criação do filtro combinado 3x3
img_combined = cv2.filter2D(img, -1, h_combined)  # Aplicação do filtro combinado

# Mostrar as imagens
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(img_sequencial, cmap='gray')
plt.title('Aplicação Sequencial (h1 -> h2)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(img_combined, cmap='gray')
plt.title('Aplicação do Filtro Combinado')
plt.axis('off')

plt.show()
