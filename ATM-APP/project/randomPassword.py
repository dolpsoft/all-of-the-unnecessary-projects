# Please don't use random passwords generated by this code. The responsibility completely belong to you.
# I used my 'Random Password Generator' project while I'm making this 'module'. This file only a state module of 'Random Password Generator' project.

from random import choice

class RandPass: 
     def __init__(self):
          self.numbers= [0,1,2,3,4,5,6,7,8,9]
          self.letters= ["A","B", "C", "D" , "E", "F", "G" ,"H",  "İ" , "J",  "K", "L" ,  "M", "N" , "O" , "P"  ,"R", "S", "T", "U", "V", "W", "X", "Y",  "Z"   ]
          self.sLetters= ["a", "b", "c", "d", "e" , "f", "g","h", "i", "j","k", "l",	"m", "n",	"o" , "p", "r","s","t","u","v", "w",  "x", "y" , "z"]
          self.foreignChracters= [ "@", "#","!","_"]


     def random_password(self):
           ranN= choice(self.numbers)
           ranN2= choice(self.numbers)
           ranN3= choice(self.numbers)
           ranN4= choice(self.numbers)


           ranL= choice(self.letters)
           ranL2= choice(self.letters)
           ranL3= choice(self.letters)
           ranL4= choice(self.letters)


           ransL= choice(self.sLetters)
           ransL2= choice(self.sLetters)
           ransL3= choice(self.sLetters)
           ransL4= choice(self.sLetters)
    
           ranFC= choice(self.foreignChracters)
           ranFC2= choice(self.foreignChracters)
           ranFC3= choice(self.foreignChracters)
           ranFC4= choice(self.foreignChracters)
           
           print(str(ranN2)+str(ranN3)+ ransL+ ranFC+ ransL2 + ransL2+ ranFC2+ranFC3+ransL3+str(ranN)+ ranL2 +ranL3+str(ranN4)+ransL4+ranL4 )

           return str(ranN2)+str(ranN3)+ ransL+ ranFC+ ransL2 + ransL2+ ranFC2+ranFC3+ransL3+str(ranN)+ ranL2 +ranL3+str(ranN4)+ransL4+ranL4 



