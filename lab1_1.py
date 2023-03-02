pw1 = input("Введите пароль: ")
pw2 = input("Подтвердите пароль: ")
if len(pw1) <= 6:
    print("Пароль короткий!")
else:
    if pw1 != pw2:
        print("Пароли не совпадают!")
    elif (
            pw1 == pw2 and
            any(c.isdigit() for c in pw1) and
            any(c.islower() for c in pw1) and
            any(c.isupper() for c in pw1) and
            any(c in "!@#$%^&*()_+-={}[]|\:;'<>?,./" for c in pw1)
    ):
        print("Пароль принят!")
    else:
        print("Пароль не принят!")
