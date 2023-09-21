from cryptography.fernet import Fernet

# Generate a key for encryption (keep this key secret)
key = Fernet.generate_key()
print("Key: ", key) #b'_LREkXLq1baabFYPLNR6QkPB5SgCvi87uXJSg3ZPbbM='
cipher_data = Fernet(key)
print('cipher_data: ',cipher_data)

# Specify the path to the input and output files

input_file = 'C:/Users/oindey/Desktop/Ansible/pythonFiles/ADC2023-5888_withTwoInventoryFile/creds.txt'
output_file = 'C:/Users/oindey/Desktop/Ansible/pythonFiles/ADC2023-5888_withTwoInventoryFile/encrypted_file.txt'
# Read the content of the input file
with open(input_file, 'rb') as file:
    plaintext = file.read()

# Encrypt the content
encrypted_data = cipher_data.encrypt(plaintext)

# Write the encrypted data to the output file
with open(output_file, 'wb') as file:
    file.write(encrypted_data)

print(f'Text file encrypted and saved as {output_file}')
