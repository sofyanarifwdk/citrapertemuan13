from PIL import Image
import numpy as np
from utils import binary_to_text

def extract_message(img_path):
    img = Image.open(img_path)
    img_array = np.array(img)

    binary_message = ""
    for row in img_array:
        for pixel in row:
            for i in range(3):  # RGB channels
                binary_message += str(pixel[i] & 1)
                if len(binary_message) % 8 == 0 and binary_message[-8:] == '00000000':
                    message = binary_to_text(binary_message[:-8])  # Hilangkan terminator
                    return message

    return binary_to_text(binary_message)

# Contoh penggunaan
if __name__ == "__name__":
    img_path = 'image_with_message.png'  # Ganti dengan path gambar yang berisi pesan
    extracted_message = extract_message(img_path)
    print(f"Pesan yang diekstraksi: {extracted_message}")
