from cryptography.fernet import Fernet

'''
pwd = input("Your password. ")

def write():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
            user, passw = data.split(" ")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input("You new password: ")
    with open('password.txt', 'a') as f:
        f.write(name + " " + fer.encrypt(pwd.encode()).decode() + "\n")  


while True:
    mode = input(
    "Add password or View password.(view, add), press q to quit ").lower()

if mode == "q":
   quit()

if mode == 'view':
    view()
elif mode == 'add':
    add()
    
else:
    print("Invalid mode")
    


'''
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue






commetn

if mode == "q"
    quit()
'''
