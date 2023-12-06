import time, sys

#use these two functions in our program instead of the usual print() and input() functions

def tpp(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.016)
  
def ti(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.016)
  value = input()  
  return value