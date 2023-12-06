# chapter test mode. disable the play mode and use this to test# 
"""
import random
import os
from intro_pkg.config import tpp, ti
from intro_pkg.setting import Cute

pet_name = "noir"
pet_speciman = "dog"
pet_stamina = 7
pet_inventory = ["Silver_Vine_Stick","Safety_Hat"]
"""

from intro_pkg.setting import Cute
from stage_2_pkg.stage_2_0 import pet_name, pet_speciman, pet_stamina, pet_inventory
import os
from intro_pkg.config import tpp, ti

friend = Cute(pet_name,pet_speciman, pet_stamina)                                        # to import variables from file to file 

#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                                     # testing

#Stamina balance check 
#if stamina <= 0 : Game Over 
while True:
    if friend.stamina <= 0:
        ti("Will you restart?")
        sad_1_2 = input ("Yes or No? ")
        if sad_1_2.casefold() == "yes":
             os.system('play.py')
            
        elif sad_1_2.casefold() == "no":
            print("Good Bye") 
            exit()
        else:
            print("Invalid Entry")
            continue
    else:
        print("")
        break


print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")

ti("...\n")
ti("...\n")
ti("...\n")
ti("...\n")
ti("...\n")
ti("...\n")


ti(f"{friend.name} kept walking into the cave.\n")

ti("...\n")
ti("...\n")
ti("...\n")

ti(f"A few moment later, {friend.name} heard some chirpping sounds\n\n")

print("""
    =/\                 /\=
    / \`._   (\_/)   _.'/ \       (_                   _)
   / .''._'--(o.o)--'_.''. \       /\                 /\`
  /.' _/ |`'=/ " \='`| \_ `.\     / \`._   (\_/)   _.'/ \`
 /` .' `\;-,'\___/',-;/` '. '\   /_.''._'--('.')--'_.''._\`
/.-'       `\(-V-)/`       `-.\  | \_ / `;=/ " \=;` \ _/ |
             "   "               \/  `\__|`\___/`|__/`  \/
                                  `       \(/|\)/       `
                                           " ` "
      
      
      """)

ti(f"\nIt's a group of bats!\n")

# Has Safety_Hat 
if "Safety_Hat" in pet_inventory: 
    ti(f"Fortunately, {friend.name} has a saftey hat. {friend.name} wore the hat and passed through the hallway\n")

# Doesn't have Safety_Hat 
else: 
    ti(f"Unfortunately, {friend.name} has nothing to protect from him/her from bats. {friend.name} passed through the hallway\n")
    ti("...\n")
    ti("...\n")
    ti("...\n")
    ti(f"{friend.name} felt something wet on its head....\n")
    ti("OMG...! It's a poop!\n")
    friend.stamina-=2
    ti(f"{friend.name} got stressed out with the stench of bat poop and lost (2) stamina points")


ti("...\n")
ti("...\n")
ti("...\n")

ti(f"({friend.name}~~~~)\n")

ti(f"You and {friend.name} heard the voice of the Dog Fairy again\n")

friend.bonus_stage()

print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")

pet_name = friend.name
pet_speciman = friend.speciman
pet_stamina = friend.stamina


#print(pet_name,pet_speciman, pet_stamina)                                       # testing 
#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                          # testing



import stage_2_pkg.milestone_2_2                    # go to the stage 2 milestone#2 disable this when you test.