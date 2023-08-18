#### Time's Up - the fastest version of Zork you'll ever play
#### SomeThing

#### RNGesus has entered the chat
import random

#### RNGesus
RNGesus = random.randint(0, 1)

#### Beginning steps
steps = random.randint(50, 60)

#### User inventory
gun         = 0
sword       = 0
camera      = 0
binoculars  = 0

#### Start game
start = False

#### Starting Position
start_hor = random.randint(0, 4) # starting hor
start_ver = random.randint(0, 4) # starting ver

#### Escape Position
end_hor = random.randint(0, 4) # escape hor
end_ver = random.randint(0, 4) # escape hor

#### Player Positions
hor = start_hor
ver = start_ver

min_hor = 0
min_ver = 0

max_hor = 4
max_ver = 4

#### Loose Brick
lb = 0

#### User Path
move_north      = 0
move_west       = 0
move_east       = 0
move_south      = 0
look_north      = 0
look_west       = 0
look_east       = 0
look_south      = 0

#### The Intro
print()
print("<<<                                         \x1B[1mWelcome to Zork Xtreme\x1B[0m                                                    >>>")
print("<<< Welcome to Zork Xtreme, the aim of the game is to escape before you are caught. Explore the map as best you can,  >>>")
print("<<< you may find some interesting things along the way. Some will prove more useful than others.                      >>>")
print(f"<<< In this game you have a limited number of moves. You have {steps} moves to escape.                                     >>>")
print("<<< When you're ready to begin type \"start\" and press ENTER.                                                          >>>")
print("<<< If at any time you don't know what command to use, type \"help\" to print a list of available commands.             >>>")

print()

while start == False:
       menu = input("<<< Are you ready to run? ").lower()
       if menu == "start":
              start = True
              print()
              print("========")
              print("Let's Go")
              print("========")
              print()

       elif menu == "help":
              print("==============================================================================================")
              print("                                            \x1B[1mHELP")
              print("==============================================================================================")
              print()
              print("======================================== \x1B[1mHow to move:\x1B[0m ========================================")
              print("To navigate the map use the command \"move\" followed by a direction on the compass.")
              print("Example, \"move north\" will move you north one step. You may only make one step at a time.")
              print()
              print()
              print("While you explore you may come across some buildings. To enter them use the \"enter\" command.")
              print("Example: \"enter house\"")
              print("Use the \"exit\" [building] to leave them.")
              print("Example: \"exit house\"")
              print()
              print()
              print("====================================== \x1B[1mUseful Commands\x1B[0m ======================================")
              print()
              print("When you come across an item on the map, to pick it up enter \"pick up\" [item].")
              print()
              print()
              print("To inspect something use the command \"inspect\" [item].")
              print()
              print()
              print("During the game you might have some items which can come in useful.")
              print("Use the commmand \"use\" [item].")
              print()
              print()
              print("To quit the game at any time enter \"quit\"")
              print()
              print()
              print("==============================================================================================")
              print("==============================================================================================")
              print()
              print()



       else:
        print()
        print("<<< Too scared? No one blames you. Come back when you're ready.                                           >>>")
        print()
        exit()


#### User inputs

