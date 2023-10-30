from hashlib import sha256
from color import *

password = "test"
hashed_password = sha256(password.encode()).hexdigest()

print(f"password: {password}")
print(f"hashed password: {hashed_password}")

if (sha256(b"test").hexdigest() == hashed_password):
    print(fg.GREEN + "fonctionne!" + fg.RESET)

else:
    print(fg.RED + "mauvais hash!" + fg.RESET)
    print(fg.RED + str(sha256(b"test").hexdigest) + " ≠ " + hashed_password + fg.RESET)