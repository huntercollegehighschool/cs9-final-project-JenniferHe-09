"""
Names: Jennifer He and Charlotte Li
Name of Project: Dumb Ways to Die Adventure Story (Hunter Vers.)
"""

"""
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'
#'\033[1m' '\033[0m' --> bold/unbold :D
#os.system('clear') --> clear console
I think replacing the # before the m with 0 ends it

print(color("string")) to print string in color color
Color library: https://www.webucator.com/article/python-color-constants-module/
for colors :)))
"""

import random 
import time
import os
from colors import red
from colors import blue
from colors import green
from colors import cyan
from colors import magenta
from colors import yellow

def dead():
  time.sleep(1)
  os.system('clear')
  print(red('\033[3m' + "Congrats you died, please use your brain and make better decisions this time around!\n"))
  start()

def choiceS():
  print(green("You keep walking..."))
  time.sleep(1)
  print(cyan("It is suspiciously quiet as you continue to walk through this crumbling building.\n\nDesperate, you wish for a way to escape this cursed situation, even if it means certain death."))
  time.sleep(1)
  print(blue("..."))
  time.sleep(1)
  print(red("A loose ceiling tile falls on your head, along with a cloud of asbestos.\n\nEverything fades into darkness..."))
  time.sleep(5)
  dead()

def choiceR():
  print("These doors are heavier than you expected...")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print(magenta("Before you can look into the dark gymnasium, a sudden gust of wind hits you in the face, and you are knocked onto the ground.\n\nIt takes you a few seconds to recover.\n\nThe doors seem a lot heavier as they slam on your fingers..."))
  time.sleep(4)
  dead()

def choiceN():
  print("You open the door to find darkness.")
  time.sleep(1)
  print(yellow("It takes a few seconds for your eyes to adjust. You fumble for a light switch, until you remember that your phone has a flashlight..."))
  time.sleep(1)
  print(red("Are those...\033[1mBODIES?\033[0m"))
  time.sleep(5)
  dead()

def choiceM():
  print("You continue to trudge through the hallways.")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("You find a divide in the hallway.\n\nOne part leads to a set of purple double doors, and the other leads into darkness.\n\nDo you decide to keep exploring, or go through the doors?\n")
  while(True):
    choice11 = input(blue("Enter R to open them, or S to keep going: "))
    if choice11 == "R" or choice11 == "r":
      choiceR() 
      break 
    elif choice11 == "S" or choice11 == "s":
      choiceS()
      break
    else:
      print("That is not an option.")

def choiceJ():
  print("You remembered that emergency exits are usually near staircases, and hurry down several flights.")
  time.sleep(1)
  num = random.randint(1,3)
  if num == 1:
    print("Your hand brushes against the flaking banisters, and you get a splinter.")
    time.sleep(0.5)
    print("You keep going...")
    time.sleep(0.5)
    print(green("What kind of painful wood is this? I feel... dizz-"))
    time.sleep(3)
    dead()
  elif num == 2:
    print(red("You keep running, and turn around, expecting another set of winding stairs. You crash into a mess of old bikes and yoga mats."))
    time.sleep(3)
    dead()
  else:
    print("You keep going, and ram into a set of doors, expecting them to lead outside. Instead, you are flung into the basement. If there were no windows before...")
    time.sleep(0.5)
    print("When your eyes adjust, you see a trophy case, next to yet another long hallway and a closet door. Do you keep exploring, or look into the closet?\n")
    while(True):
      choice9 = input(blue("Enter M to continue looking, or N to open the door: "))
      if choice9 == "M" or choice9 == "m":
        choiceM()
        break
      elif choice9 == "N" or choice9 == "n":
        choiceN()
        break
      else:
        print("That is not a option.")

def choiceI():
  print("You enter the double doors and find yourself in a huge auditorium. You notice a student sleeping in each of the numerous seats. Feeling extremely relieved to find more people around you, your adrenaline levels decrease, giving way to a wave of tiredness. You notice an empty seat. Perhaps if you take a short nap, you'll wake up to find that this was all a dream. Would you like to rest or wake up a student to ask for directions?\n")
  while(True):
    choice8 = input(blue("Enter P to sleep, or Q to ask for directions: "))
    if choice8 == "P" or choice8 == "p":
      print(red("You settle down to take a quick nap. \033[4mHa, what an idiot!\033[0m Hasn't anyone taught you to stay awake during moments of danger? You feel something sharp cut your neck before you black out."))
      time.sleep(5)
      dead()
    if choice8 == "Q" or choice8 == "q":
      num = random.randint(1,2)
      if num == 1:
        print(red("You walk up to a student near you, falling asleep with the darkest eyebags you've ever seen. Lightly tapping them on the shoulder, you open your mouth to ask for help. Before you can do so, they open their eyes and glare at you: \n'\033[3m' + HEY. Do you have any idea how hard it is to get some sleep at this school?? Go away! + '\033[0m' \nThey close their eyes and begin snoring again, but not before flinging and arm out in annoyance, sending you tumbling roughly down the nearby stairs. What...")) 
        time.sleep(20)
        dead()
      if num == 2:
        print("You walk up to a student near you, falling asleep still holding their schoolwork. Lightly tapping them on the shoulder, you ask for help. Sending you a quick glare, they point up and tell you to go to the roof. Before you can thank them, they fall asleep again. How weird... but you set off to the roof regardless. \n\nYou arrive at the roof and find a ladder, seemingly going down, outside of this horrid prison. Would you like to bend over to get a better look at where the ladder really leads or just climb away?\n")
        choice10 = input(blue("Enter T to get a better look, or U to start climbing out of this place: "))
        if choice10 == "T" or choice10 == "t":
          print(cyan("You lean over to get a better look, yet suddenly you feel a heavy weight on your back (is this what the students have to suffer through everyday here? -- you recall their huge backpacks...) and you fall right off the edge of the roof. Oh. You were so close."))
          time.sleep(15)
          dead()
        if choice10 == "U" or choice10 == "u":
          print("You climb down the ladder, landing safely outside the building. Congrats! You've escaped. After you run as far as you can from here, it's time to find the nearest police station!\n")
          time.sleep(3)
          print("Or so you thought...\n")
          time.sleep(1)
          print(cyan("You suddenly feel an immense burst of pain and collapse on the ground. Oh... I see now. It was simply impossible to make it out of that building alive. As you feel the disappointment of all your effort going to waste, your last thought is, 'the poor students... how they've suffered.\n'"))
          print(cyan("And this, ends the tale of the cursed brick prison. A place of eternal suffering that slowly kills off its own students.\n\n"))
          print(blue("\033[1mEND.\033[0m"))
        else:
          print("That is not an option.")
        
