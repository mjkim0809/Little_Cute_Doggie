from intro_pkg.setting import Cute
from intro_pkg.config import ti,tpp

print("""
                                         _     _ _   _   _         ____      _         ____                    _      
                                        | |   (_) |_| |_| | ___   / ___|   _| |_ ___  |  _ \  ___   __ _  __ _(_) ___ 
                                        | |   | | __| __| |/ _ \ | |  | | | | __/ _ \ | | | |/ _ \ / _` |/ _` | |/ _ \`
                                        | |___| | |_| |_| |  __/ | |__| |_| | ||  __/ | |_| | (_) | (_| | (_| | |  __/
                                        |_____|_|\__|\__|_|\___|  \____\__,_|\__\___| |____/ \___/ \__, |\__, |_|\___|
                                                                                                   |___/ |___/        

    """)



print("                                        ====================== Journey of your Little Friend ==========================")

print("""
                                                                Copyright (c) 2023 MJ Kim
                                                                    All Right Reserved
      
      """)

ti("\n\ntip(1): press 'Enter' Key to see the next messsage")
ti("tip(2): play the game with full screen\n\n\n\n")

# Type a name 
while True: 
    print("What's the name of your little cute friend?")
    pet_name = input ("Type your furry cute friend's name: ")
    
    ti(f"\nIs your friend name '{pet_name}'?")
    ti("If the name is correct?\nType yes or no: ")
    answer = input("Yes or No?: ")
    if answer.casefold() == "yes": 
        break
    elif answer.casefold() == "no":
        ti("\nRetype your friend's name")
        continue
    else:
        ti("Invalid Entry. Try again.")
        continue


# Choose the specimen 
while True: 
    print("\n")
    ti("""Is your friend a dog?
1. Yes, he/she is a lovely dog (type "dog")
2. No, he/she is not a dog but actually a furry cat (type "cat")""")
    
    pet_speciman = input("Dog or Cat?: ")
    

    #choose a dog 
    if pet_speciman.casefold() == "dog":
        print("""
    ___
 __/_  `.  .----.
 \_,` | \-'  /   )`-')
  "") `"`    \  ((`"`
 ___Y  ,    .'7 /|
(_,___/...-` (_/_/ 
""")
        ti (f"Awesome! The story of {pet_name} will begin soon! \n")
        friend = Cute(pet_name,pet_speciman,10)                                            # Dog's defulat stamina point = 10 
        #ti(friend.name, friend.speciman, friend.stamina)                                 # testing
        break
    
    #choose a cat
    elif pet_speciman.casefold() == "cat":
        print("""
    |\__/,|   (`\`
  _.|o o  |_   ) )
-(((---(((--------
""")
        ti (f"Awesome! The story of {pet_name} will begin soon! \nThe journey will be tougher, but your braveness will be appreciated")
        friend = Cute(pet_name,pet_speciman, 5)                                            # Cat's defulat stamina point = 5
        #ti(friend.name, friend.speciman, friend.stamina)                                 # testing
        break

    else: 
        ti("Invalid Choice. Try Again. \n")
        continue

ti("\nIs he/she ready to go on a new adventure?")
ti("1. Yes, he/she is ready.")
ti("2. No, he/she is not ready.")
ti("You chosee the number.\n")

while True:
    
    option_1 = input("Your Choice: ")
    
    if option_1 == "1":
        ti (f"Great! The story of {pet_name} will begin soon!\n")
        ti("Passcode to the intro is '0826' Remember this.\n")
        break

    elif option_1 == "2":
        ti("That's unfortuate. Come back and he/she gets ready.")
        ti("GoodBye.")
        
        exit()

    else: 
        ti("Invalid Choice. Try Again.\n")
        continue




print("""                                            ========== Little Cute Doggie ========== 
                                            ====== Journey of your Little Dog =======
                                            -------------Introduction --------------""", "\n","\n")


while True:
    passcode_0 = input("What is the passcode? ")
    if passcode_0 == "0826":
        ti(f"Hi. {friend.name} seems to be ready.\n")
        break

    else:
        ti("Wrong passcode. Please go back to the main page.")
        continue

        
