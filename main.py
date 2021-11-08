from string import printable
import random
import pyperclip
import os

digit = printable.strip()
passw = []
length = input("Password Length: ")


def passwords(Length):
    if length == '':
        print("No password is 0 words silly!")
        exit()
    elif length.replace(' ', '').isalpha():
        print("type a number")
        exit()
    else:
        for _ in range(int(length)):
            passw.append(random.choice(digit))
    word = ''.join(passw)
    name = input("Input a name for your password!")
    with open(f"{name}.txt", 'w') as f:
        f.write(f'{name}: {word}  #' + os.linesep)
        f.close()
    clip = input("Would you like to copy your password to your clipboard? (y or n)")
    if clip == "y":
        pyperclip.copy(word)
        print("Password has been copied to clipboard and is ready to use!")
    if clip == "n":
        print(f"Here is  your password!\n {word}")


passwords(length)
