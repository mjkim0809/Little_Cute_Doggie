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

# Actual play mode. Disable test mode block first # 

from intro_pkg.setting import Cute
from stage_1_pkg.milestone_1_1 import pet_name, pet_speciman, pet_stamina, pet_inventory
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
        sad_1_1 = input ("Yes or No?")
        if sad_1_1.casefold() == "yes":
             os.system('play.py')
            
        elif sad_1_1.casefold() == "no":
            ti("Good Bye") 
            exit()
        else:
            ti("Invalid Entry")
            continue
    else:
        ti("")
        break


print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")

ti(f"{friend.name} walks toward the bridge. After 30 min walking, {friend.name} heard somebody was looking for help.\n")
ti("???: PLEASE SOMEBODY HELP ME!!!\n")
ti(f"{friend.name} dashed to the bridge and found that someone is floundering the river.\n")
ti("Puss in the boots: Finally!!! Amigo! My name is Puss! Can you please help me...?\n")


#when your pet's specimen = Dog
if friend.speciman.casefold() == "dog":
    ti("(Damn... It's a cat! It's a damn cat!)\n")     
    ti(f"{friend.name} also became somewhat hesitant like you\n")    
    ti("Puss in the boots: I know cats and dogs have never been in a good relationship ever, but... please help little Puss...\n\n\n")
    print("""
                ____             
                \ _ `\          
                 | \  `\._      
                 |  |  _/ `-.._
                 |  /-'  // /.'`-. .--.__
                 /-'    || // //  |    __\`
               ./   .` |\///_//   \  /'   |
             .'.-.__.` \ |/'-' .'  \|    /
            / ( ____`.\ |/ .' '.'   |\  /
           /  -//   \     /- _  '     `'|
           |  ||o    ;       __`--      |
           |   \    /      //  `.  \    |
           \    `---'     |/o    \_ )   \`
         _ _\_    /       |      /       |
       _-_`-__-_.-'|__    \`-..-'       /
      '  .--_--_-.. \_\/_              /
        ' /    \... / .. \_-___       / \`
         /      `-._| ..-._--___     /   \`
        /    .---.|  `-.__/`--.__---'     |
       /_.--/ . . \__/   _   `--._-.      |
    .-'    | || | |   .-' `-.     \ `\    |
  .'       `-\/\|-'  |  / /  \     `\ \   |
 /                    \/ | .  |           |
/                      \_/_/ / \          |
|                          \/   \         |
""")


    ti("\n\n(Puss seems to need help desperately... )\n")
    ti(f"(Most of cats worship Cat demons, and there's a high chance that Puss is one of acolytes and attack your {friend.speciman}...)\n")

    while True: 
        ti("""Will you have your dog to help Puss? 
A. Nah... Cats are gross. Just keep going your way
B. No matter what he is, the life matters. Let's save him!\n""")
        ti("(Choose the alphabet)")
        option_1_2 = input("Will you have your dog to help Puss?: ")

        if option_1_2.casefold() == "a":
            ti("\n You cannot risk your dog to save a potential Cat demon acolyte \n")            
            ti("Puss in the boots: You Damn Dog!!! Argh!!!\n")            
            ti(f"{friend.name} crossed the bridge as leaving behind Puss. A big wave splashed Puss, and he got swept away...\n")
            
            friend.penalty(0)

            print("\nCurrent stamina balance : ", friend.stamina)
            ti(f"{friend.name} has {pet_inventory}")
            break

        elif option_1_2.casefold() == "b":
            ti(f" \n You made a hard decision,but {friend.name} respected your decision. Actually, {friend.name} felt proud of you.\n")            
            ti(f"{friend.name} jumped into the river and swam toward Puss.\n")            
            ti(f"{friend.name} : Woof! Woof! (ride on my back!)\n")            
            ti(f"Puss stares {friend.name} with eyes of surpirse and gratitude\n")            
            ti("Puss in the boots: Thank you so much, amigo!\n")            
            ti("Puss climbed back to your dog's back. Your dog swam back to the nearest river shore.\n")            
            ti("River tides were tough, but your dog managed to get out of the river somehow\n")            
            ti(f"(However, your {friend.speciman} lost (3) point stamina...)\n")                                                      # penlaty point = 3, adjust it after testing
            friend.penalty(3)
            
            ti("Puss in the boots: Thank you so much, buddy! Without you, I would be the damn drowned cat!\n")            
            ti("Puss in the boots: I am the cat who knows the honor. What can I do for you? May I ask where you are heading?\n")            
            ti(f"({friend.name} explains the whole story to Puss)\n")            
            ti("Puss in the boots: So, you are on the way to the 'little cute cave' to save your friend!\n")            
            ti("Puss in the boots: I am glad that there's a way I can help you out!\n")            
            ti("Puss took off his boots and pulled out a shiny stick from one of his boots\n")            
            ti("Puss in the boots: This is a 'Silver Vine Stick', and this will help you at some point!\n")
            
            print(f"{friend.name} obtained 'Silver_Vine_Stick'!\n")
            
            pet_inventory.append("Silver_Vine_Stick")                                                                  # obtain silver vine stick 

            ti("Puss in the boots: Good luck on your jorney my dear friend!\n")
            
            ti(f"Your {friend.speciman} crossed the bridge. It was fulfilling as {friend.name} saved a life \n")
            
            print(f"\nCurrent stamina balance : {friend.stamina}")
            print(f"{friend.name} has {pet_inventory}")
            break
        else:
            ti("Invalid Entry. Try Again")
            continue

