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
#activate when you play the game
from intro_pkg.setting import Cute
from stage_1_pkg.milestone_1_2 import pet_name, pet_speciman, pet_stamina, pet_inventory
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

ti(f"After walking for a while, {friend.name} can see the entrace of the 'pretty cute forest.'\n")
ti(f"Also can see the signboard before {friend.name}\n")

print("""\n\n                                                    🠔 To the entrance of 'Little Cute Cave' (5 miles)
     
                                                        To the entrance of 'Little Cute Cave' (2 miles) ➝\n\n""")


ti("Which path will you choose?\n")

while True: 
    choice_1_3 = input("Left = type 'left', Right = type 'right':  ")
    if choice_1_3.casefold() == 'left':
        ti(f"\n({friend.name} tilted his/her head)\n")
        ti(f"However, {friend.name} followed your direction. Even though it is a longer path, but it is a fun walk!\n")

        while True: 
            if friend.speciman == 'dog': 
                print("""
                            .--~~,__
                :-....,-------`~~'._.'
                `-,,,  ,_      ;'~U'
                _,-' ,'`-__; '--.
                (_/'~~      ''''(;
                
                """)
                break
            
            elif friend.speciman == 'cat': 
                print("""
                                                 _
                                                | \`
                                               | |
                                              | |
                        |\                   | |
                        /, ~\                / /
                        X     `-.....-------./ /
                        ~-. ~  ~              |
                            \             /    |
                            \  /_     ___\   /
                            | /\ ~~~~~   \ |
                            | | \        || |
                            | |\ \       || )
                            (_/ (_/      ((_/
                """)
                break

            else:
                print("")
                break
        
        ti(f"{friend.name} also found the deer - it was the frist time to see a deer!")
        print("""
                   /|       |\`
              `__`\`\       //__'
                   ||      ||
               \__`\`\     |'__/
                `_`\`\   //_'
                  _.,:---;,._
                  \_:     :_/
                    |@. .@|
                    |     |
                    ,\.-./ \`
                    ;;`-'   `---__________-----.-.
                   ;;;                         \_\`
                   ';;;                         |
                    ;    |                      ;
                     \   \     \        |      /
                      \_, \    /        \     |\`
                        |';|  |,,,,,,,,/ \    \ \_
                        |  |  |           \   /   |
                        \  \  |           |  / \  |
                        | || |           | |   | |
                        | || |           | |   | |
                        | || |           | |   | |
                        |_||_|           |_|   |_|
                        /_//_/           /_/   /_/

            """)    
        ti(f"{friend.name} got super excited!\n")
        ti(f"The deer noticed {friend.name} and walked toward him/her \n")
        ti(f"And, it gave you a safety hat out of nowhere and walked away\n")

        pet_inventory.append("Safety_Hat")

        ti(f"({friend.name} obtained 'Safety Hat!')\n")

        ti(f"You and {friend.name} are not sure why the deer gave you the hat, but who knows you or {friend.name} need it someday?\n")
        ti(f"Now you can see the entrance of 'Little Cute Cave.' \n")
        break


    elif choice_1_3.casefold() == 'right':
        ti(f"You and {friend.name} thought that there's no reason why to choose the longer path.")
        ti("After a while, you can see the entrance of 'Little Cute Cave.' \n")
        break

    else:
        ti("Invalid Choice. Choose Again")
        continue

print("\n\n                 ------------------------------------------------------------------------------------------\n\n")

pet_name = friend.name
pet_speciman = friend.speciman
pet_stamina = friend.stamina


#print(pet_name,pet_speciman, pet_stamina)                                       # testing 
#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                          # testing



print("\n\n                 ------------------------------------------------------------------------------------------\n\n")






