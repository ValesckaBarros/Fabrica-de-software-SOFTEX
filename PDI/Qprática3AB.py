import cv2
import os
import numpy as np

image_folder = 'CME_18'
template_path = 'instrumento_referencia.jpg'

template = cv2.imread(template_path, 0)
template_height, template_width = template.shape[:2]

instrument_images = []
non_instrument_images = []

threshold = 0.6

for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    img = cv2.imread(image_path, 0)
    
    found_instrument = False
    for scale in np.linspace(0.5, 1.5, 10):
        resized_template = cv2.resize(template, (int(template_width * scale), int(template_height * scale)))
        res = cv2.matchTemplate(img, resized_template, cv2.TM_CCOEFF_NORMED)
        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        if max_val >= threshold:
            found_instrument = True
            break
    
    if found_instrument:
        instrument_images.append(image_name)
    else:
        non_instrument_images.append(image_name)

print("Imagens com instrumento:", instrument_images)
print("Imagens sem instrumento:", non_instrument_images)


