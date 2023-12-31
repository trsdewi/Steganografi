from PIL import Image

def read_RGB(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    rgb_values = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            rgb_values.append(((x, y), r, g, b))  # Menambahkan koordinat piksel ke dalam tuple
    return img, rgb_values

def adjust_cover_with_original(cover_img, cover_rgb, x, y, new_r, new_g, new_b):
    # Mengubah nilai RGB pada koordinat yang dipilih di gambar cover
    cover_pixels = cover_img.load()
    cover_pixels[x, y] = (new_r, new_g, new_b)

    # Mengubah nilai RGB pada list rgb_values agar sesuai dengan perubahan yang dilakukan pada gambar cover
    for idx, pixel in enumerate(cover_rgb):
        if pixel[0] == (x, y):
            cover_rgb[idx] = (pixel[0], new_r, new_g, new_b)
            break

    return cover_img, cover_rgb

def main():
    original_image_path = input("Masukkan path file gambar asli: ")
    cover_image_path = input("Masukkan path file gambar cover: ")

    original_img, original_rgb = read_RGB(original_image_path)
    cover_img, cover_rgb = read_RGB(cover_image_path)

    print("\nNilai RGB dari gambar asli:")
    for i, rgb in enumerate(original_rgb[:10]):
        print(f"Piksel-{i+1}: {rgb}")

    print("\nNilai RGB dari gambar cover sebelum perubahan:")
    for i, rgb in enumerate(cover_rgb[:10]):
        print(f"Piksel-{i+1}: {rgb}")

    x = int(input("Masukkan koordinat X piksel yang ingin diubah pada gambar cover: "))
    y = int(input("Masukkan koordinat Y piksel yang ingin diubah pada gambar cover: "))

    # Memilih nilai RGB dari gambar asli sesuai dengan koordinat yang dipilih
    selected_pixel = None
    for pixel in original_rgb:
        if pixel[0] == (x, y):
            selected_pixel = pixel
            break

    if selected_pixel:
        new_r, new_g, new_b = selected_pixel[1], selected_pixel[2], selected_pixel[3]

        # Menyesuaikan nilai RGB pada gambar cover berdasarkan koordinat yang dipilih dari gambar asli
        new_cover_img, new_cover_rgb = adjust_cover_with_original(cover_img, cover_rgb, x, y, new_r, new_g, new_b)

        print("\nNilai RGB dari gambar cover setelah perubahan:")
        for i, rgb in enumerate(new_cover_rgb[:10]):
            print(f"Piksel-{i+1}: {rgb}")

        new_cover_img.show()  # Tampilkan gambar cover yang telah diubah

        # Simpan citra baru dengan nilai RGB yang telah diubah
        new_cover_img.save("gambar_cover_baru.jpg")  # Ganti dengan path dan nama file yang diinginkan

    else:
        print("Koordinat piksel yang dimasukkan tidak ditemukan pada gambar asli.")

if __name__ == "__main__":
    main()

