import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregar a imagem em escala de cinza
img = cv2.imread('Tools.bmp', cv2.IMREAD_GRAYSCALE)

# Suavização com filtro Gaussiano
img_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Aplicar limiar adaptativo para binarizar a imagem
# QUAL ALGORITIMO???????
thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY_INV, 11, 2)

# Aplicar fechamento morfológico para conectar regiões próximas
#EROSAO E DILATAÇÃO
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Detectar contornos
# 
contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtrar contornos por área mínima
min_area = 100  # Defina um valor razoável com base no tamanho das ferramentas
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

# Contar as ferramentas
num_tools = len(filtered_contours)
print(f"Número de ferramentas detectadas: {num_tools}")

# Visualizar os resultados
img_contours = cv2.drawContours(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), filtered_contours, -1, (0, 255, 0), 2)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(thresh, cmap='gray')
plt.title('Imagem Binarizada')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(img_contours)
plt.title(f'Ferramentas Detectadas: {num_tools}')
plt.axis('off')

plt.show()
