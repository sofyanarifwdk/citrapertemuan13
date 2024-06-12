from PIL import Image
import numpy as np
from utils import text_to_binary

def embed_message(img_path, message, output_path):
    img = Image.open(img_path)
    img_array = np.array(img)

    message_binary = text_to_binary(message) + '00000000'  # Tambahkan terminator null byte
    message_length = len(message_binary)
    index = 0

    for row in img_array:
        for pixel in row:
            for i in range(3):  # RGB channels
                if index < message_length:
                    pixel[i] = (pixel[i] & ~1) | int(message_binary[index])
                    index += 1
                else:
                    break

    img_with_message = Image.fromarray(img_array)
    img_with_message.save(output_path)
    print(f"Pesan telah disisipkan ke dalam {output_path}")

# Contoh penggunaan
if __name__ == "__main__":
    original_img_path = 'Bunga_Mawar.jpg'  # Ganti dengan path gambar asli Anda
    modified_img_path = 'image_with_message.png'
    message = 'BARU BELAJAR NIH >>>'

    embed_message(original_img_path, message, modified_img_path)