while steps != 1:
        # Map Layout
        # Row Zero (0)
       if hor == 0 and ver == 0:
               
              print()
              print("\x1B[1mTowering walls as far as the eye can see surround you to the West and South. The fog of the forest makes\nit hard to see the path from the door to the west running to the east.")
              print("\x1B[1mIn the distant North you see a light through the trees but the forest is thick and dark, you should stay\nclose to the wall.")
              print()
              print()
        
       elif hor == 1 and ver == 0:
               
              print()
              print("\x1B[1mThe fog is thinner here, you can see the path winding through the trees to the west and to the east.")
              print("\x1B[1mTo the north the forest grows thicker and looks unforgiving.")
              print()
              print()

       elif hor == 2 and ver == 0:
               
              print()
              print("\x1B[1mA stone path leads north and west, to the east the trees start to disopate and\nit looks as though there may be a clearing.")
              print("\x1B[1mIt's eerily quiet.")
              print()
              print()

       elif hor == 3 and ver == 0:
               
              print()
              print("\x1B[1mThere are fewer trees here but the fog remains thick.")
              print("\x1B[1mTo the east you make out some small organised objects but its hard to make out\nwhat they are from here.")
              print()
              print()

       elif hor == 4 and ver == 0:
              
              print()
              print("\x1B[1mYou come to a small black fence surrounding a grave yard, it's well questionably\nmaintained considering the state of everything else.")
              print("\x1B[1mWestward there stands nothing but a few lone trees. The forest is easy to see to\nthe north.")
              print()
              print()
        
        # Row One (1)
       elif hor == 0 and ver == 1 and lb == 1:
              
              print()
              print("\x1B[1mYou're surrounded by dense trees and shrubbery, you decide to hold close to the western wall so you\ndon't get lost.")
              print("\x1B[1mYou stub your toe on the brick you dropped on the floor. -1 to run away.")
              print()
              print()
               
       elif hor == 0 and ver == 1 and lb != 1:
               
              print()
              print("\x1B[1mYou're surrounded by dense trees and shrubbery, you decide to hold close to the western wall so you\ndon't get lost.")
              print("\x1B[1mAs you run your hand over the bricks to keep your way you notice one of the bricks is loose from\nthe wall.")
              print()
              print()
        
       elif hor == 1 and ver == 1:
               
              print()
              print("\x1B[1mYou manage to fumble through the shrubbery, it's  miracle you didn't cut yourself.\nThere is a small mound of overturned earth in front of you and a neatly placed rock on top.")
              print("\x1B[1mFrom here you can hardly see in any other direction.")
              print()
              print()

       elif hor == 2 and ver == 1:
               
              print()
              print("\x1B[1mTo the east you see a small wooden structure lead up to by the small path you're\nstood on. The path also heads south towards a forest.")
              print("\x1B[1mThe west looks like a hellscape of jungle. At least it looks less boring than\nthe north where there's nothing but trees as far as you can see.")
              print()
              print()

       elif hor == 3 and ver == 1:
               
              print()
              print("\x1B[1mYou come across a small shed which has fallen into disrepair, the door is just about attached to the hinges.\nA dark figure crosses the window as you hear the clatter of something heavy falling on the floor.")
              print("\x1B[1mAfter a moment things settle down again, looking around outside the shadow is nowhere to be seen,\nmaybe it's still inside...")
              print()
              print()
        
       elif hor == 4 and ver == 1:
               
              print()
              print("\x1B[1mLike the other half of the map there's nothing here but a large collection of\nboring old trees. Might be worth looking up once in a while.")
              print("\x1B[1mTo the west you can see a small shed, south there's a short fence  guarding\nsome stones. North there's... don't make me say it again.\n\n\nFine, it's trees.")
              print()
              print()
        
        # Row Two (2)
       elif hor == 0 and ver == 2:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()
        
       elif hor == 1 and ver == 2:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 2 and ver == 2:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 3 and ver == 2:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 4 and ver == 2:
               
              print()
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

        # Row Three (3)
       elif hor == 0 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 1 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 2 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 3 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 4 and ver == 3:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

        #Row Four (4)
       elif hor == 0 and ver == 4:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 1 and ver == 4:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 2 and ver == 4:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 3 and ver == 4:
               
              print()
              print("\x1B[1m")
              print("\x1B[1m")
              print()
              print()

       elif hor == 4 and ver == 4:
               
              print()
              print("\x1B[1mThere's a clearning in the forrest and the wall here is broken through but climing it looks deadly\nbased on the steep drop.")
              print("\x1B[1mYou make out a faint object in the distance, if only you had something to get a better look.")
              print()
              print()

       # Buildings
       # Rusty Shed at 3, 1
       elif hor == 10 and ver == 10:

              print()
              print("\x1B[1mYou pull the door on the shed open, the creak of the hinges makes your spine buckle.\nYou're unable to walk, you lose.")
              print()
              print("\x1B[1mJust kidding. There's a work bench with some orange-looking tools and a broken chair.\nIn the corner there is a cabinet with a gun stood in it.\nWhatever you saw moving in the window isn't here either.")
              print()
              print()



       print("What would you like to do? ")
       user_input = input("> ").lower().strip()

        # Boarder Control
       if user_input == "move north" and ver >= 10 or user_input == "move south" and ver >= 10:
              print()
              print("You're inside.")
              print("Horizontal: ", hor, "Vertical: ", ver)
              print()

       elif user_input == "move west" and hor >= 10 or user_input == "move east" and hor >= 10:
              print()
              print("You're inside.")
              print("Horizontal: ", hor, "Vertical: ", ver)
              print()

       elif user_input == "move north" and ver == max_ver or user_input == "move south" and ver == min_ver:
              print()
              print("A giant wall stands in your way.")
              print("Horizontal: ", hor, "Vertical: ", ver)
              print()

       elif user_input == "move west" and hor == min_hor or user_input == "move east" and hor == max_hor:
              print()
              print("A giant wall stands in your way.")
              print("Horizontal: ", hor, "Vertical: ", ver)
              print()

        # Movement
       elif user_input == "move north":
              ver += 1
              steps -= 1
              print(hor, ", ", ver)
       elif user_input == "move west":
              hor -= 1
              steps -= 1
              print(hor, ", ", ver)
       elif user_input == "move east":
              hor += 1
              steps -= 1
              print(hor, ", ", ver)
       elif user_input == "move south":
              ver -= 1
              steps -= 1
              print(hor, ", ", ver)

       # Moving in / out of Buildings
       # Shed at 3, 1
       elif user_input == "enter shed" and hor == 3 and ver == 1:
              hor = 10
              ver = 10

       elif user_input == "exit shed" and hor == 10 and ver == 10:
              hor = 3
              ver = 1

        # Inspect
        # Brick
       elif user_input == "inspect brick" and hor == 0 and ver == 1:
              lb += 1
              print("==============================")
              print("\x1B[1mDon't look back.")
              print("\x1B[1mIt will only catch you faster.")
              print("==============================")
              print()
       elif user_input == "inspect brick":
              print("What brick?")
       


       # Pick up Items
       # Gun
       elif user_input == "pick up gun" and gun == 1:
              print()
              print("===========================================================================")
              print("\x1B[1mYou already have a gun and we don't trust you to have two.")
              print("\x1B[1mShouldn't you be trying to get out of here?.")
              print("===========================================================================")
              print()

       elif user_input == "pick up gun" and hor == 10 and ver == 10:
              gun += 1
              print()
              print("===========================================================================")
              print("\x1B[1mYou put the gun in your belt.")
              print("\x1B[1mDon't shoot yourself.")
              print("===========================================================================")
              print()

       # Sword
       elif user_input == "pick up sword" and sword == 1:
              print()
              print("===========================================================================")
              print("\x1B[1mYou cannot carry two swords.")
              print("\x1B[1mDon't fall on it.")
              print("===========================================================================")
              print()

       elif user_input == "pick up sword":
              sword += 1
              print()
              print("===========================================================================")
              print("\x1B[1mYou put the sword over your shoulder.")
              print("\x1B[1mJust because you have a sword now doesn't make you a swashbuckler.")
              print("===========================================================================")
              print()

       # Camera
       elif user_input == "pick up camera" and camera == 1:
              print()
              print("===========================================================================")
              print("\x1B[1mCameras are out of stock.")
              print("\x1B[1mBloody tourists.")
              print("===========================================================================")
              print()

       elif user_input == "pick up camera":
              camera += 1
              print()
              print("===========================================================================")
              print("\x1B[1mYou put the camera strap around your neck.")
              print("\x1B[1mBloody tourists.")
              print("===========================================================================")
              print()

       # Binoculars
       elif user_input == "pick up binoculars" and binoculars == 1:
              print()
              print("===========================================================================")
              print("\x1B[1mYou already have the binoculars.")
              print("\x1B[1mYou know you only have one set of eyes right?")
              print("===========================================================================")
              print()

       elif user_input == "pick up binoculars":
              binoculars += 1
              print()
              print("===========================================================================")
              print("\x1B[1mYou put the binoculars into your sack.")
              print("\x1B[1mGood thing there aren't any windows 'round here.")
              print("===========================================================================")
              print()

       # Use Item
       # Binoculars
       elif user_input == "use binoculars" and hor == 4 and ver == 4:

              print()
              print("\x1B[1mYou see an old decrepit tower of a once great castle in the distance. Maybe that explains the walls...")
              for n in range(0, 25):
                     print()
              print("\x1B[1mSUDDENLY THROUGH THE ARROW SLITS OF THE TOWER YOU MAKE EYE CONTACT WITH IT.")
              print()
              print()

       elif user_input == "use binoculars":
              print()
              print("You look through the binoculars and see nothing due to the thick fog.")
              print()
              print()

        # Help Menu
       elif user_input == "help":
              print("==============================================================================================")
              print("                                            \x1B[1mHELP")
              print("==============================================================================================")
              print()
              print("======================================== \x1B[1mHow to move:\x1B[0m ========================================")
              print("To navigate the map use the command \"move\" followed by a direction on the compass.")
              print("Example, \"move north\" will move you north one step. You may only make one step at a time.")
              print()
              print()
              print("While you explore you may come across some buildings. To enter them use the \"enter\" command.")
              print("Example: \"enter house\"")
              print("Use the \"exit\" [building] to leave them.")
              print("Example: \"exit house\"")
              print()
              print()
              print("====================================== \x1B[1mUseful Commands\x1B[0m ======================================")
              print()
              print("When you come across an item on the map, to pick it up enter \"pick up\" [item].")
              print()
              print()
              print("To inspect something use the command \"inspect\" [item].")
              print()
              print()
              print("During the game you might have some items which can come in useful.")
              print("Use the commmand \"use\" [item].")
              print()
              print()
              print("To quit the game at any time enter \"quit\"")
              print()
              print()
              print("==============================================================================================")
              print("==============================================================================================")
              print()
              print()

       # Quit game
       elif user_input == "quit":
              print()
              print("==============================")
              print("That's the cowards way out.")
              print("==============================")
              print()
              exit()
       
       # Uknown Inputs
       else:
              print()
              print("Uknown Command, see \"HELP\" for valid inputs.")
              print()



    
    #### PLACEHOLDER for later inspects

    # Binoculars
#elif user_input == "use binoculars" and binoculars == 1 and hor == 5 and ver == 5:
#        print("There's an old decrepit tower of a once great castle in the distance. Maybe that explains the walls...")
#        for n in range(25):
#            print()
#        print("SUDDENLY THROUGH THE ARROW SLITS OF THE TOWER YOU MAKE EYE CONTACT WITH IT.\n")
#elif user_input == "use binoculars" and binoculars == 0:
#        print()
#        print("You are not carrying any binoculars")
#        print()
#else:
#        print("You look through the binoculars and see nothing, the fog is too thick.")
        
    



#### VALUE CHECK ####
print(f"Guns         : {gun}")
print(f"Sword        : {sword}")
print(f"Camera       : {camera}")
print(f"Binoculars   : {binoculars}")
print()
print(f"Moves: {move_north}")
print(f"Moves: {move_east}")
print(f"Moves: {move_west}")
print(f"Moves: {move_south}")
print()


#if user_input == "use gun" and gun == 1 and RNGesus == 1:
#print("<<< You come to a clearing in the middle of the misty woods. You see a faint light in the distance.")