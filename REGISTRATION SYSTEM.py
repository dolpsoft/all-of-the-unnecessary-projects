#----------------Start And Some İnfo----------------#
import time

print ("İNFO")
time.sleep(1)
print("-"*50)
print("In order to register to the system, you must enter your name, an e-mail address where we can reach you if necessary, and your password that you will use when logging in.")
time.sleep(3)
print("-"*50)



#-------Name/Surname Entry and Name/Surname Checking -------#
names=input ("Your Name/Surname: ")
print("-"*50)
while len(names)<5 or len(names)==0:
   
    print("Entered name/surname must be at least 5 characters. Please try again!")
    print("-"*50)
    names=input ("Your Name/Surname: ")
while " "   not in names:
    print("It must be space between the first name/surname entered. Please try again!")
    print("-"*50)
    names=input ("Your Name/Surname: ")
    print("-"*50)
    
print("Your name  and surname is verticified ☑ ")
print("-"*50)


#-------------E-Mail Entry and E-Mail Checking----------#
eMail= input("Enter Your E-Mail: ")
print("-"*50)

while len(eMail)<10 or len(eMail)==0:
    print ("Please enter a valid E-mail address! Your e-mail address must have at least 10 characters! Try again. (ex: 123@example.com): ")
    print("-"*50)
    eMail= input("Enter Your E-Mail: ")
    print("-"*50)

while "com"   not in eMail:
    print("Please enter a valid email! Try again. (ex: 123@example.com)")
    print("-"*50)
    eMail= input("Enter Your E-Mail: ")
    print("-"*50)          
            
while "."   not in eMail:
    print("Please enter a valid email! Try again.(ex: 123@example.com)")
    print("-"*50)
    ePosta= input("Enter Your E-Mail: ")
    print("-"*50)      


while "@"   not in eMail:
    print("Please enter a valid email! Try again.(ex: 123@example.com)")
    print("-"*50)
    eMail= input("Enter Your E-Mail: ")
print("Email Verified ☑")
print("-"*50)      


#----------------Password Entry and Password Checkup----------------#
password= input("Password: ")
print("-"*50)
while len(password)<8 or len(password)==0:
    print ("Lütfen geçerli bir şifre giriniz! Şifreniz en az 8 karakterli olmalı! Tekrar deneyin.")
    print("-"*50)
    password= input("Password: ")
    print("-"*50)


while " " in password:
    print("Please do not put a space in your password! Try again.")
    print("-"*50)
    password= input("Password: ")
    print("-"*50)


while "%" in password:
    print("Please do not use any foreign characters in your password. Try again.")
    print("-"*50)
    password= input("Password: ")
    print("-"*50)
   

    
while "*" in password:
    print("Please do not use any foreign characters in your password. Try again.")
    print("-"*50)
    password= input("password: ")
    print("-"*50)
print("Password Verified ☑")
print("-"*50)

#---------------------Loading Animation-------------------#
print('Registering in the system...')
time.sleep(1)
print("_̲̅_̲̅_̲̅_̲̅_̲̅) 1O%")
print("")
time.sleep(1)
print("_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 2O%")
print("")
time.sleep(1)
print("_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 3O%")
print("")
time.sleep(3)
print("[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 4O%")
print("")
time.sleep(0.5)
print("_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 5O%")
print("")
time.sleep(0.5)
print("_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 6O%")
print("")
time.sleep(0.5)
print("_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 7O%   ")
print("")
time.sleep(0.5)
print("_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 8O%")
print("")
time.sleep(0.5)
print("_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 9O%")
print("")
time.sleep(5)
print("_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅) 100%")
time.sleep(3)
print("")
print("-"*50)
print("Successfully registered to the system! ")
print("-"*50)

#-----------------------------------------------------------------------------------# 