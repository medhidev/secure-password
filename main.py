# Import Other Code
from hashlib import sha256

banner = '''
  ____                             ____                                     _ 
 / ___|  ___  ___ _   _ _ __ ___  |  _ \ __ _ ___ _____      _____  _ __ __| |
 \___ \ / _ \/ __| | | | '__/ _ \ | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
  ___) |  __/ (__| |_| | | |  __/ |  __/ (_| \__ \__ \  V  V / (_) | | | (_| |
 |____/ \___|\___|\__,_|_|  \___| |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|                                                                              
'''
print(fg.BLUE + banner + fg.RESET)

# Interface
# coming soon ... with buble_charm package

no_validate = True
while (no_validate):
    user_account = input("name account: ")
    master_password = input("master password: ")

    # Password Security
    if(len(master_password) >= 8):
        no_validate = False
        hashed_master_password = sha256(master_password.encode()).hexdigest()
        print(fg.GREEN + f"[+] {master_password} added with succed! " + fg.RESET)

        # Write File
        file = open("passwd/password.txt", "w")
        file.write(hashed_master_password)

    else:
        print(fg.RED + f"ERROR : password '{master_password}' " + fg.RESET)
        print(fg.YELLOW + "[→] 8 chars min \n[→] not emoji or other char not in ASCII Table" + fg.RESET)

no_connect = True
while (no_connect):
    password = input("connect to secure password: ")
    if(sha256(password.encode()) == hashed_master_password):
        no_connect = False
        print(fg.GREEN + "welcome user: " + fg.RESET)
    else:
        print(fg.RED + "Wrong master password" + fg.RESET)