while True:
    ti("Do you think he/she is ready?")
    ti("1.Yes")
    ti(f"2.No {friend.name} still needs time.")
    ti("You chosee the number.\n")
    option_2 = input("What's your choice?: ")
    
    if option_2 == "1": 
        ti("\nSounds lovely! Let the stroy begin!")
        break
        
    elif option_2 == "2":
        ti("\nOk, take your time")
        continue
                
    else: 
        ti("\nInvalid entry. Try again.")
        continue

print("""\n\n
                    =====================================================================================================\n\n""")

ti(f"There's a little, adorable {friend.speciman} called {friend.name}\n") 
ti("He/She is a very cute, very smart, and also very loyal to you.\n")
ti("Plus.... don't be surprised\n")


ti("…\n")
ti("…\n")
ti("…\n")


ti(f"{friend.name} has a super power as well!\n") 


ti(f"{friend.name} can share his/her view and can follow your directions like magic!\n")


ti("Today, you woke up with a severe pain. After checking all symptons, you found that you have Little Cute Doggie syndrome.\n")


ti("You got out of bed and managed to crawl to the kitchen somehow.\n")


ti("You took a couple of Advil and laid down on the floor with very little concious.\n")


ti("…\n")


ti("…\n")


ti("…\n")


ti("You still feel dizzy and can not stand up even after a while.\n")

#dog 
if friend.speciman == "dog": 
    ti("""Little Cute Doggie Syndrom (LCD)... 
Depending on the bond between you and your dog, the severity may vary - it could be just a sneeze or a fatal disease.\n""")
    
    ti("""Cat demons curses dog owners with LCD sydrome. 
The stronger the connection between you and your dog, the more you will suffer.
With this evil curse, Cat demons separate dogs and their owners. 
When they feel sad with the loss of their dog, Cat demons appear before them and tempted them to have cats as their new pets...!\n""")
    
    ti(f"As you love {friend.name} so much, it became lethal flu...\n")

#cat
elif friend.speciman == "cat": 
    ti("""Little Cute Doggie Syndrom (LCD)... 
Depending on the bond between you and your dog, the severity may vary - it could be just a sneeze or a fatal disease.\n""")
    
    ti("""Cat demons curses dog owners with LCD sydrome. 
The stronger the connection between you and your dog, the more you will suffer.
With this evil curse, Cat demons separate dogs and their owners. 
When they feel sad with the loss of their dog, Cat demons appear before them and tempted them to have cats as their new pets...!\n\n""")
    
    ti(f"{friend.name} vowed that {friend.name} will fight against Cat demon for the peace between dogs and cats\n")
    
    ti(f"However, {friend.name}'s vow provoked Cat demon and you have LCD syndrome now...\n")
    
    ti(f"{friend.name} did not realize that his/her choice would bring such disastor...\n")


ti(f"({friend.name} found you collapsed in the kitchen and started staring at you.)\n")

ti("...\n")

ti("...\n")

ti("...\n")

ti(f"{friend.name} thought you were playing dead - you used to pretend to have heart attack and play dead almost everday...!\n")

ti(f"Another 30 min passed after he/she found you on the ground... {friend.name} figured out something was wrong and panicked.\n") 

ti(f"({friend.name} started to lick your face to wake you up.)\n")

ti("Even if you took Advil, the pain still didn't go away.\n")

ti(f"You could feel {friend.name}'s warm toungue.\n")

ti("'Urghhh......'\n")

ti("One thing crossed your mind while you are groaning in pain.\n")

ti("""The cure for LCD syndrome only can be found in 'little cute cave.'
And, Dogs are the only creatures allowed to enter that place and find the cure for their owner.\n""")

ti(f"You thought that you definitely cannot send {friend.name} to the 'littel cute cave' to find the cure alone.\n")
ti("You shook your head and began to crawl back to your bedroom and call 911...\n")


ti("\n(!!!)\n\n")


ti(f"The superpower of {friend.name} just activated!\n\nYour dog just read that 'the cure' and 'little cute cave' crossed your mind.\n")


ti(f"{friend.name} recalled what the neighbor dogs, Basenji said.\nHe talked about the 'Little Cute Doggie Syndrome' and said the cure is at 'little cute cave.'\n")


ti(f"{friend.name} seemded to be determined and ran out to the entrance with no hesitation.\n")


pet_name = friend.name
pet_speciman = friend.speciman
pet_stamina = friend.stamina

#ti(pet_name,pet_speciman, pet_stamina)                                       # testing 