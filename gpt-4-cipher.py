alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '=', '<', '>', ';', ':', '+', '_', '}', '{', '[', ']',
'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '/']
substitution_key = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
'9', '8', '7', '6', '5', '4', '3', '2', '1', '+', '_', '.', ',', "-", '/', '}', '{', '~', '`', 'а', 'ы',
'л', 'у', 'и', 'ф', 'о', 'к', 'д', 'т', 'б', 'е', 'з', 'м']


def encrypt(message):
    encrypted_message = ""
    for character in message.lower():
        if character in alphabet:
            index = alphabet.index(character)
            encrypted_character = substitution_key[index]
            encrypted_message += encrypted_character
        else:
            encrypted_message += character
    return encrypted_message

def decrypt(encrypted_message):
    original_message = ""
    for character in encrypted_message:
        if character in substitution_key:
            index = substitution_key.index(character)
            original_character = alphabet[index]
            original_message += original_character
        else:
            original_message += character
    return original_message

message = input("message: ")
encrypted_message = encrypt(message)
print(encrypted_message)
print("") 


# decrypte
want_dec = input("Do you want decrypt message (y/n): ")
if want_dec.lower() == 'y':
  print("")
  enc_msg = input("Enter encrypt message: ")

  decrypted_message = decrypt(enc_msg)
  print(decrypted_message)

if want_dec.lower() == 'n':
  exit()
