
import easygui # Used for the graphical interface
import pickle  # Used to save the monsters even when the program isn't running

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


# Adding new monster cards to the catalogue
def addMonster():
    fieldValues = easygui.multenterbox("Enter all the values", "Adding new monster",fieldNames)
    FullCatalogue.update({fieldValues[0]: MonsterTemplate.copy()})
    FullCatalogue[fieldValues[0]["Strength"]] = fieldValues[1]
    FullCatalogue[fieldValues[0]["Speed"]] = fieldValues[2]
    FullCatalogue[fieldValues[0]["Stealth"]] = fieldValues[3]
    FullCatalogue[fieldValues[0]["Cunning"]] = fieldValues[4]




# Deleting a monster from the catalogue
def deleteMonster():
    choiceList = []
    for i in FullCatalogue:
        choiceList.append(i)
    choices = easygui.multchoicebox("Select which monster to delete", "Deleting monsters", choiceList)
    for i in choices:
        FullCatalogue.pop(i)


def editMonster():
    choiceList = []
    for i in FullCatalogue:
        choiceList.append(i)
    monsterEdit = easygui.choicebox("Choose which monster to edit","Editing Monsters", choiceList)
    for i in range(0,2):
        nameEdit = easygui.integerbox("Enter the name(Enter 0 to not change)", "Editing values")
        if nameEdit == 0:
            strengthEdit = easygui.integerbox("Enter the strength(Enter 0 to not change)", "Editing values")
            if strengthEdit == 0:
                speedEdit = easygui.integerbox("Enter the speed(Enter 0 to not change)", "Editing values")
                if speedEdit == 0:
                    stealthEdit = easygui.integerbox("Enter the stealth(Enter 0 to not change)", "Editing values")
                    if stealthEdit == 0:
                        cunningEdit = easygui.integerbox("Enter the cunning(Enter 0 to not change)", "Editing values")
                        if cunningEdit == 0:
                            break
                        else:
                            monsterEdit["Cunning"] = cunningEdit
                    else:
                        monsterEdit["Stealth"] = stealthEdit
                else:
                    monsterEdit["Speed"] = speedEdit
            else:
                monsterEdit["Strength"] = strengthEdit
        else:
            monsterEdit["Name"] = nameEdit


# Outputing monster to shell
def shellOutput():
    for i in FullCatalogue:
        shells =[]
        shells.append(i)

    outputMonster = easygui.multchoicebox("Select which monster to print to shell", "Printing monsters", shells)
    print(outputMonster)



# Main menu function
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
    exit

