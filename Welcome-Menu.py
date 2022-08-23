# Author: Parsa Ahmadnezhad
# Description:
#    A high-resolution VR game aiming to educate players
#    about how different planets behave and how to survive living in them,
#    while providing a fun and interesting experience for the player.

print("\n" + "Welcome to the Galaxy Survivors!" + "\n")

print("Main Menu:")
print("    1. New Game")
print("    2. Load Game (Empty)")
print("    3. Settings")
print("    4. Credit")
print("    5. Exit Menu" + "\n")

while True:
    choice = int(input("Please enter the number of your selection from main manu: "))
    if choice == 1:
        print("Level 1:")
        print("    Location: Earth")
        print("    Survivor’s Age: 21")
        print("    Era: 20th century")
        print("    Transportation: Rockets" + "\n")
    elif choice == 2:
        print("No Saved Game Data!" + "\n")
    elif choice == 3:
        print("Full settings will be available with the premium version." + "\n")
    elif choice == 4:
        print("Created and Desigened by: Parsa Ahmadnezhad")
        print("Tools Used: Canva, Google Slides, Visual Studio Code")
        print("Langauge: Python 3"+ "\n")
    elif choice == 5:
        print("Thank you for playing the Galaxy Survivors!")
        break
