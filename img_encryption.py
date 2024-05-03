from PIL import image
import numpy as np

print("--------------Image Encryption Tool--------------")

def encrypt_image(image_path,key):
    #opening the image
    original_image=image.open(image_path)

    #converting the image to a numpy array
    image_array=np.array(original_image)

    #applying a more complex mathematical operation to each pixel using the key 
    encrypted_image_array=(image_array*key)//(key+1)

    #creating a new imagefrom the encrypted numpy array
    encrypted_image=Image.fromarray(np.unit8(encrypted_image_array))

    #saving the encrypted image
    encrypted_image_path="encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f"image encrypted successfully.Encrypted image saved at :{encrypted_image_path}")
    exit()

def encrypt_image(encrypted_image_path,key):
    #opening the encrypted image
    encrypted_image=Image.open(encrypted_image_path)

    #converting the image to a numpy array
    encrypted_image_array=np.array(encrypted_image)

   #reversing the more complex encryption using the key
    decrypted_image_array=(encrypted_image_array*(key+1))//key

   #clipping values to ensure they are in the valid pixel value range
    decrypted_image_array=np.clip(decrypted_image_array,0,255)

   #creating a new image from the decrypted numpy array
    decrypted_image=Image.fromarray(np.unit8(decrypted_image_array))

   #saving the decrypted image
    decrypted_image_path="decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"Image decrypted successfully.Decrypted image saved at :{decrypted_image_path}")
    exit()

def main():
    while true:
        print("select an option:")
        print("e-Encrypt image")
        print("d-Decrypt image")
        print("q-Quit")
        choice=input("Your choice:")

        if choice=='e':
            encrypt_choice()
        elif choice=='d':
            decrypt_choice()
        elif choice=='q':
            print("Exitting the program.")
            exit()
        else:
            print("Invalid choice. please choose'e'for encryption,'d'for decryption, or 'q'to quit.")

def encrypt_choice():
    key=int(input("Enter encryption key:"))
    image_location=input("Enter the location or URL of the image: ")

    try:
        encrypt_image(image_location,key)
    except filenotfounderror:
        print("Invalid location.Image not found.please try again.")
        encrypt_choice()

def decrypt_choice():
    key=int(input("Enter decryption key:"))
    encryption_image_location=input("Enter the location of the encrypted image:")

    try:
        decrypt_image(encrypted_image_location,key)
    except FilenotFoundError:
        print("Invalid location.Encrypted image not found.please try again.")
        decrypt_choice()

