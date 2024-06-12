from PIL import Image
import numpy as np

def detect_LSB_steganography(img_path, original_img_path):
    # Load gambar yang dicurigai dan gambar asli
    img = Image.open(img_path)
    original_img = Image.open(original_img_path)

    # Konversi gambar ke array numpy
    img_array = np.array(img)
    original_img_array = np.array(original_img)

    # Bandingkan histogram dari kedua gambar
    img_hist = np.histogram(img_array, bins=256, range=(0, 256))[0]
    original_img_hist = np.histogram(original_img_array, bins=256, range=(0, 256))[0]

    # Hitung perbedaan histogram
    hist_diff = np.sum(np.abs(img_hist - original_img_hist))

    # Hitung MSE (Mean Squared Error)
    mse = np.mean((img_array - original_img_array) ** 2)

    # Output hasil deteksi
    print(f"Perbedaan histogram: {hist_diff}")
    print(f"MSE: {mse}")

    # Ambil bagian tersembunyi dari gambar
    hidden_data = extract_hidden_data(img_array, original_img_array)

    if hidden_data:
        print(f"Pesan tersembunyi yang terdeteksi: {hidden_data}")
    else:
        print("Tidak ada pesan tersembunyi yang terdeteksi.")

def extract_hidden_data(img_array, original_img_array):
    hidden_data = ""
    for row, original_row in zip(img_array, original_img_array):
        for pixel, original_pixel in zip(row, original_row):
            for i in range(3):  # loop through RGB channels
                # extract hidden data from LSB
                hidden_data += str(pixel[i] & 1)
                # check for terminator null byte
                if len(hidden_data) % 8 == 0 and hidden_data[-8:] == '00000000':
                    hidden_data = hidden_data[:-8]  # remove terminator
                    return ''.join(chr(int(hidden_data[i:i+8], 2)) for i in range(0, len(hidden_data), 8))
    return None

# Contoh penggunaan
if __name__ == "__main__":
    img_path = 'image_with_message.png'  # Ganti dengan path gambar yang dicurigai
    original_img_path = 'Bunga_Mawar.jpg'  # Ganti dengan path gambar asli

    detect_LSB_steganography(img_path, original_img_path)