#when your pet's specimen = Cat
elif friend.speciman.casefold() == "cat":
    ti("(It's a cat!)\n") 
    
    ti(f"{friend.name} also became somewhat hesitant like you \n")
    
    ti("Puss in the boots: God bless you! Please help me, my cat friend!... I will return the favor for sure! \n")
    
    ti("(Puss seems to need help desperately... ) \n\n")
    print("""
                ____             
                \ _ `\          
                 | \  `\._      
                 |  |  _/ `-.._
                 |  /-'  // /.'`-. .--.__
                 /-'    || // //  |    __\`
               ./   .` |\///_//   \  /'   |
             .'.-.__.` \ |/'-' .'  \|    /
            / ( ____`.\ |/ .' '.'   |\  /
           /  -//   \     /- _  '     `'|
           |  ||o    ;       __`--      |
           |   \    /      //  `.  \    |
           \    `---'     |/o    \_ )   \`
         _ _\_    /       |      /       |
       _-_`-__-_.-'|__    \`-..-'       /
      '  .--_--_-.. \_\/_              /
        ' /    \... / .. \_-___       / \`
         /      `-._| ..-._--___     /   \`
        /    .---.|  `-.__/`--.__---'     |
       /_.--/ . . \__/   _   `--._-.      |
    .-'    | || | |   .-' `-.     \ `\    |
  .'       `-\/\|-'  |  / /  \     `\ \   |
 /                    \/ | .  |           |
/                      \_/_/ / \          |
|                          \/   \         |
""")

    while True: 
        ti("\n\n\nWill you have your cat to help Puss?")
        ti("A. Nah... Cats are gross. Just keep going your way")
        ti("B. No matter what he is, the life matters. Let's save him!\n")
        ti("(Choose the alphabet)")
        
        option_1_2_cat = input("Will you have your cat to help Puss?: ")

        if option_1_2_cat.casefold() == "a":
            ti("\n You cannot risk your cat to save a potential Cat demon acolyte\n ")
            
            ti("Puss in the boots: Damn you!!! Argh!!!\n")
            
            ti(f"{friend.name} crossed the bridge as leaving behind Puss. A big wave splashed Puss, and he got swept away...\n")
            
            ti(f"However, your {friend.speciman} felt guilty as {friend.name} walked away and let him die...\n")
            
            ti(f"(Your {friend.speciman} got stressed out so much and lost (2) stamina points.)")         # penlaty point = 2, adjust it if needed after testing
            
            friend.penalty(2)
            print(f"Current stamina balance : {friend.stamina}")
            print(f"{friend.name} has {pet_inventory}")
            break

        elif option_1_2_cat.casefold() == "b":
            ti(f" \n You made a hard decision,but {friend.name} respected your decision. Actually, {friend.name} felt proud of you.\n")
            
            ti(f"{friend.name} jumped into the river and swam toward Puss.\n")
            
            ti(f"You know what? One of {friend.name}'s ancestors is a cousin of tigers, so {friend.name} is actually capable of swimming!\n") 
            
            ti(f"Puss stares {friend.name} with eyes of surpirse and gratitude. \n")
            
            ti("Puss in the boots: Thank you so much, amigo!")
            
            ti(f"Your {pet_speciman} dragged Puss w/ his cloaks and swam back to the nearest river shore. \n")
            
            ti("River tides were tough, but your dog managed to get out of the river somehow")
            
            ti(f"(Your {friend.speciman} lost (1) point stamina...)\n")                                    # penlaty point = 1, adjust it after testing
            
            friend.penalty(1)
            
            ti("Puss in the boots: Thank you so much, buddy! Without you, I would be the damn drowned cat! \n")
            
            ti("Puss in the boots: I am the cat who knows the honor. What can I do for you? May I ask where you are heading?\n")
            
            ti(f"({friend.name} explains the whole story to Puss)\n")
            
            ti("""Puss in the boots: What a coincidence! I am also a cat like you fright for the peace between dog and cat. 
So, you are on the way to the 'little cute cave' to save your friend!\n""")
            
            ti("Puss in the boots: I am glad that there's a way I can help you out!\n")
            
            ti("Puss took off his boots and pulled out a shiny stick from one of his boots\n")
            
            ti("Puss in the boots: This is a 'Silver Vine Stick', and this will help you at some point!\n")

            pet_inventory.append("Silver_Vine_Stick")                                                                 # obtain silver vine stick 
            
            ti("Puss in the boots: Good luck on your jorney my dear friend!\n")
            
            ti(f"Your {friend.speciman} crossed the bridge. It was fulfilling as {friend.name} saved a life")
            
            print(f"\nCurrent stamina balance : {friend.stamina}")
            ti(f"{friend.name} has {pet_inventory}")
            break
        else:
            ti("Invalid Entry. Try Again")
            continue

print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")

friend.bonus_stage()

print("\n\n                                        ------------------------------------------------------------------------------------------\n\n")

pet_name = friend.name
pet_speciman = friend.speciman
pet_stamina = friend.stamina


#print(pet_name,pet_speciman, pet_stamina)                                       # testing 
#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                          # testing


import stage_1_pkg.milestone_1_3                                                # go to the stage 1 milestone#3 disable this when you test.

