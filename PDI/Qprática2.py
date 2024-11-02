import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('alumgrns.bmp')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
smooth_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
edges = cv2.Canny(smooth_img, 80, 180)
_, binary_img = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
closed_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)
contours, _ = cv2.findContours(closed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
num_textures = len(contours)
print(f"Número de regiões de diferentes texturas detectadas: {num_textures}")

output_img = img.copy()
cv2.drawContours(output_img, contours, -1, (0, 255, 0), 2)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
plt.title('Regiões de Textura Detectadas')
plt.axis('off')

plt.show()
