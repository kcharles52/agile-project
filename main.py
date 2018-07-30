import sys
# from .user import login,logout
# from .comment import make_comment

print("Welcome to the comments app.")
while True:
    print()
    print()
    print("Press 's' to signup")
    print("Press 'l' to login")
    print("Press 'x' to exit")
    print()

    result = input("Enter your choice: ")

    if str(result).lower()=='l':
        pass

    elif str(result).lower()=='s':
        pass

    elif str(result).lower()=='x':
        sys.exit()


    else:
        print()
        print("You made an invalid selection.")
        print()
        print()
        continue
