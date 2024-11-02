import cv2
import os

image_folder = 'CME_18'

blurred_images = []
sharp_images = []

laplacian_threshold = 30

for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
        laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
        
        if laplacian_var < laplacian_threshold:
            blurred_images.append(image_name)
        else:
            sharp_images.append(image_name)
    else:
        print(f"Imagem não carregada: {image_name}")

print("Imagens borradas:", blurred_images)
print("Imagens nítidas:", sharp_images)
