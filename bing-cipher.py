import random
from colorama import init, Fore, Style

# Initialize the colorama module
init()

# A function to encrypt a message
def encrypt(message):
  key = random.randint(1, 25)
  ciphertext = ""

  for char in message:
    if char.isalpha():
      code = ord(char)

      if code >= 65 and code <= 90:
        code = (code - 65 + key) % 26 + 65
      elif code >= 97 and code <= 122:
        code = (code - 97 + key) % 26 + 97

      char = chr(code)
    ciphertext += char
  return ciphertext, key

# A function to decrypt a message
def decrypt(ciphertext, key):
  plaintext = ""
  for char in ciphertext:
    if char.isalpha():
      code = ord(char)
      if code >= 65 and code <= 90:
        code = (code - 65 - key) % 26 + 65
      elif code >= 97 and code <= 122:
        code = (code - 97 - key) % 26 + 97

      char = chr(code)
    plaintext += char
  return plaintext

# encrypte 
message = input("message: ")

ciphertext, key = encrypt(message)
print(Fore.YELLOW + "Cipher:", ciphertext, "|||  key:", key)

print("")

# decrypte
want_dec = input(Fore.BLUE + "Do you want decrypt message (y/n): ")
if want_dec.lower() == 'y':
  print("")
  enc_msg = input(Style.RESET_ALL + "Enter encrypt message: ")
  enc_key = int(input(Style.RESET_ALL + "Enter encrypt key: "))

  plaintext = decrypt(enc_msg, enc_key)
  print(Fore.BLUE + "\nThe decrypted message is:", plaintext)


if want_dec.lower() == 'n':
  exit()




