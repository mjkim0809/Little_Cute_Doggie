# chapter test mode. disable the play mode and use this to test# 
"""
import random
import os
from intro_pkg.config import tpp, ti
from intro_pkg.setting import Cute

pet_name = "noir"
pet_speciman = "dog"
pet_stamina = 7
pet_inventory = []
"""

from intro_pkg.setting import Cute
from stage_1_pkg.milestone_1_3 import pet_name, pet_speciman, pet_stamina, pet_inventory
import os
from intro_pkg.config import tpp, ti



print("""                                            ========== Little Cute Doggie ========== 
                                            ====== Journey of your Little Dog =======
                                            ---------------- Stage 2 ----------------""", "\n","\n")



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


ti(f"{friend.name} entered the 'little cute cave.'\n")

ti(f"The mouth of the cave is very dark and you cannot see its end at all.'\n")

ti(f"({friend.name}~~~~)\n")

ti(f"You and {friend.name} heard the voice of the Dog Fairy but could not find her\n")

ti("Dog Fairy: the mystic power of the cave dow not allow me to teleport there but I can still deliver my voice.")
ti("I cannot help you when you fight against 'Cat Demon' but I will find a way to help you before you encounter it.\n\n")


ti("The Dog Fairy dissappeared\n\n")


print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")

pet_name = friend.name
pet_speciman = friend.speciman
pet_stamina = friend.stamina


#print(pet_name,pet_speciman, pet_stamina)                                       # testing 
#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                          # testing


import stage_2_pkg.milestone_2_1                            # go to the stage 2 milestone#1 disable this when you test.