"""
Mitchell Hornsby
Projet 11
knightFight.py
"On my honor, I have neither given nor recieved any unacknowleged aid on this project."
This project is designed to run a program allowing the user to play a text-based dungeon game.
"""
import random

class Combatant(object):
    """The parent class for Knight, Orc, Goblin and Dragon."""

    #Constructor method for the generic Combatant class.
    def __init__(self):
        self._hitPoints = 100

    #Tells the Combatant calss and its child classes what to print.
    def __str__(self):
        return self._name + " has " + str(self._hitPoints) + " HP."

    #Returns the amount of HP a combatant has left.
    def get_hp(self):
        return self._hitPoints

    #Returns the name of a combatant.
    def get_name(self):
        return self._name

    #Checks whether a combatant hasany HP remaining.
    def still_alive(self):
        if self._hitPoints > 0:
            return True
        else:
            return False

    #Allows the combatants to damage each other.
    def take_damage(self, damageAmount):
        self._hitPoints -= damageAmount


class Knight(Combatant):
    """The player-controlled object. Attacks Orcs, Goblins, and Dragons."""

    #Knight-specific constructor method.
    def __init__(self, knightName):
        self._name = knightName
        self._hitPoints = 200

    #Allows the user to choose what action the Knight should perform.
    def attack(self):

        #Displays the user's options, then recieves input.
        print()
        print("  (1) Sword")
        print("  (2) Axe")
        print("  (3) Spear")
        print("  (4) Cower")    #(Extra credit.)
        print()
        attack = int(input("Choose an attack: "))
        print("-----------------")
        
        #Performs a sword attack.
        if attack == 1:
            print()
            print(self._name, "slashed with his sword!")
            print("Sword's attack did 25 damage.")
            return 25

        #Either performs an axe attack, or misses.    
        elif attack == 2:
            print()
            print(self._name, "swung his axe!")
            probability = random.randint(0, 100)
            if probability >= 35:
                print("Axe's attack did 45 damage.")
                return 45
            else:
                print(self._name, "missed!")
                return 0

        #Either performs a spear attack, or misses.
        elif attack == 3:
            print()
            print(self._name, "thrusted his spear!")
            probability = random.randint(1,2)
            if probability == 1:
                print("Spear's attack did 60 damage.")
                return 60
            else:
                print(self._name, "missed!")
                return 0

        #Cowers in fear of the opponent. (Extra credit.)
        elif attack == 4:
            cowers = ["threw down his weapons and begged for mercy!",\
                      "preemptively winced in pain!",\
                      "shed a single tear in concession!",\
                      "scrambled to get away, but tripped and fell!",\
                      "assumed the fetal position and rocked back and forth!"]
            print()
            print(self._name, random.choice(cowers))
            return 0

        #Disallows the user to input anything besides 1-4.
        else:
            print("That's not a valid attack!")
            return 0

            
class Orc(Combatant):
    """A possible enemy the Knight can encounter."""

    #Orc-specific constructor method.
    def __init__(self):
        self._name = "Orc"
        self._hitPoints = 100

    #Allows the Orc to perform attacks.
    def attack(self):
        probability = random.randint(0, 100)

        #The Orc attack misses.
        if probability <= 10:
            print(self._name, "missed!")
            return 0 

        #The Orc lands a sword attack.
        elif probability <= 60:
            print(self._name, "slashed its sword!")
            print("Orc's attack did 20 damage.")
            return 20

        #The Orc lands a club attack.
        elif probability <= 100:
            print(self._name, "swung its club!")
            print("Orc's attack did 5 damage.")
            return 5
    

class Goblin(Combatant):
    """A possible enemy the Knight can encounter."""

    #Goblin-specific constructor method.
    def __init__(self):
        self._name = "Goblin"
        self._hitPoints = 100

    #Allows the Goblin to perform attacks.
    def attack(self):
        probability = random.randint(0, 100)

        #The Goblin lands an axe attack.
        if probability <= 20:
            print(self._name, "swung its axe!")
            print("Goblin's attack did 25 damage.")
            return 25

        #The Goblin lands an axe attack.
        elif probability <= 60:
            print(self._name, "slammed its hammer!")
            print("Goblin's attack did 15 damage.")
            return 15

        #The Goblin's attack misses.
        elif probability <= 100:
            print(self._name, "missed!")
            return 0


class Dragon(Combatant):
    """A possible enemy the Knight can encounter."""

    #Dragon-specific constructor method. 
    def __init__(self):
        self._name = "Dragon"
        self._hitPoints = 150

    #Allows the Dragon to perform attacks.
    def attack(self):
        probability = random.randint(0, 100)

        #The Dragon lands a devastating fire attack.
        if probability <= 5:
            print(self._name, "breathed fire!")
            print("Dragon's attack did 90 damage.")
            return 90

        #The Dragon lands a slash attack.
        elif probability <= 35:
            print(self._name, "slashed its claws!")
            print("Dragon's attack did 30 damage.")
            return 30

        #The Dragon misses.
        elif probability <= 100:
            print(self._name, "missed!")
            return 0 

