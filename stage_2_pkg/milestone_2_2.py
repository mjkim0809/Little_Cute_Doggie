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
from stage_2_pkg.milestone_2_1 import pet_name, pet_speciman, pet_stamina, pet_inventory
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


print("\n\n                 ------------------------------------------------------------------------------------------\n\n")

ti("...\n")
ti("...\n")
ti("...\n")

ti(f"After passing through bunch of bats, {friend.name} arrived a large void area")

#dog
if friend.speciman == "dog": 
    ti("???: How dare stupid dog before me!\n")
#cat
elif friend.speciman == "cat":
    ti("???: It's a surprise that I can see my fellow cat friend!\n")

print("""
     ____       /\__/\`    _____
    /     \    /`    '\`  /     \`
   /       \ === 0  0 ===/       \`
  /_-------_\  \  --  / /_-------_\  
              /        \`
             /          \`
            |            |
             \  ||  ||  /
              \_oo__oo_/#######o
        """)


ti("A little cat with demon wings appeared\n")

ti("Cat Demon: I am a Cat Demon! Kneel before me and explain why you are here!\n")

ti(f"Cat Demon asked {friend.name} to kneel before him, but {friend.name} refused and explained that you are looking for the cure for LCD syndrom\n")

#dog
if friend.speciman == "dog": 
    ti("""Cat Demon: Hmmm... Why should I help you, smelly dog? 
I see many human already became our servants, and LCD is no longer needed to make more slaves.\n""")

#cat
elif friend.speciman == "cat":
    ti("""Cat Demon: Wait... You are the one like Puss in the Boots! Why should I help you little betrayer?\n""")



ti("""Cat Demon: I do have the cure right beneath me. 
Well... As a decendant of Spinx, I will follow the trandation though. 
I will give you very difficult quizzes. If you pass all, I will give the cure.
FYI, for centuries, there's only one hero dog called 'Noir' passed the all quizzes and got the cure from me.
Solve the quizzes or leave. Choose.\n""")

ti("Cat Demon looks stubborn and seems not to move one single inch... ...\n")

ti("...\n")
ti("...\n")
ti("...\n")

if "Silver_Vine_Stick" in pet_inventory: 
    ti("Cat Demon: Hold on...! You have Meowjuana! Give me that stick!!!\n")
    ti("Cat Demon went crazy on the silver vine stick that Puss gave you earlier. !!!\n""")
    ti(f"{friend.name} waved the stick\n")
    ti("Cat Demon: Oh please! I've never tasted that stick for centuries...! Please let me taste it!!! Please!!!\n")
    ti(f"{friend.name} shook his/her head\n")
    ti("""Cat Demon: You want the cure, right? Right?
Fuxx the trandition!
I will give you the cure and you give me the stick? Deal?""")
    ti(f"{friend.name} nodded his/her head\n")
    ti("Cat Demon: Deal!\n")
    ti(f"Cat Demon handed the cure to {friend.name}, and {friend.name} handed the Silver_Vine_Stick to Cat Demon\n")
    
    # remove "Sliver Vine Stick"
    pet_inventory.remove("Silver_Vine_Stick")

    ti("Cat Demon: This is it! Now I am happy little cat!\n")


else: 
    ti("It seems like there's no choice...\n")
    ti("\nCat Demon: Ok, it seems like you are going to solve quizzes\n")
    ti("Cat Demon: First Quiz. What is always coming, but never arrives?\n")
    quiz_1 = input("Type the answer : ")
    if quiz_1.casefold() == "tomorrow": 
        ti("\nCat Demon: Correct! Let's go for the next quiz.")
        ti("Cat Demon: Second Quiz. What is it that lives if it is fed, and dies if you give it a drink?\n")
        quiz_2 = input("Type the answer : ")
        if quiz_2.casefold() == "fire": 
            ti("\nCat Demon: Correct! Let's go for the last quiz.\n")
            ti("Cat Demon: Final Quiz. Uncle Bill's farm had a terrible storm and all but seven sheep were killed. How many sheep are still alive?\n")
            quiz_3 = input("Type the answer in words (if the answer is 1, type one): ")
            if quiz_3.casefold() == "seven": 
                ti("\nCat Demon: Correct! Accroding to the trandtion, you may take the cure!\n")
            else: 
                ti("Cat Demon: That's not the answer. I cannot give you the cure. Be Gone!\n")
                friend.quiz_fail()
        else:
            ti("Cat Demon: That's not the answer. I cannot give you the cure. Be Gone!\n")
            friend.quiz_fail()
    else:
        ti("Cat Demon: That's not the answer. I cannot give you the cure. Be Gone!\n")
        friend.quiz_fail()

ti(f"{friend.name} left the cave with the cure.\n")

ti(f"Only thing left to do is that {friend.name} comes back to you.\n")



print("\n\n                 ------------------------------------------------------------------------------------------\n\n")

pet_name = friend.name
pet_speciman = friend.speciman
pet_stamina = friend.stamina


#print(pet_name,pet_speciman, pet_stamina)                                       # testing 
#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                          # testing



print("\n\n                 ------------------------------------------------------------------------------------------\n\n")
