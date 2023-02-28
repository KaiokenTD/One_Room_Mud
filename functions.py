def validate_user_name():
    user_name = input("Enter your name: ")
    attempts = 0
    while attempts < 3:
        if len(user_name) > 10 and not user_name.isalpha():
            print("Username cannot be longer than 10 chars or contain any numbers.")
            user_name = input("Enter your name: ")
        elif len(user_name) > 10:
            print("User name can not be longer than 10 characters.")
            user_name = input("Enter your name: ")
        elif not user_name.isalpha():
            print("User name cannot contain any numbers.")
            user_name = input("Enter your name: ")
        else:
            return user_name

        attempts += 1
    print("You have exceeded the maximum number of attempts.")
    exit()
