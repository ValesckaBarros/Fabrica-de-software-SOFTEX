import cv2
import os
import numpy as np

image_folder = 'CME_18'
template_path = 'instrumento_referencia.jpg'

template = cv2.imread(template_path, 0)
template_height, template_width = template.shape[:2]

instrument_images = []

for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    img = cv2.imread(image_path, 0)

    found_instrument = False
    for scale in np.linspace(0.5, 1.5, 10):
        resized_template = cv2.resize(template, (int(template_width * scale), int(template_height * scale)))
        res = cv2.matchTemplate(img, resized_template, cv2.TM_CCOEFF_NORMED)
        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        if max_val >= 0.6:
            found_instrument = True
            
            top_left = max_loc
            bottom_right = (top_left[0] + resized_template.shape[1], top_left[1] + resized_template.shape[0])
            cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
            
            # Determinar a orientação usando o retângulo mínimo
            rect = cv2.minAreaRect(np.array([[top_left[0], top_left[1]], 
                                               [bottom_right[0], top_left[1]], 
                                               [bottom_right[0], bottom_right[1]], 
                                               [top_left[0], bottom_right[1]]], dtype=np.float32))
            angle = rect[2]

            if angle < -45:
                angle += 90

            if abs(angle) < 15:  # Horizontal
                orientation = "Horizontal"
            elif abs(angle) > 75:  # Vertical
                orientation = "Vertical"
            else:  # Inclinado
                orientation = "Inclinado"

            # Imprimir a orientação no console
            print(f"Imagem: {image_name} - Orientação: {orientation}")

            # Adicionar a orientação na imagem
            cv2.putText(img, f'Orientation: {orientation}', (top_left[0], top_left[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            break

    if found_instrument:
        instrument_images.append(image_name)

# Exibir resultados
for img_name in instrument_images:
    img_path = os.path.join(image_folder, img_name)
    img = cv2.imread(img_path)
    cv2.imshow('Detected Instrument', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
print("Imagens com instrumento:", instrument_images)
