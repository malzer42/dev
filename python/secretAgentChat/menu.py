from generate_one_time_pad import generate_otp
from load_file import load_file, save_file
from get_plaintext import get_plaintext
from encrypt import encrypt

def menu():
    try:
        print("\nSECRET AGENT CHAT")
        choices = ['1', '2', '3', '4']
        choice = '0'
        while True:
            while choice not in choices:
                print('What would you like to do?')
                print('1. Generate one-time pads')
                print('2. Encrypt a message')
                print('3. Decrypt a message')
                print('4. Quit the program')
                choice = input('Please type 1, 2, 3 or 4 and press Enter ')
                if choice == '1':
                    sheets = int(input('How many one-time pads would you like to generate? '))
                    length = int(input('What will be your maximum message length? '))
                    generate_otp(sheets, length)
                elif choice == '2':
                    filename = input('Type in the filename of the OTP you want to use ')
                    sheet = load_file(filename)
                    encrypt(sheet)
                    #filename = input('What will be the name of the encrypted file? ')
                elif choice == '3':
                    filename = input('Type in the filename of the OTP you want to use ')
                    sheet = load_file(filename)
                    filename = input('Type in the name of the file to be decrypted ')
                    ciphertext = load_file(filename)
                    plaintext = decrypt(ciphertext, sheet)
                    print('The message reads:')
                    print('')
                    print(plaintext)
                elif choice == '4':
                    exit()
                choice = '0'
    except FileNotFoundError as file_not_found_error:
        print(file_no_found_error)
    else:
        print('')
    finally:
        print('')
                
