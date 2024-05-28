from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open("D:\PRODIGY_CS_02\Python.png")
    width, height = img.size
    
    # Encrypt each pixel using a simple mathematical operation (addition)
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_pixels.append(encrypted_pixel)
    
    # Create a new image with the encrypted pixels
    encrypted_img = Image.new(img.mode, (width, height))
    encrypted_img.putdata(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(image_path)
    width, height = encrypted_img.size
    
    # Decrypt each pixel using the inverse mathematical operation (subtraction)
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_pixels.append(decrypted_pixel)
    
    # Create a new image with the decrypted pixels
    decrypted_img = Image.new(encrypted_img.mode, (width, height))
    decrypted_img.putdata(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    # Path to the image file
    image_path = "D:\PRODIGY_CS_02\Python.png"
    
    # Encryption key (can be any integer)
    key = 50
    
    # Encrypt the image
    encrypt_image(image_path, key)
    
    # Decrypt the encrypted image
    decrypt_image("encrypted_image.png", key)

if __name__ == "__main__":
    main()
