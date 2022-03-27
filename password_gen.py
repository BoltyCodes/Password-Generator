#imports

import random



#info
print("Hey there! This PasswordGenerator has three levels: 1,2,3")
print("level 1 will give you a small password; Something used for passwords for small websites.")
print("level 2 will give you a medium password; Something used for general purpose such as spotify, discord, facebook etc.")
print("level 3 will give you a large password; Something used for E-commerce websites, google, gmail, etc.")

level = int(input("Enter your level:"))

#symbols
symbols = ["!", "@", "#", "$", "%"]

symbol = random.choice(symbols)


#Levels
def levelone():
  print("You have selected level 1")
  print("We are going to ask a few questions to generate the best password for you!")



  name = input("Enter your name:")
 # age = int(input("Enter your age"))   
 # pet = input("Enter your pet:")
  year = input("Enter your year of birth:")
  split_name= list(name)

  names = name[0:3]

  print("The password is:",name+symbol+year)
   




def leveltwo():
    print("You have selected level 2")

    name = input("Enter your name:")
    age = int(input("Enter your age:"))   
    pet = input("Enter your pet:")
    year = input("Enter your year of birth:")

    x = input(f"The password is:  {name}{symbol}{age}{symbol}{year}."   )
    print(x)



#Getting the random letters *sigh*                                                                                                                 
with open("password_generator/a.txt", "r") as file:
    read = file.read().splitlines()
    if len(read) <= 8:
      True
    word = random.choice(read)
    fixed_Word = list(word)

    first_half = word[0:3]


#Symbols 




def levelthree():
    print("You have selected level 3")

    name = input("Enter your name:")
    age = int(input("Enter your age:"))   
    pet = input("Enter your pet:")
    year = input("Enter your year of birth:")


    half_pet = pet[0:3]

    print(f"The password is:  {name}{symbol}{age}{symbol}{year}{symbol}{half_pet}{first_half}")
 





if level == 1:
    levelone()

elif level == 2:
    leveltwo()

else:
    levelthree()



