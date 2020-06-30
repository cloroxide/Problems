

print("Do you want to sign up?")
sign = str(input())
def q1():
    if sign.lower()=="no":
        print("Okay, have a nice day!")
        exit()
    if sign.lower()=="yes":
        print("Please Enter Your Username and Password")
        user = str(input("Username:"))
        if user.lower() == "":
            print("You can't put a blank username!")
            q1()
        pword = input("Password:")
        if pword.lower() == "":
            print("You can't put a blank password!")
        print("Account Created.\nDo you want to sign in?")
        sign2 = str(input())
        if sign2.lower() == "no":
            print("Okay, have a nice day!")
        if  sign2.lower() == "yes":
            print("\n "*999)
            while True:
                print("Please Enter Username and Password")
                user1 = str(input("Username:"))
                pword1 = input("Password:")
                if user1.strip("") == user.strip("","") and pword.strip("") == pword1.strip(""):
                    print("You have logged in!")
                    exit()
                if user1.strip() != user.strip():
                    print("Wrong Username")
                if pword.strip() != pword1.strip():
                    print("Wrong Password")
        else:
             print("Please enter Yes or No")
    else:
           print("Please enter Yes or No")
           q1()

while True:
    q1()
