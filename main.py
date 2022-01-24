"""
Name(s): Ylan Guo
Name of Project: (Don't) Eat Everything
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

import time

def start():
  print("You find yourself in an strange room with a button. Are you going to press it?")
  choice = input("Enter A to press or B to investigate the room. ")
  while choice != "A" and choice != "B":
    print("You must choose either A or B")
    choice = input("Enter A to press or B to investigate the room. ")
  if choice == "A":
    press()
  elif choice == "B":
    investigate()
  
def die():
  print("Uh oh.")
  print("You died!\n")
  choice = input("Press R to restart. ")
  if choice == "R":
    start()

def victory():
  print("\nCongrats! You got out!")
  print("You win!\n")
  choice = input("Press Y to play again. ")
  if choice == "Y":
    start()
  

def candy():
  candy = "Eating candy... \n" * 50
  time.sleep(1.75)
  print(candy)
  time.sleep(0.50)
  print("Candy eaten!\n")

def press():
  print("You pressed the button!")
  print("A chocolate bunny hops out!")
  print("It looks pretty tasty...")
  choice = input("Press E to chomp on it, L to leave it alone, or T to talk to it. ")
  while choice != "E" and choice != "L" and choice != "T":
    print("You must choose either E, L, or T")
    choice = input("Press E to chomp on it, L to leave it alone, or T to talk to it. ")
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
  choice = input("Press Y to agree or N to refuse and eat the rabbit anyways. ")
  while choice != "Y" and choice != "N":
    print("You must choose either Y or N")
    choice = input("Press Y to agree or N to refuse and eat the rabbit anyways. ")
  if choice == "Y":
    dealY()
  elif choice == "N":
    dealN()

def dealY():
  print("You: Ok, I won't eat you.")
  print("You: Give me my candy now.")
  print("You gain 1 candy. Do you want to ea--")
  print("The rabbit suddenly becomes enormous and eats you.")
  print("Rabbit: HAHAHAHAHA YOU THOUGHT I WOULDN'T EAT YOU HAHAHA THIS IS REVENGE")
  die()

def dealN():
  print("You: Nope!")
  print("You eat the rabbit. It's very sweet.")
  print("Suddenly, you feel a bit nauseous.")
  print("Rabbit: HAHAHA I'M POISONOUS HAHAHA")
  die()

def leaverabbit():
  print("You ignore the rabbit.")
  print("Rabbit: Hey!")
  print("I'm bored! Talk to me!")
  choice = input("Press R to respond or I to continue ignoring it. ")
  while choice != "R" and choice != "I":
    print("You must choose either R or I")
    choice = input("Press R to respond or I to continue ignoring it. ")
  if choice == "R":
    talkrabbit()
  elif choice == "I":
    ignore()

def ignore():
  print("You continue to ignore the rabbit.")
  print("Rabbit: HOW DARE YOU IGNORE ME!")
  print("The rabbit suddenly becomes enormous and eats you.")
  print("Rabbit: HAHAHA SERVES YOU RIGHT")
  die()

def talkrabbit():
  print("You talk to the rabbit.")
  print("You: Hi?")
  print("Rabbit: Hello!")
  print("Rabbit: Thanks for pressing the button! I've been trapped there for so long...")
  print("Rabbit: Wanna play a game? I'll give you candy if you win!")
  choice = input("Press Y to agree or press N to refuse. ")
  while choice != "Y" and choice != "N":
    print("You must choose either Y or N")
    choice = input("Press Y to agree or N to refuse. ")
  if choice == "Y":
    gameY()
  elif choice == "N":
    gameN()

def gameY():
  print("You agree to play a game with the rabbit.")
  print("Rabbit: Yay!")
  print("Rabbit: Ok, the rules of this game are simple.")
  print("Rabbit: Just try to guess my favorite number!")
  favnum = input("Enter the rabbit's favorite number or press Y to give up. ")
  guess = 0
  while favnum != "5" and favnum != "five" and favnum != "Five" and guess < 4 and favnum != "Y":
    print("No, try again")
    guess += 1
    favnum = input("Enter the rabbit's favorite number or press Y to give up. ")
  if favnum == "5":
    favnumR()
  elif favnum == "Y":
    giveup()
  else:
    favnumW()

def giveup():
  print("Rabbit: HOW DARE YOU GIVE UP")
  print("The rabbit suddenly becomes enormous and eats you.")
  die()

def favnumR():
  print("Rabbit: Nice! You got it right!")
  print("Here's your reward!")
  print("You gain 1 candy. Do you want to eat it? Of course you do!")
  candy()
  print("The rabbit disappears and you decide to investigate the room.")
  cont = input("Press C to continue. ")
  while cont != "C":
    cont = input("Press C to continue. ")
  if cont == "C":
    investigate()

def favnumW():
  print("Rabbit: WRONG.")
  print("Rabbit: How disappointing.")
  print("The rabbit suddenly becomes enormous and eats you.")
  die()

def gameN():
  print("You refuse to play with the rabbit.")
  print("Rabbit: HOW DARE YOU!")
  print("The rabbit suddenly becomes enormous and eats you.")
  print("Rabbit: HAHAHAHA SERVES YOU RIGHT")
  die()

def investigate():
  print("After investigating the room, you find a few things.")
  print("First, a sign that says 'WARNING: DO NOT PRESS BUTTON. WILL DISPENSE CHOCOLATE BUNNY.' above the button.")
  cont = input("Press C to continue. ")
  while cont != "C":
    cont = input("Press C to continue. ")
  if cont == "C":
    investigate2()

def investigate2():
  print("Second, a piece of candy. Do you want to eat it? Of course you do!")
  candy()
  cont = input("Press C to continue. ")
  while cont != "C":
    cont = input("Press C to continue. ")
  if cont == "C":
    investigate3()

def investigate3():
  print("Third, a mysterious trapdoor. Do you want to go through it?")
  choice = input("Press Y to enter, press N to stay out and just peek inside, or press B to ignore the trapdoor and go press the button. ")
  while choice != "Y" and choice != "N" and choice != "B":
    print("You must choose either Y, N, or B")
    choice = input("Press Y to enter, press N to stay out and just peek inside, or press B to ignore the trapdoor and go press the button. ")
  if choice == "Y":
    enter()
  elif choice == "N":
    peek()
  elif choice == "B":
    press()

def enter():
  print("You open the trapdoor and jump through.")
  print("Falling...")
  time.sleep(1.00)
  print("Falling...")
  time.sleep(1.00)
  print("Falling...")
  time.sleep(1.00)
  print("You've been falling for a while...")
  time.sleep(1.00)
  print("Like a really long time actually.")
  time.sleep(1.00)
  print("Maybe you shouldn't have jumped...")
  print("Do you want to call for help?")
  choice = input("Press Y to scream or N to stay silent. ")
  while choice != "Y" and choice != "N":
    print("You must choose either Y or N")
    choice = input("Press Y to scream or N to stay silent. ")
  if choice == "Y":
    scream()
  elif choice == "N":
    splat()

def splat():
  print("Falling...")
  time.sleep(1.00)
  print("Falling...")
  time.sleep(1.00)
  print("Maybe you should've screamed...")
  time.sleep(1.00)
  print("You finally hit the ground!")
  print("Splat!")
  die()

def scream():
  print("You scream for help.")
  print("Huh? What's that?")
  print("You hear the sound of hooves and squeaking.")
  time.sleep(1.00)
  print("???: Don't worry! I'll catch you!")
  print("You land in a pile of... chocolate cream?")
  print("???: Hello! What's your name?")
  yn = input("Enter your name or press 1 to refuse to answer. ")
  if yn == "1":
    rude()
  else: 
    yn1 = yn + "!"
    print("Mousse: Hi", yn1, "I'm the chocolate mousse mouse moose!")
    print("How do you want to respond?")
    choice = input("Press A to ask what that means, press B to ask if you're going to be eaten, press C to run for your life, or press D to eat. ")
    while choice != "A" and choice != "B" and choice != "C" and choice != "D":
      print("You must choose either A, B, C, or D.")
      choice = input("Press A to ask what that means, press B to ask if you're going to be eaten, press C to run for your life, or press D to eat. ")
    if choice == "A":
      ask()
    elif choice == "B":
      ask2()
    elif choice == "C":
      ruuun()
    elif choice == "D":
      eatmousse()


def rude():
  print("You: I'm not telling you my name.")
  print("???: Well that's rude!")
  print("You get thrown out of the chocolate cream. You look up and realize the chocolate cream was a mouse moose hybrid made of chocolate mousse. ")
  print("The chocolate mousse mouse moose eats you.")
  die()

def ruuun():
  print("You scramble out of the chocolate cream and sprint away.")
  print("You trip and fall into a pit.")
  print("Falling...")
  time.sleep(1.00)
  print("Falling...")
  time.sleep(1.00)
  print("You hit the ground and splat!")
  die()

def eatmousse():
  print("You grab a handful of the chocolate pudding and eat it. It's very sweet.")
  print("Mousse: Did you just eat me???")
  print("Mousse: How rude!")
  print("You get thrown out of the chocolate cream and the chocolate mousse mouse moose eats you.")
  die()

def ask():
  print("You: What does that mean???")
  print("Mousse: It means I'm part mouse, part moose, and made out of chocolate mousse!") 
  print("Mousse: My turn to ask a question!")
  print("Mousse: Why were you falling?")
  choice = input("Press A to refuse to answer, B to explain everything, or C to lie. ")
  while choice != "A" and choice != "B" and choice != "C":
    print("You must choose either A, B, or C")
    choice = input("Press A to refuse to answer, B to explain everything, or C to lie. ")
  if choice == "A":
    rude2()
  elif choice == "B":
    explain()
  elif choice == "C":
    lie()
  
def ask2():
  print("You: Are you going to eat me?")
  print("Mousse: Of course not!")
  print("Mousse: Unless, of course, you give me a reason to...")
  print("Mousse: But I'm sure you won't, you seem like a polite person.")
  print("Mousse: My turn to ask a question!")
  print("Mousse: Why were you falling?")
  choice = input("Press A to refuse to answer, B to explain everything, or C to lie. ")
  while choice != "A" and choice != "B" and choice != "C":
    print("You must choose either A, B, or C")
    choice = input("Press A to refuse to answer, B to explain everything, or C to lie. ")
  if choice == "A":
    rude2()
  elif choice == "B":
    explain()
  elif choice == "C":
    lie()

def rude2():
  print("You: I'm not telling you.")
  print("Mousse: How rude!")
  print("You get thrown out of the chocolate cream and the chocolate mousse mouse moose eats you.")
  die()

def lie():
  print("You: Well, I used to be a bird, but then I became human while flying, and fell!")
  print("Mousse: Strange.. I haven't seen any birds around here recently, they've all been flying away...")
  print("Mousse: Are you lying?")
  print("Mousse: How rude!")
  print("You get thrown out of the chocolate cream and the chocolate mousse mouse moose eats you.")
  die()

def explain():
  print("You explain everything that's happened to you.")
  print("Mousse: I see...")
  print("Mousse: Well if you want to go home, I may be able to help you.")
  print("You: How?")
  print("Mousse: There's a door labelled exit that way. You'll reach if in about an hour if you walk. You can't miss it.")
  print("Mousse: I can't accompany you because I'm a bit busy today, but I'll give you a candy to help you along the way.")
  print("You gain 1 candy. Do you want to ea--")
  print("Mousse: You shouldn't eat it now, it'll be useful later. Also, be careful! There're a lot of random holes in the ground!")
  print("You: Thanks!")
  choice = input("Press A to run for the exit, B to start walking towards the exit, or C to eat the candy anyways. ")
  while choice != "A" and choice != "B" and choice != "C":
    print("You must choose either A, B, or C")
    choice = input("Press A to run for the exit, B to start walking towards the exit, or C to eat the candy anyways. ")
  if choice == "A":
    ruun()
  elif choice == "B":
    walk()
  elif choice == "C":
    eatcandy()

def ruun():
  print("You get out of the chocolate mousse mouse moose and start running in the direction the mousse said to go.")
  print("You trip and fall into a pit. Maybe you should've listened when they said to watch out for random holes in the ground...")
  print("Falling...")
  time.sleep(1.00)
  print("Falling...")
  time.sleep(1.00)
  print("You hit the ground and splat!")
  die()

def walk():
  print("You get off the chocolate mousse mouse moose and begin walking towards the exit. As you walk, you nearly fall into a giant hole. Luckily, you listened to the mousse and were careful!")
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.00)
  print("You're beginning to get really tired. As you walk, you remember the candy the chocolate mousse mouse moose game you.")
  choice = input("Press Y to eat the candy or N to continue walking. ")
  while choice != "Y" and choice != "N":
    print("You must choose either Y or N")
    choice = input("Press Y to eat the candy or N to continue walking. ")
  if choice == "Y":
    eatcandy2()
  elif choice == "N":
    walk2()

def walk2():
  print("You continue to walk.")
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.50)
  print("Walking...")
  time.sleep(1.75)
  print("You collapse from exhaustion.")
  die()

def eatcandy():
  print("You toss the candy into your mouth.")
  candy()
  print("Mousse: Well it's your choice.")
  choice = input("Press A to run for the exit or B to start walking towards the exit.")
  while choice != "A" and choice != "B":
    print("You must choose either A or B")
    choice = input("Press A to run for the exit or B to start walking towards the exit. ")
  if choice == "A":
    ruun()
  elif choice == "B":
    walk3()

def walk3():
  print("You get off the chocolate mousse mouse moose and begin walking towards the exit. As you walk, you nearly fall into a giant hole. Luckily, you listened to the mousse and were careful!")
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.00)
  print("You're beginning to get really tired. As you walk, you think about the candy the chocolate mousse mouse moose gave you. It's a pity you already ate it...")
  walk2()

def eatcandy2():
  print("You toss the candy into your mouth.")
  candy()
  print("Now that you've eaten the candy, you feel much better and continue walking happily.")
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.00)
  print("You see a giant door with a big red exit sign on top in the distance.")
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.00)
  print("Walking...")
  time.sleep(1.00)
  print("You reach the door!")
  print("The door opens as you approach and you exit the strange place.")
  victory()

def peek():
  print("You open the trapdoor and look through.")
  print("You spot a ladder leading down, but can't see much farther than that.")
  choice = input("Press Y to climb down the ladder or N to go press the button. ")
  while choice != "Y" and choice != "N":
    print("You must choose either Y or N")
    choice = input("Press Y to climb down the ladder or N to go press the button. ")
  if choice == "Y":
    ladder()
  elif choice == "N":
    press()

def ladder():
  print("You climb down the ladder.")
  print("The ladder stops at a mysterious room. You can either go into the room or continue going down and fall. ")
  choice = input("Press Y to enter the room or N to let go of the ladder and continue going down. ")
  while choice != "Y" and choice != "N":
    print("You must choose either Y or N")
    choice = input("Press Y to enter the room or N to let go of the ladder and continue going down. ")
  if choice == "Y":
    room()
  elif choice == "N":
    enter()

def room():
  print("The room is mostly empty.")
  print("You find a small desk with a journal on top, open to the last page. ")
  choice = input("Press A to read the last page, B to skim through the entire journal, C to look through the drawers, or D to go back to the ladder and jump down. ")
  while choice != "A" and choice != "B" and choice != "C" and choice != "D":
    print("You must choose either A, B, C, or D")
    choice = input("Press A to read the last page, B to skim through the entire journal, C to look through the drawers, or D to go back to the ladder and jump down. ")
  if choice == "A":
    read()
  elif choice == "B":
    print("You flip through the journal, but all the pages are empty except for the last page.")
    time.sleep(1.00)
    read()
  elif choice == "C":
    snoop()
  elif choice == "D":
    enter()

def snoop():
  print("You find a candy in one the drawers. Everything else is empty.")
  print("You gain a candy. Do you want to eat it? Yes, obviously. ")
  candy()
  choice = input("Press A to read the last page, B to skim through the entire journal, or C to go back to the ladder and jump down. ")
  while choice != "A" and choice != "B" and choice != "C":
    print("You must choose either A, B, or C")
    choice = input("Press A to read the last page, B to skim through the entire journal, or C to go back to the ladder and jump down. ")
  if choice == "A":
    read()
  elif choice == "B":
    print("You flip through the journal, but all the pages are empty except for the last page.")
    read()
  elif choice == "C":
    enter()

def read():
  print("You read the last page.")
  print("\nIt says: \nIf you'reading this journal, I assume you too have been trapped here. After many years of research, I have found my way out of this place, and so I am recording it to assist anyone else who finds themselves here.")
  print("The way out is simple. If you press and hold the button, a bird made of marshmallows will appear. If you give it something to eat, it'll fly you out of here. It loves chocolate.")
  print("I also suspect there's a way out if you jump down, but I'm scared of dying from the fall.")
  print("Anyways, I'm leaving now. I've destroyed all my research so the dangerous secret of how to make infinite chocolate bunnies will never be discovered.")
  print("\nWell that was interesting...")
  choice = input("Press A to go back up the ladder or B to jump down. ")
  while choice != "A" and choice != "B":
    print("You must choose either A or B")
    choice = input("Press A to go back up the ladder or B to jump down. ")
  if choice == "A":
    up()
  elif choice == "B":
    enter()

def up():
  print("You climb back up the ladder.")
  choice = input("Press A to press the button or B to press and hold the button. ")
  while choice != "A" and choice != "B":
    print("You must choose either A or B")
    choice = input("Press A to press the button or B to press and hold the button. ")
  if choice == "A":
    press()
  elif choice == "B":
    hold()

def hold():
  print("You press and hold the button.")
  print("A large bird made of marshmallows appears in front of you.")
  print("Bird: FOOD")
  print("Bird: I WANT FOOD")
  print("Bird: GIVE ME FOOD")
  choice = input("Press A to tell the bird you don't have any food, B to escape by jumping through the trapdoor, or C to press the button. ")
  while choice != "A" and choice != "B" and choice != "C":
    print("You must choose either A, B, or C")
    choice = input("Press A to tell the bird you don't have any food, B to escape by jumping through the trapdoor, or C to press the button. ")
  if choice == "A":
    nofood()
  elif choice == "B":
    enter()
  elif choice == "C": 
    press2()

def nofood():
  print("You: Sorry, I don't have any food...")
  print("Bird: NO FOOD????")
  print("Bird: BUT I'M HUNGRY")
  print("Bird: YOU LOOK LIKE FOOD")
  print("Bird: FOOD FOOD FOOD")
  print("The bird eats you.")
  die()

def press2():
  print("You press the button.\n A chocolate bunny hops out.")
  print("Bird: FOOD!!!")
  print("The marshmallow bird eats the chocolate bunny.")
  print("Bird: Thanks for the food!")
  print("Bird: I figure you want me to fly you out?")
  print("You: Yes!")
  print("You get onto the bird's back and the bird breaks out of the room and flies away.")
  victory()

start()