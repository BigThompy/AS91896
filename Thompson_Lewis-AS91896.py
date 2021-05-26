
import easygui # Used for the graphical interface
import pickle # Used to save the monsters even when the program isn't running

# The template for existing monster and creating new monsters
MonsterTemplate = {"Name": 0, "Strength": 0, "Speed":0, "Stealth": 0, "Cunning": 0}

# Used for creating a monster
fieldNames = ["Name", "Strength", "Speed", "Stealth", "Cunning"]
fieldValues = []


# All monsters, user cards will be added to this also
FullCatalogue = {
                'Stoneling': {"Name": 'Stoneling', "Strength": 7, "Speed":1, "Stealth": 25, "Cunning": 15},
                'Vexscream': {"Name": 'Vexscream', "Strength": 1, "Speed":6, "Stealth": 21, "Cunning": 19},
                'Dawnmirage': {"Name": 'Dawnmirage', "Strength":5, "Speed":15, "Stealth": 18, "Cunning": 22},
                'Blazegolem': {"Name": 'Blazegolem', "Strength": 15, "Speed":20, "Stealth": 23, "Cunning":6},
                'Websnake': {"Name": 'Websnake', "Strength": 7, "Speed":15, "Stealth": 10, "Cunning": 5},
                'Moldvine': {"Name": 'Moldvine', "Strength": 21, "Speed":18, "Stealth": 14, "Cunning": 5},
                'Vortexwing': {"Name": 'Vortexwing', "Strength": 19, "Speed":13, "Stealth": 19, "Cunning": 2},
                'Rotthing': {"Name": 'Rotthing', "Strength": 16, "Speed":7, "Stealth": 4, "Cunning": 12},
                'Froststep': {"Name": 'Froststep', "Strength": 14, "Speed":14, "Stealth": 17, "Cunning": 4},
                'Wispghoul': {"Name": 'Wispghoul', "Strength": 17, "Speed":19, "Stealth": 3, "Cunning": 2}
}

# Saving the monsters to a file
def saveData():
    global FullCatalogue
    pickle.dump(FullCatalogue, open('monsters.monster', 'wb'))

# Loading the monsters
def loadData():
    global FullCatalogue
    FullCatalogue = pickle.load(open('monsters.monster', 'rb'))

# Adding new monster cards to the catalogue
def addMonster():
    while True:
        name = easygui.enterbox("Enter the name", "Adding new monster") # Getting 
        if name == None: # Is returned when the user presses cancel
            break   # Exits the loop
        else:
            FullCatalogue.update({name: MonsterTemplate.copy()})    # Everything is normal so it makes the new monster dictionary and adds the name

        strength = easygui.integerbox("Enter the strength", "Adding new monster")
        if strength == None:
            break
        elif strength > 25:
            easygui.msgbox("Value is to big! It has to be less than 25. Try again")
            continue
        else:
            FullCatalogue[name]["Strength"] = strength

        speed = easygui.integerbox("Enter the speed", "Adding new monster")
        if speed == None:
            break
        elif speed > 25:
            easygui.msgbox("Value is to big! It has to be less than 25. Try again")
            continue
        else:
            FullCatalogue[name]["Speed"] = speed
        stealth = easygui.integerbox("Enter the stealth", "Adding new monster")
        if stealth == None:
            break
        elif stealth > 25:
            easygui.msgbox("Value is to big! It has to be less than 25. Try again")
            continue
        else:
            FullCatalogue[name]["Stealth"] = stealth
        cunning = easygui.integerbox("Enter the cunning", "Adding new monster")
        if cunning == None:
            break
        elif cunning > 25:
            easygui.msgbox("Value is to big! It has to be less than 25. Try again")
            continue
        else:
            FullCatalogue[name]["Cunning"] = cunning
        saveData()
        break

# Deleting a monster from the catalogue
def deleteMonster():
    choiceList = []
    for i in FullCatalogue:
        choiceList.append(i)
    choices = easygui.multchoicebox("Select which monster to delete", "Deleting monsters", choiceList)
    if choices == None:
        return None
    else:
        for i in choices:
            FullCatalogue.pop(i)
        saveData()

# Editing a monster
def editMonster():
    choiceList = []
    for i in FullCatalogue:
        choiceList.append(i)
    monsterEdit = easygui.choicebox("Choose which monster to edit","Editing Monsters", choiceList)
    if monsterEdit == None:
        return
    else:
        for i in range(0,2):
            nameEdit = easygui.enterbox("Enter the name(Enter 0 to not change)", "Editing values")
            if nameEdit == None:
                break
            elif nameEdit == 0:
                pass
            else:
                FullCatalogue[monsterEdit]["Name"] = nameEdit
                break

            strengthEdit = easygui.integerbox("Enter the strength(Enter 0 to not change)", "Editing values")
            if strengthEdit == None:
                break
            elif strengthEdit == 0:
                pass
            elif strengthEdit > 25:
                easygui.msgbox("The value is too big! Please make sure it is less than 25!")
                continue
            else:
                FullCatalogue[monsterEdit]["Strength"] = strengthEdit
                break

            speedEdit = easygui.integerbox("Enter the speed(Enter 0 to not change)", "Editing values")
            if speedEdit == None:
                break
            elif speedEdit == 0:
                pass
            elif speedEdit > 25:
                easygui.msgbox("The value is too big! Please make sure it is less than 25!")
                continue
            else:
                FullCatalogue[monsterEdit]["Speed"] = speedEdit
                break

            stealthEdit = easygui.integerbox("Enter the stealth(Enter 0 to not change)", "Editing values")
            if stealthEdit == 0:
                pass

            elif stealthEdit > 25:
                easygui.msgbox("The value is too big! Please make sure it is less than 25!")
                continue
            else:
                FullCatalogue[monsterEdit]["Stealth"] = stealthEdit

            cunningEdit = easygui.integerbox("Enter the cunning(Enter 0 to not change)", "Editing values")
            if cunningEdit == None:
                break
            elif cunningEdit == 0:
                pass
            elif cunningEdit > 25:
                easygui.msgbox("The value is too big! Please make sure it is less than 25!")
                continue
            else:
                FullCatalogue[monsterEdit]["Cunning"] = cunningEdit
                break

        saveData()

# Outputing monster to shell
def shellOutput():
    shells = []
    for i in FullCatalogue:
        shells.append(i)
    while True:
        if len(shells) == 0:
            break
        else:
            outputMonster = easygui.choicebox("Select which monster to print to shell", "Printing monsters", shells)
            if outputMonster == None:
                break
            else:
                print("Name: " + str(FullCatalogue[outputMonster]["Name"]))
                print("Strength: " + str(FullCatalogue[outputMonster]["Strength"]))
                print("Speed: " + str(FullCatalogue[outputMonster]["Speed"]))
                print("Stealth: " + str(FullCatalogue[outputMonster]["Stealth"]))
                print("Cunnning: " + str(FullCatalogue[outputMonster]["Cunning"]))



# Main menu function
while True:
    saveData()
    loadData()
    mainChoice = easygui.buttonbox("Welcome to the Monster Card Catalogue!\n What would you like to do?", choices=("Add a new monster", "Delete a monster", "Outputting a monster stats to shell", "Edit a monster", "Quit"))
    if mainChoice == "Add a new monster":
        addMonster()
    elif mainChoice == "Delete a monster":
        deleteMonster()
    elif mainChoice == "Outputting a monster stats to shell":
        shellOutput()
    elif mainChoice == "Edit a monster":
        editMonster()
    elif mainChoice == "Quit":
        break
        saveData()