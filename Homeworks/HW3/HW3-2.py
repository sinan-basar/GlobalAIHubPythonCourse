# Day3 - HomeWorks 2/2

user_info = {
    "username":"allkill",
    "password":"light.night"
    }

print(
    "#####Please, enter username and password!#####"
    )

in_username = input("Enter username:")
in_password = input("Enter password:")

if in_username == user_info.get("username") and in_password == user_info.get("password"):
    print("Username and password are true. Login is succuessful...")
else:
    print("Username/password or both are wrong.")
