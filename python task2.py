# data collection
import random
import string

# user name 
print("hello! what is your name? "
       "\nSurname first")
myName_surname = input()
print("first name" )
myName_firstname = input()

print("enter your email ")
userEmailAddress = str(input("enter your email address: >>> "))
anAtsymbol = "@"

if anAtsymbol in userEmailAddress:
    print("You have entered a valid email address")
else:
    print("Not valid email address! - retry ")
    print("enter your email ")
    userEmailAddress = str(input("enter your email address: >>> "))
    anAtsymbol = "@"
    
# password generator
def randStr(chars = string.ascii_uppercase + string.digits, N=5):
	return ''.join(random.choice(chars) for _ in range(N))
password_gen = (myName_surname[0:2] + myName_firstname[len(myName_firstname)- 2: len(myName_firstname) - 0] + randStr(N=5))
print(password_gen)
# input password by the user

print("Is the password satisfactory? "
     "\nYes to continue and No to input your own password!")
password_Again = True
while password_Again:
 Again = str(input(""))
 if str(Again) == "no":
    print("you can now input your own password!")
    password_gen = input("password should be more than 7 characters: >> ")
    if len(password_gen) < 7 :
            print ("password length too short"
                   "\nInput new password!")
    password_gen = input("password should be more than 7 characters: >> ")
    password_Again = True
    password = True
 if str(Again) == "yes" or "Yes":
        print(" congratulations your registration has been completed!")
        password_Again = not True
        password = not True
             
        print([myName_firstname, myName_surname, userEmailAddress, password_gen])
    