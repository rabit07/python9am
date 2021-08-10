import os
import getpass

if not os.path.exists('database.txt'):
    fs = open('database.txt', 'w')
    fs.close()


def register():
    print("=============Create user name==============")
    username = input("Enter User Name:")
    if username in open('database.txt', 'r').read():
        print("Username already exists")
        exit()
    password = getpass.getpass("Enter password:")
    print("password")
    confirm_password = getpass.getpass("Confirm password:")
    if password != confirm_password:
        print("Password not match:")
    exit()


register()
