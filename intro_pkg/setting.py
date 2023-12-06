from intro_pkg.config import tpp, ti
import os

# class "Cute" to for player's pet name, speciman, stamina, and instances method for stamina balance, penalty
class Cute:                 
    def __init__ (self, name, speciman, stamina):
        self.name = name
        self.speciman = speciman
        self.stamina = stamina
                                            # Dog's defulat stamina point = 10, Cat's defulat stamina point = 7, bonus point if dog name = noir
    def penalty(self, penalty):
        if penalty < self.stamina: 
            self.stamina -= penalty
        else:
            self.stamina = 0

    def blessing(self, blessing): 
        self.stamina += blessing

    def stamina_balance(self):          
        print (f"Current {self.name}'s stamina is {self.stamina}\n")

        if self.stamina <=0:                                                                                        
            ti(f"({self.name} eventually got knocked out, and you lost the view shared with your firend.)\n")            
            ti("...\n")
            ti("...\n")
            ti("...\n")
            ti("A Dog Fairy appeared\n")
            ti("Dog Fairy: The journey should've been tough but not that difficult to complete it.\n")
            ti(f"Dog Fairy: {self.name} has loved you and began this journey for your own sake, but your wrong choices led {self.name} to the death.\n")
            ti("Dog Fairy: I will wind back the clock to the very beginning. May the mighty hero dog Noir bless you to make right choices next time...\n")
            ti("(She made a finger snap)\n")
            ti("...\n")
            ti("...\n")
            ti("...\n")
            ti("(Restart the game if you want your little cute doggie to finish the journey.)")
            

        elif self.stamina <= 5:
            ti(f"(Your {self.speciman} seemed to be exhausted. Please take a good care of your little cute {self.speciman}!)\n")
        else:
            ti(f"(You {self.speciman} still seemed to be healthy and confident! You've been taking care of {self.name} well. Please keep taking care of your little cute friend!\n)")

    # from milestone 1_2, it will start while True 
    def bonus_stage(self):
        if self.stamina <= 3: 
            import random
            ti(f"{self.name} feels dizzy and callapsed...\n A moment later, a Dog Fairy appears and say, \n")
            ti("""Dog Fairy: My lovely furry friend ~ 
I am here to help you. 
I will choose one number among 1,2,3 and 4 and your owner guesses it is even or odd.\n""")
            ti(f"{self.name} is waiting for your decision...\n")
            guess_number = input("What is your choice? Even or Odd?: ")
            
            if guess_number.casefold() == "odd":
                if random.randint(1,4) == 1 or random.randint(1,4) == 3:
                    ti("Dog Fairy: Congratulation! \n")
                    ti(f"A magical power is flown to him! {self.name} gets (3) stamina points!" )

                    self.stamina += 3

                    print(f"Your dog's stamina now is {self.stamina} \n")

                else:
                    ti("Dog Fairy: I am so sorry, sweetie, but your owner is not that desperate to make a right guess.\n")
                    
                    ti("(She dissapeared into the smoke.)")

            elif guess_number.casefold() == "even":
                if random.randint(1,4) == 2 or random.randint(1,4) == 4:
                    ti("Dog Fairy: Congratulation! \n")
                    ti(f"A magical power is flown to him! {self.name} gets (3) stamina points!" )

                    self.stamina += 3

                    print(f"Your dog's stamina now is {self.stamina} \n")
                
                else:
                    ti("Dog Fairy: I am so sorry, sweetie, but your owner is not that desperate to make a right guess.\n")
                    ti("(She dissapeared into the smoke.)")

            else:
                ti("Dog Fairy: I am so sorry, sweetie, but your owner is not that desperate to pay attention to my question.\n")
                ti("(She dissapeared into the smoke.) \n")
        
        else:
            ti("A Dog Fairy appears and say,\n")
            ti(f"Dog Fairy: {self.name}... it seems that your owner has taken a good care of you.\n")
            ti("Dog Fairy: I will give a organic beef jerky. Hope this helps you to complete this jorney!'\n")
            ti("(The Dog Fairy dissapeared.)\n")
            ti(f"{self.name} chews the jerkey, and it tastes yummy!!!")
            self.stamina += 1
            print(f"{self.name} gets (1) stamina points!" )
            print(f"Your dog's stamina now is {self.stamina}" )
    
    def quiz_fail(self):
        ti(f"Cat Demon waved his tail. {self.name} failed to get a cure for you...")
        ti("Will you have your friend to restart the journey?")
        quiz_fail_choice = input("Type 'Yes' or 'No': ")
        if quiz_fail_choice == "Yes":
            os.system('play.py')
            
        elif quiz_fail_choice() == "no":
            print("Good Bye") 
            exit()



#testing
"""
friend = Cute("Noir","Dog",3)
print(friend.name, friend.stamina)                                             # this is for testing the function

friend.penalty(5)
print(friend.name, friend.stamina)                                             # this is for testing the function

friend.restart(friend.name, friend.speciman, friend.stamina)                                             # this is for testing the function

friend.stamina_balance(friend.name,friend.stamina)                                              # this is for testing the function

friend.bonus_stage(friend.name,friend.stamina)                                                  # this is for testing the function 
print(friend.name, friend.stamina)
"""


