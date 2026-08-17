import string
import random

while True:
    pass_len = int(input("Enter length of password:"))
    if pass_len < 8:
        print("Error! Password must contain 8 or more digits.")
        continue
    while True:
        print("Please enter yes or no.")
        c1 = input("Do u want upper case? ").lower()
        if c1 not in ["yes", "no"]:
            print("Error! Inavlid input")
            print("Please, enter 'yes' or 'no' only.")
            continue
        c2 = input("Do u want lower case? ").lower()
        if c2 not in ["yes", "no"]:
            print("Error! Inavlid input")
            print("Please, enter 'yes' or 'no' only.")
            continue
        c3 = input("Do u want numbers? ").lower()
        if c3 not in ["yes", "no"]:
            print("Error! Inavlid input")
            print("Please, enter 'yes' or 'no' only.")
            continue
        c4 = input("Do u want symbols? ").lower()
        if c4 not in ["yes", "no"]:
            print("Error! Inavlid input")
            print("Please, enter 'yes' or 'no' only.")
            continue
        count = 0
        password_pool = ""
        if c1 == "yes":
            count += 1
            password_pool += string.ascii_uppercase
        if c2 == "yes":
            count += 1
            password_pool += string.ascii_lowercase
        if c3 == "yes":
            count += 1
            password_pool += string.digits
        if c4 == "yes":
            count += 1
            password_pool += string.punctuation
        if count < 2:
            print("Error! Choose at least 2 yes.")
            continue
        break
    password = ""
    for i in range(pass_len):
        password += random.choice(password_pool)
    print("Your Password is:", password)
    while True:
        again = input("Do you want to generate password again? ").lower()
        if again not in ["yes", "no"]:
            print("Enter 'yes' or 'no' only")
        if again == "yes" or again == "no":
            break
    if again == "no":
        print("Thank you for using password generator. GOOD BYE!")
        break

