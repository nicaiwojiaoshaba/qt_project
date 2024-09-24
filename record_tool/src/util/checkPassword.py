import bcrypt


def checkPassword(password, hashedPassword):
    return bcrypt.checkpw(password.encode("utf-8"), hashedPassword.encode("utf-8"))
