# chapter test mode. disable the play mode and use this to test# 
"""
import random
from intro_pkg.config import tpp, ti
from intro_pkg.setting import Cute

pet_name = "noir"
pet_speciman = "dog"
pet_stamina = 7
pet_inventory = []
"""

# Actual play mode. Disable test mode block first # 

from intro_pkg.setting import Cute
from stage_1_pkg.stage_1_0 import pet_name, pet_speciman, pet_stamina, pet_inventory
import random
from intro_pkg.config import tpp, ti


friend = Cute(pet_name,pet_speciman, pet_stamina)                                        # to import variables from file to file 

#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                                     # testing

print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")

ti(f"""\nWhile you had a talk with the Dog Fairy, your {friend.speciman} ran relentlessly to locate the 'little cute cave.'\n
Basenji told him that the cave is in the 'pretty cute forest.'\n
{friend.name}, however, knew the whereabout of the forest but not the specific location of its entrace...\n""")

ti(f"You could feel that {friend.name} felt lost. So, you instructed him to ask around the location of the cave.\n")

ti(f"{friend.name} read your mind. He/she slowed down and began to search for animal folk to ask the location of the cave.\n")

ti("...\n")
ti("...\n")
ti("...\n")
ti("...\n")
ti("...\n")

ti(f"A couple of hours later, {friend.name} encountered a small Chihuahua.\n")

ti("'Hey! My dear doggie friend! My name is TINY, but my gut is never tiny ever!'\n")

ti(f"TINY waved his paw to ask {friend.name} to come over\n")

ti("TINY: Hey! A small human shared this food with me! Do you wanna try some?\n")

ti(f"({friend.name} smelled sweetness and started to drool. However, the color of food is dark brown. And, {friend.name} smelled bitterness as well...)\n\n")

while True:
    ti(f"""Will you allow {friend.name} to try it?
a. No. Stop TINY!!!
b. Why not? Let's have fun together :D""")
    tpp("\n(Choose the alphabet)\n")

    option_1_1 = input("Will you allow your friend to try it?: ")
    
    if option_1_1.casefold() == "a":
        ti(f"\nYou figured out that it is chocolate! You asked {friend.name} to stop TINY to eat it\n")
        
        ti("Your dog explained to TINY that it is called 'chocolate', which is poison to dogs\n")
        
        ti("""TINY: OMG...! I am sure that little human had no intetion to harm me...but this gives me goosebumps...
Hey, buddy! Thank you for saving my life! You can find the entrace of 'pretty cute forest' after you cross that bridge
Good luck to your journey!\n""")

        friend.penalty(0)
               
        break

    elif option_1_1.casefold() == "b":
        ti(f"\nTINY and {friend.name} tried the food together.\n")
        
        ti(f"However, a couple of minutes later, both {friend.name} and TINY felt unwell and started to puke.\n")
        
        penalty_1_1 = random.randint(1,3)                                                                           # penalty point is random 
        ti(f"{friend.name} ended up vomiting all the food he had today and lost {penalty_1_1} stamina points \n")
        friend.penalty(penalty_1_1)
        
        
        
        ti("TINY: I am so... sorry that I put you in ... the trouble....\n")
        
        ti("TINY: You said that you are looking for the entrance of 'pretty cute forest...' Cross that bridge, then you will see the entrance... \n")
        break

    else:
        ti("Invalid Entry. Try Again")
        continue

pet_name = friend.name
pet_speciman = friend.speciman
pet_stamina = friend.stamina


#print(pet_name,pet_speciman, pet_stamina)                                       # testing 
#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                          # testing

print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")


friend.stamina_balance()


print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")

import stage_1_pkg.milestone_1_2                                # go to the stage 1 milestone#2 disable this when you test. 
