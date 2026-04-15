import string
import random
import time
def genpass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def main():
    user = input("password length: ")
    password_length = int(user)
    result = genpass(password_length)
    result2 = result.strip()
    print(f"password is: {result2}")
    time.sleep(5)
def loopfinal
    while True:
        main()
        last = input("redo? [N/y]: ")
        if last == "N":
            break
loopfinal()
