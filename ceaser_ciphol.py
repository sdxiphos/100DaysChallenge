alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plane_text,shift_amount):
    encrypt_text=''
    for item in text:
        if item in alphabet:  
                encrypt_text += alphabet[(alphabet.index(item)+shift)%len(alphabet)]
    return encrypt_text

def decrypt(plane_text,shift_amount):
    decrypt_text=''
    for item in text:
        if item in alphabet:
            decrypt_text += alphabet[alphabet.index(item)-shift]
    return decrypt_text


if direction=='encode':

    print(f'Your encrypted letter: {encrypt(plane_text=text,shift_amount=shift)}')
elif direction=='decode':
    print(f'Your decrypted letter: {decrypt(plane_text=text,shift_amount=shift)}')
else:
    print('You entered wrong type! Try again! \n')
    pass