class Potion(Combatant):
    """Encounterable object that heals the user between 25 and 75 HP. Extra credit attempt."""

    #Potion-specific constructor method.
    def __init__(self):
        self._heal = random.randint(25, 75)

    #Returns the amount of HP that the potion will heal.
    def get_heal(self):
        return self._heal

    #Does 'negative damage', which adds HP to the Knight.
    def heal(self): 
        return -(self._heal)

    
def main():

    #Creates a new game.
    c = Combatant()

    #Allows the user to name their knight, and displays opening instructions.
    knightName = str(input("Enter your knight's name: "))
    k = Knight(knightName)
    print()
    print(k)
    print(knightName, "has three different attacks.")
    print()
    print("   (1) The sword does 25 damage, but never misses.")
    print("   (2) The axe does 45 damage, but has a 35% chance of missing.")
    print("   (3) The spear does 60 damage, but has a 50% chance of missing.")
    print("   (4) Cower in terror. Maybe they'll pity you.")
    print()

    #Launches the game.
    start = str(input("Press 'enter' to start your battle!"))
    print()
    if start == "":

        #Keeps track of defeated enemies.
        dragonCount = 0
        goblinCount = 0
        orcCount = 0

        #Confirms Knight is still alive before the next enemy encounter.
        while k.still_alive() == True:

            #Determines which enemy will appear. 
            chooseEnemy = random.randint(0, 100)
            

            #Initiates battle with a Dragon.
            if chooseEnemy <= 15 and k.still_alive() == True:

                #Displays pre-battle information.
                print("-------------Starting battle--------------")
                d = Dragon()

                #Confirms that both Dragon and Knight are alive, then launches the next volley of attacks.
                while d.still_alive() == True and k.still_alive() == True:

                    #Displays each party's HP, then launches attacks and records damage.
                    print(d)
                    print(k)
                    d.take_damage(k.attack())
                    print()
                    k.take_damage(d.attack())
                    print()
                    print('-----------------')

                #Confirms the Knight is still alive, then displays victory message and adds to monster count.
                if k.still_alive() == True:
                    print()
                    print(k.get_name(), "defeated the Dragon.")
                    dragonCount += 1
                    print()

                #Breaks the loop if the Knight dies.
                else:
                    break


            #Initiates battle with a Goblin.
            elif chooseEnemy <= 50 and k.still_alive() == True:

                #Displays pre-battle information.
                print("-------------Starting battle--------------")
                g = Goblin()

                #Confirms that both the Goblin and Knight are alive, then launches the next volley of attacks.
                while g.still_alive() == True and k.still_alive() == True :

                    #Displays each party's HP, then launches attacks and records damage.

                    print(g)
                    print(k)
                    g.take_damage(k.attack())
                    print()
                    k.take_damage(g.attack())
                    print()
                    print('-----------------')

                #Confirms the Knight is still alive, then displays victory message and adds to monster count.
                if k.still_alive() == True:
                    print()
                    print(k.get_name(), "defeated the Goblin.")
                    goblinCount +=1
                    print()

                #Breaks the loop if the Knight dies.
                else:
                    break


            #Initiates battle with an Orc.
            elif chooseEnemy <= 90 and k.still_alive() == True:

                #Displays pre-battle information.
                print("-------------Starting battle--------------")
                o = Orc()

                #Confirms that both the Orc and Knight are alive, then launches the next volley of attacks.
                while o.still_alive() == True and k.still_alive() == True :

                    #Displays each party's HP, then launches attacks and records damage.
                    print(o)
                    print(k)
                    o.take_damage(k.attack())
                    print()
                    k.take_damage(o.attack())
                    print()
                    print('-----------------')

                #Confirms the Knight is still alive, then displays victory message and adds to monster count.
                if k.still_alive() == True:
                    print()
                    print(k.get_name(), "defeated the Orc.")
                    orcCount += 1
                    print()

                #Breaks the loop if the Knight dies.
                else:
                    break

            #Encounters a potion instead of an enemy. (Extra credit)
            elif chooseEnemy <= 100 and k.still_alive() == True :

                #Creates a potion and displays it to the user.
                p = Potion()
                print("--------------Found Potion----------------")
                print()
                print(k.get_name(), "stumbled upon a potion!")
                print(k.get_name(), "healed by", p.get_heal(), "HP.")
                print()
                #Imparts "negative damage" to the Knight, healing him. 
                k.take_damage(p.heal())


            #Breaks the loop if the Knight is dead.
            else:
                break
            
        #Displays "Game over" message and end-game stats.
        if k.still_alive() == False:
            print("Game over.")
            
            print()
            print(k.get_name(), "defeated...")
            print(goblinCount, "Goblins.")
            print(orcCount, "Orcs.")
            print(dragonCount, "Dragons.")

    #Makes the user press enter to initiate the game.
    else:
        print("You must press enter!")
        
        
    
    
if __name__ == '__main__':
    main()
