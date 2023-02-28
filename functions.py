def validate_user_name():
    user_name = input("Enter your name: ")
    attempts = 0
    while attempts < 3:
        if len(user_name) > 10 and not user_name.isalpha():
            print("Username's cannot be longer than 10 chars,  contain any numbers or spaces.\n")
            user_name = input("Enter your name: ")
        elif len(user_name) > 10:
            print("Username's can not be longer than 10 characters.\n")
            user_name = input("Enter your name: ")
        elif not user_name.isalpha():
            print("Username's cannot contain any numbers or space.\n")
            user_name = input("Enter your name: ")
        else:
            return user_name

        attempts += 1
    print("You have exceeded the maximum number of attempts.")
    exit()


