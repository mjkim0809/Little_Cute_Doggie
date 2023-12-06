# 1. Please read README.MD 
#2. Flow chart "Little Cute Doggie V.1.0" is available int the same folder 
#3. Check mijkim0809 in GITHUB 
#4. Copyright (c) 2023 MJ Kim 

import sys
from intro_pkg.config import tpp, ti


import intro_pkg.intro_0

# Stage 1
while True: 
    ti("Give the passcode to open the next stage.\n(Hint: what's the name of the neighbor dog?)")
    passcode_1 = input("Type the passcode: ")
    
    if passcode_1.casefold() == "basenji":
        import stage_1_pkg.stage_1_0
        break
    else:
        print("invalid entry")
        continue

# Stage 2
while True: 
    ti("Name the food very poisonus to the dog (Hint: Name the food that TINY tried to share it with your friend)")
    passcode_2 = input("Type the passcode: ")
    
    if passcode_2.casefold() == "chocolate":
        import stage_2_pkg.stage_2_0
        break

    else:
        print("invalid entry")
        continue

#Epilouge 
while True: 
    ti("What's the name of the hero dog who passed the Cat Demon's test?")
    passcode_2 = input("Type the passcode: ")
    
    if passcode_2.casefold() == "noir":
        import epilouge_pkg.epilogue
        break

    else:
        print("invalid entry")
        continue
