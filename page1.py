#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.
def press():
  print("You pressed the button!")
  print("A chocolate bunny hops out!")
  print("It looks pretty tasty...")
  choice = input("Press E to chomp on it, L to leave it alone, or T to talk to it.")
  if choice == "E":
    eatrabbit()
  elif choice == "L":
    leaverabbit()
  elif choice == "T":
    talkrabbit()

def eatrabbit():
  print("You grab the rabbit and are about to eat it...")
  print("Rabbit: Wait!")
  print("Rabbit: No!")
  print("Rabbit: Don't eat me!")
  print("Rabbit: How about this? Let's make a deal.")
  print("Rabbit: I give you candy and you leave me alone!")
  
