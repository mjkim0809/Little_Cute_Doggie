print("""\n\n\n\n                                            ========== Little Cute Doggie ========== 
                                            ==== Journey of your Little Friend =====
                                            ---------------- Stage 1 ----------------\n\n\n\n""")


from intro_pkg.intro_0 import pet_name, pet_speciman, pet_stamina
from intro_pkg.setting import Cute
from intro_pkg.config import tpp, ti


friend = Cute(pet_name,pet_speciman, pet_stamina)                                        # to import variables from file to file 
pet_inventory = []                                                                        # to set initial list

ti(f"You called {friend.name}\n")

ti(f"Even before you called and stop {friend.name}, {friend.name} ran out of the house.\n")

ti("...\n")
ti("...\n")
ti("...\n")
ti("You stared the door for a while. You felt so guilty that you couldn't stop him\n")

ti("While you suffered from guiltness, a Dog Fairy appeared.\n")


if friend.speciman.casefold() == "dog":
    ti("Dog Fairy: Don't worry. Even if the journey to the cave will be tough, you can help him to find the cure and come back home safely.\n")
    
    
    if friend.name.casefold() == "noir":
        ti("She is about to snap his finger, but...\n")
        
        ti("Dog Fairy: Wait a moment... your dog looks like a decendant of the hero dog, Noir. \n")
        ti("Dog Fairy: I can definitely see that your dog is way stronger than any other dogs. It's my honor to help the children of the mighty hero.\n")
        
        ti("(As your dog is a decendant of the hero dog, Noir, your dog will start with 20 stamina point.) \n")

        friend.blessing(10)
        
        #print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
    else:
        ""
        #print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing

elif friend.speciman.casefold() == "cat": 
    ti(f"Dog Fairy: Your friend is brave and wise enough to make a tough decision so don't worry.\n I will give a blessing to {friend.name}\n")
    
    ti(f"(Now, {friend.name} can visit the 'little cute cave'!)\n")
    
    ti(f"(Dog Fairy's wish worked! {friend.name} got (2) stamina points!)\n")
    friend.blessing(2)
    #print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing


ti(f"Dog Fairy: There will be many crossroads before your friend. Help {friend.name} to make the right choices.\n")

ti("The Dog Fairy dissapeared into the smoke. You don't get 100% what she said, but you will do your best so that your dog to come back sound and safe.\n")
#print(friend.name, friend.speciman, friend.stamina,"\n")                                       # to test the easteregg works or not 


pet_name = friend.name
pet_speciman = friend.speciman
pet_stamina = friend.stamina


#print(pet_name,pet_speciman, pet_stamina,"\n")                                       # testing 
#print(friend.name, friend.speciman, friend.stamina,"\n")                                 # testing
#print(pet_inventory,"\n")                                                          # testing


import stage_1_pkg.milestone_1_1