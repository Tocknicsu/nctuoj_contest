import config
import hashlib

def HashPassword(x):
    hpwd = hashlib.sha512(str(x).encode()).hexdigest() + config.TORNADO_SETTING['password_salt']
    hpwd = hashlib.md5(str(hpwd).encode()).hexdigest()
    return str(hpwd)

if __name__ == "__main__":
    print(HashPassword("admin"))
