import numpy as np
import imageio

def extract_lsb_from_image(image_path, bit_count):
    img = imageio.v2.imread(image_path)
    height, width, _ = img.shape
    lsb_data = []
    count = 0
    for r in range(height):
        for c in range(width):
            if count >= bit_count:
                break
            pixel = img[r, c]
            lsb_data.extend([pixel[0] & 1, pixel[1] & 1, pixel[2] & 1])
            count += 3  # three bits per pixel; rgb
    return lsb_data[:bit_count]

def binary_to_int(binary_list):
    binary_str = ''.join(str(b) for b in binary_list)
    return int(binary_str, 2)

if __name__ == "__main__":
    # first, do the text
    header_bits = extract_lsb_from_image("hide_text.png", 32)#32: header here
    message_length = binary_to_int(header_bits)
    total_bits_needed = 32 + (message_length * 8)
    message_bits = extract_lsb_from_image("hide_text.png", total_bits_needed)[32:]
    message = ''.join(chr(binary_to_int(message_bits[i:i+8])) for i in range(0, len(message_bits), 8))
    with open("hide_text.txt", "w") as file:
        file.write(message)
    # then, create image
        header_bits = extract_lsb_from_image("hide_image.png", 64)#64: header here for imagw
    height = binary_to_int(header_bits[:32]) # before 32
    width = binary_to_int(header_bits[32:]) # after 32
    total_bits_needed = 64 + (height * width * 3 * 8) #*3 because of rgb again
    pixel_bits = extract_lsb_from_image("hide_image.png", total_bits_needed)[64:]
    img_array = np.zeros((height, width, 3), dtype=np.uint8)
    idx = 0
    for r in range(height):
        for c in range(width):
            for channel in range(3):
                byte = pixel_bits[idx:idx+8]
                img_array[r, c, channel] = binary_to_int(byte)
                idx += 8

    decoded_image_path = "decoded_image.png"
    imageio.imwrite(decoded_image_path, img_array)