def choiceK():
  print ("You grab a random lunchbox and open it to find a sandwich. Well ok... it can sustain you for a while. \n\nYou then look over at the school lunch. The meat was raw, thank god you didn't eat it... Grabbing a few more extra safe-looking meals, you set off to find a way out again. \n\nYou walk up a few flights of stairs to come across two black doors, next to another staircase. Do you go through the double doors, or keep looking for an exit near the staircases?\n")
  while(True): 
    choice7 = input(blue("Enter I to go through the double doors, or J to look for an escape: "))
    if choice7 == "I" or choice7 == "i":
      choiceI()
      break
    elif choice7 == "J" or choice7 == "j":
      choiceJ()
      break
    else:
      print("That is not an option.")

def choiceH():
  print("You back away slowly and turn back towards a set of green doors. You rush out into what looks like a hallway. You come across two black doors, next to another staircase. Do you go through the double doors, or keep looking for an exit near the staircases?\n")
  while(True):
    choice6 = input(blue("Enter I to go through the double doors, or J to look for an escape: "))
    if choice6 == "I" or choice6 == "i":
      choiceI()
      break
    elif choice6 == "J" or choice6 == "j":
      choiceJ()
      break
    else:
      print("That is not an option.")

def choiceG():
  print("You reach towards the closet, and turn the knob.")
  time.sleep(0.5)
  print(red("..."))
  time.sleep(0.5)
  print(green("You are absorbed into a pit of inky darkness."))
  time.sleep(1)
  print(red("Several unindentified objects scratch you.\n\n When you realize that this was a bad idea, the door slams shut behind you.\n\nIn frustration, you kick what feels like a cardboard box."))
  time.sleep(1)
  print(green("It turns out that all it took was a little nudge to cause the entire mountain of old electronics and hopefully-not-bodies to fall on your head..."))
  time.sleep(5)
  dead()

def choiceF():
  print("You wait...")
  time.sleep(1)
  print("You keep waiting...")
  time.sleep(1)
  print("The sounds continue, but nothing happens.\n")
  while(True): 
    choice5 = input(blue("Enter G to open the closet, or H to escape: "))
    if choice5 == "G" or choice5 == "g":
      choiceG()
      break
    elif choice5 == "H" or choice5 == "h":
      choiceH()
      break
    else:
      print("That is not an option.")

def choiceE():
  print("You hurry up the stairs...")
  time.sleep(0.5)
  print(yellow("and trip over a pencil.\n\nYou roll down several flights. Why does life keep doing this to you?"))
  time.sleep(5)
  dead()

def choiceC():
  print("You choose to keep exploring. \nYou come across the cafeteria, that has a few school lunches and student lunch boxes scattered around. Would you like to eat the school lunch or home lunch?\n")
  while(True):
    choice4 = input(blue("Enter K for school lunch, or L for home lunch: "))
    if choice4 == "K" or choice4 == "k":
      choiceK()
      break
    if choice4 == "L" or choice4 == "l":
      print(green("Oh. The meat wasn't cooked, no wonder all the students here are gone or dead..."))
      time.sleep(5)
      dead()
    else:		
      print("That is not an option.")

def choiceB():
  print("You come across one of many questionable-looking hallways.\nAt the end, you can see what appears to be a staircase.\nYou hear some unidentified thumping sounds from a nearby closet.\nDo you made a run for it down a set of nearby stairs, or stay?\n")
  while(True):
    choice3 = input(blue("Enter E to run, or F to stay: "))
    if choice3 == "E" or choice3 == "e":
      choiceE()
      break
    elif choice3 == "F" or choice3 == "f":
      choiceF()
      break
    else:
      print("That is not an option.")

def choiceA():
  print("You look outside through a window on the second floor that took a few hours to find. There's no one in sight, but the window looks low enough to jump out of. Would you like to keep exploring within the building or make an escape through the window?\n\n")
  while(True):
    choice2 = input(blue("Enter C to keep exploring, or D to make an escape: "))
    if choice2 == "C" or choice2 == "c":
      choiceC()
      break
    elif choice2 == "D" or choice2 == "d":
      print(yellow("Ouch, that was a bit too much higher than what you expected."))
      time.sleep(5)
      dead()
      break
    else:
      print("That is not an option.")

def start():
  print(blue('\033[1m' + "Dumb Ways to Die -- Brick Prison (Hunter) Version!" + '\033[0m'))
  print("You wake up in an empty school building that looks like a brick prison, what would you like to do?\n")
  while(True):
    choice1 = input(blue("Enter A to look outside, or B to walk through the building: "))
    if choice1 == "A" or choice1 == "a":
      choiceA()
      break
    elif choice1 == "B" or choice1 == "b":
      choiceB()
      break
    else:
      print("That is not an option.")
      os.system('clear')

start()