# Day3 - HomeWorks 1/2

username = "allkill"
password = "light.night"

print(
    "#####Please, enter username and password!#####"
    )

in_username = input("Enter username:")
in_password = input("Enter password:")

if in_username == username and in_password == password:
    print("Username and password are true. Login is succuessful...")
else:
    print("Username/password or both are wrong.")
