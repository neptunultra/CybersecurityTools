from PIL import Image

def encrypt_image(image_path, key):
    """
    Encrypts an image by manipulating the pixels.

    Args:
        image_path (str): Path to the image file.
        key (int): Secret key for encryption.

    Returns:
        Image: The encrypted image.
    """
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = pixels[x, y]
            encrypted_pixel = (
                pixel[0] ^ key,
                pixel[1] ^ key,
                pixel[2] ^ key
            )
            pixels[x, y] = encrypted_pixel

    return image

def decrypt_image(image_path, key):
    """
    Decrypts an image by manipulating the pixels.

    Args:
        image_path (str): Path to the image file.
        key (int): Secret key for decryption.

    Returns:
        Image: The decrypted image.
    """
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = pixels[x, y]
            decrypted_pixel = (
                pixel[0] ^ key,
                pixel[1] ^ key,
                pixel[2] ^ key
            )
            pixels[x, y] = decrypted_pixel

    return image

def main():
    image_path = "path/to/image.jpg"
    key = 123  # Secret key for encryption/decryption

    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    encrypted_image.save("encrypted_image.jpg")

    # Decrypt the image
    decrypted_image = decrypt_image("encrypted_image.jpg", key)
    decrypted_image.save("decrypted_image.jpg")

if __name__ == "__main__":
    main()