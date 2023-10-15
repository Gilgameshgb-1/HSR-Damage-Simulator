import customtkinter
import tkinter as tk
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Honkai Star Rail Damage Simulator")

width = 1920
height = 1080

root.geometry("1920x1080")

tabview = customtkinter.CTkTabview(root, width=4*450, height=height*0.9)
tabview.grid(row=0, column=0, padx=20)
tabview.add("Main DPS") 
tabview.add("Party/Buffs") 
tabview.add("Enemy") 
tabview.add("Damage simulation")

#Init frame config
frameOne = customtkinter.CTkFrame(tabview.tab("Main DPS"), width=440, height=900)
frameOne.grid(row = 0, column = 0, padx=5, pady=20)

frameTwo = customtkinter.CTkFrame(tabview.tab("Main DPS"), width=440, height=900)
frameTwo.grid(row = 0, column = 1, padx=5, pady=20)

frameThree = customtkinter.CTkFrame(tabview.tab("Main DPS"), width=440, height=900)
frameThree.grid(row = 0, column = 2, padx=5, pady=20)

frameFour = customtkinter.CTkFrame(tabview.tab("Main DPS"), width=440, height=900)
frameFour.grid(row = 0, column = 3, padx=5, pady=20)

#------------------------------------Character page implementation---------------------------------------------

#Init character name
characterName = customtkinter.CTkLabel(frameOne, width = 440, text = "Imbibitor Lunae", font=customtkinter.CTkFont(size=20, weight="bold"))
characterName.grid(row = 0, column = 0, pady = 10)

#Init character image
characterImage = customtkinter.CTkImage(dark_image=Image.open("C:/Users/HP/Desktop/HSR-Damage-Simulator/charIcons/ImbibitorLunae.png"), size=(90,90))
characterImageFrame = customtkinter.CTkLabel(frameOne,width = 440, text="", image=characterImage)
characterImageFrame.grid(row = 1, column = 0)

#Character Picker
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

charPickerOptionMenu = customtkinter.CTkOptionMenu(frameOne, values=["Imbibitor Lunae", "Himeko", "Bronya"], font=("Roboto", 14), command=optionmenu_callback)
charPickerOptionMenu.grid(row = 2, column = 0, pady = 10)

#level picker

levelLabel = customtkinter.CTkLabel(frameOne, text="Level", font=("Roboto", 20))
levelLabel.grid(row = 3, column = 0, padx = 10, pady = 5, sticky="w")

def optionmenu_callbackLevel(choice):
    print("optionmenu dropdown clicked:", choice)

levelPickerOptionMenu = customtkinter.CTkOptionMenu(frameOne, values=["10", "20", "30", "40", "50", "60", "70", "80"], font=("Roboto", 14), command=optionmenu_callback)
levelPickerOptionMenu.grid(row = 4, column = 0, padx=10, pady = 10, sticky="w")

#Stats textbox
statsTextbox = customtkinter.CTkTextbox(frameOne, width = 440, height = 360, font=("Roboto", 14))

statsTextbox.insert("0.0","Base Stats (LVL 80)\n\n" + "HP: 2300\n" + "ATK: 1227\n" + "DEF: 760\n" + "SPD: 102\n\n" + "Advanced Stats:\n\n" + "CRIT Rate: 39.5%\n" + "CRIT DMG: 153.6%\n" + "Break Effect: 22.0%\n" + "Outgoing Healing Boost: 0.0%\n" + "Max Energy: 140\n" + "Energy Regeneration Rate: 100%\n" + "Effect Hit Rate: 23.3%\n" + "Effect RES: 6.9%\n\n" + "DMG Type Boost\nImaginary DMG Boost: 71.2%")
statsTextbox.grid(row = 5, column = 0, padx = 10, pady = 10)
statsTextbox.configure(state="disabled")

#Eidelon picker
levelLabel = customtkinter.CTkLabel(frameOne, text="Eidolon", font=("Roboto", 20))
levelLabel.grid(row = 6, column = 0, padx=10, pady = 5, sticky="w")

def optionmenu_callbackLevel(choice):
    print("optionmenu dropdown clicked:", choice)

levelPickerOptionMenu = customtkinter.CTkOptionMenu(frameOne, values=["E0", "E1", "E2", "E3", "E4", "E5", "E6"], font=("Roboto", 14), command=optionmenu_callback)
levelPickerOptionMenu.grid(row = 7, column = 0, pady = (5,180), padx = 10, sticky="w")

#------------------------------------Light cone implementation---------------------------------------------

#Init LightCone name
characterName = customtkinter.CTkLabel(frameTwo, width = 440, text = "On the Fall of an Aeon", font=customtkinter.CTkFont(size=20, weight="bold"))
characterName.grid(row = 0, column = 0, pady = 10)

#Init LightCone Image
characterImage = customtkinter.CTkImage(dark_image=Image.open("C:/Users/HP/Desktop/HSR-Damage-Simulator/LCImages/OnTheFallOfAnAeon.png"), size=(348*0.9,408*0.9))
characterImageFrame = customtkinter.CTkLabel(frameTwo,width = 440, text="", image=characterImage)
characterImageFrame.grid(row = 1, column = 0)

#LightCone Picker
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

charPickerOptionMenu = customtkinter.CTkOptionMenu(frameTwo, values=["On the Fall of an Aeon", "The Seriousness of Breakfast", "Fermata"], font=("Roboto", 14), command=optionmenu_callback)
charPickerOptionMenu.grid(row = 2, column = 0, pady = 10)

#Effect description textbox
statsTextbox = customtkinter.CTkTextbox(frameTwo, width = 440, height = 120, font=("Roboto", 14))

statsTextbox.insert("0.0","Moth To Flames\n\n" + "Whenever the wearer attacks, their ATK is increased by 8%/12%/14%/16%/18% in this battle, up to 4 time(s). When the wearer inflicts Weakness Break on enemies, the wearer's DMG increases by 12%/15%/18%/21%/24% for 2 turn(s).")
statsTextbox.grid(row = 3, column = 0, padx = 10, pady = 10)
statsTextbox.configure(state="disabled")

#LightCone level picker
levelLabel = customtkinter.CTkLabel(frameTwo, text="Level", font=("Roboto", 20))
levelLabel.grid(row = 4, column = 0, padx = 10, pady = 5, sticky="w")

def optionmenu_callbackLevel(choice):
    print("optionmenu dropdown clicked:", choice)

levelPickerOptionMenu = customtkinter.CTkOptionMenu(frameTwo, values=["10", "20", "30", "40", "50", "60", "70", "80"], font=("Roboto", 14), command=optionmenu_callback)
levelPickerOptionMenu.grid(row = 5, column = 0, padx=10, pady = 10, sticky="w")

#LightCone stats textbox
statsTextbox = customtkinter.CTkTextbox(frameTwo, width = 440, height = 105, font=("Roboto", 14))

statsTextbox.insert("0.0","Base Stats (LVL 80)\n\n" + "HP: 1058\n" + "ATK: 529\n" + "DEF: 396")
statsTextbox.grid(row = 6, column = 0, padx = 10, pady = 10)
statsTextbox.configure(state="disabled")

#LightCone Eidalon picker
levelPickerOptionMenu = customtkinter.CTkOptionMenu(frameTwo, values=["E0", "E1", "E2", "E3", "E4", "E5", "E6"], font=("Roboto", 14), command=optionmenu_callback)
levelPickerOptionMenu.grid(row = 7, column = 0, pady = (5,55), padx = 10, sticky="w")

#---------------------------------------Relics implementation---------------------------------------------

#Init Relic page
characterName = customtkinter.CTkLabel(frameThree, width = 440, text = "Relics", font=customtkinter.CTkFont(size=20, weight="bold"))
characterName.grid(row = 0, column = 0, pady = 10)

#Input for Head and Hand
characterName = customtkinter.CTkLabel(frameThree, width = 440, text = "Head", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 1, column = 0)
statsTextboxHead = customtkinter.CTkTextbox(frameThree, width = 440, height = 102, font=("Roboto", 14))

statsTextboxHead.insert("0.0","HP: 705\n" + "CRITDMG%: 20\n" + "ATK: 529\n" + "DEF: 396\n" + "CRITRATE%: 20")
statsTextboxHead.grid(row = 2, column = 0, padx = 10, pady = 6)

characterName = customtkinter.CTkLabel(frameThree, width = 440, text = "Hand", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 3, column = 0)
statsTextboxHand = customtkinter.CTkTextbox(frameThree, width = 440, height = 102, font=("Roboto", 14))

statsTextboxHand.insert("0.0","HP: 705\n" + "CRITDMG%: 20\n" + "ATK: 529\n" + "DEF: 396\n" + "CRITRATE%: 20")
statsTextboxHand.grid(row = 4, column = 0, padx = 10, pady = 6)

#Input for Body and Feet
characterName = customtkinter.CTkLabel(frameThree, width = 440, text = "Body", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 5, column = 0)
statsTextboxBody = customtkinter.CTkTextbox(frameThree, width = 440, height = 102, font=("Roboto", 14))

statsTextboxBody.insert("0.0","HP: 705\n" + "CRITDMG%: 20\n" + "ATK: 529\n" + "DEF: 396\n" + "CRITRATE%: 20")
statsTextboxBody.grid(row = 6, column = 0, padx = 10, pady = 6)

characterName = customtkinter.CTkLabel(frameThree, width = 440, text = "Feet", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 7, column = 0)
statsTextboxFeet = customtkinter.CTkTextbox(frameThree, width = 440, height = 102, font=("Roboto", 14))

statsTextboxFeet.insert("0.0","HP: 705\n" + "CRITDMG%: 20\n" + "ATK: 529\n" + "DEF: 396\n" + "CRITRATE%: 20")
statsTextboxFeet.grid(row = 8, column = 0, padx = 10, pady = 6)

#Input for Planar Sphere and Link Rope
characterName = customtkinter.CTkLabel(frameThree, width = 440, text = "Planar Sphere", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 9, column = 0)
statsTextboxPlanarSphere = customtkinter.CTkTextbox(frameThree, width = 440, height = 102, font=("Roboto", 14))

statsTextboxPlanarSphere.insert("0.0","HP: 705\n" + "CRITDMG%: 20\n" + "ATK: 529\n" + "DEF: 396\n" + "CRITRATE%: 20")
statsTextboxPlanarSphere.grid(row = 10, column = 0, padx = 10, pady = 6)

characterName = customtkinter.CTkLabel(frameThree, width = 440, text = "Link Rope", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 11, column = 0)
statsTextboxLinkRope = customtkinter.CTkTextbox(frameThree, width = 440, height = 102, font=("Roboto", 14))

statsTextboxLinkRope.insert("0.0","HP: 705\n" + "CRITDMG%: 20\n" + "ATK: 529\n" + "DEF: 396\n" + "CRITRATE%: 20")
statsTextboxLinkRope.grid(row = 12, column = 0, padx = 10, pady = 6)

#---------------------------------------Skill details implementation---------------------------------------------

#Basic attack
characterName = customtkinter.CTkLabel(frameFour, width = 440, text = "Basic Attack", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 0, column = 0, pady = 2)

valueBasicSlider = 1

basicAttackTextbox = customtkinter.CTkTextbox(frameFour, width = 440, height = 280, font=("Roboto", 14)) #Init necessary

def sliderFunction(value):
    global valueBasicSlider
    valueBasicSlider = value
    #print("Current slider value:" + str(value))
    basicAttackTextbox.configure(state="normal")
    basicAttackTextbox.delete("0.0", tk.END)
    basicAttackTextbox.insert("0.0","Basic version: Uses a 2-hit attack and deals Imaginary DMG equal to " + str(40+10*valueBasicSlider) + "% of Imbibitor Lunae's ATK to a single enemy target.\n\n" + "Enhanced version (1): Uses a 3-hit attack and deals Imaginary DMG equal to " + str(104 + 26*valueBasicSlider) + "% of Imbibitor Lunae's ATK to a single enemy target.\n\n" + "Enhanced version (2): Uses a 5-hit attack and deals Imaginary DMG equal to " + str(162 + 38*valueBasicSlider) + "% of Imbibitor Lunae's ATK to a single enemy target. From the fourth hit onward, simultaneously deals Imaginary DMG equal to " + str(24 + 6*valueBasicSlider) + "% of Imbibitor Lunae's ATK to adjacent targets.\n\n" + "Enhanced version (3): Uses a 7-hit attack and deals Imaginary DMG equal to " + str(200 + 50*valueBasicSlider) + "% of Imbibitor Lunae's ATK to a single enemy target. From the fourth hit onward, simultaneously deal Imaginary DMG equal to " + str(72 + 18*valueBasicSlider) + "% of Imbibitor Lunae's ATK to adjacent targets.")
    basicAttackTextbox.configure(state="disabled")


sliderOne = customtkinter.CTkSlider(frameFour, from_=1, to=7, number_of_steps=6, command=sliderFunction)
sliderOne.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

#Basic attack description
basicAttackTextbox.grid(row = 2, column = 0, padx = 10, pady = 5)
#------------------------------------------------------------------------------------------------------------------------------------
characterName = customtkinter.CTkLabel(frameFour, width = 440, text = "Skill", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 3, column = 0)

valueSkillSlider = 1

skillTextbox = customtkinter.CTkTextbox(frameFour, width = 440, height = 160, font=("Roboto", 14)) #Init necessary

def sliderFunctionSkill(value):
    global valueSkillSlider
    valueSkillSlider = value
    skillTextbox.configure(state="normal")
    skillTextbox.delete("0.0", tk.END)
    skillTextbox.insert("0.0","Enhances Basic ATK. Enhancements may be applied up to 3 times consecutively. Using this ability does not consume Skill Points and is not considered as using a Skill. Refer to basic attack (1), (2) and (3)\n\n" + "When using Divine Spear or Fulgurant Leap, starting from the fourth hit, 1 stack of Outroar is gained before every hit. Each stack of Outroar increases Imbibitor Lunae's CRIT DMG by " + str(6 + 0.6*valueSkillSlider) +"%, for a max of 4 stacks. These stacks last until the end of his turn.")
    skillTextbox.configure(state="disabled")

sliderTwo = customtkinter.CTkSlider(frameFour, from_=1, to=12, number_of_steps=11, command=sliderFunctionSkill)
sliderTwo.grid(row=4, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

skillTextbox.grid(row = 5, column = 0, padx = 10, pady = 5)

#------------------------------------------------------------------------------------------------------------------------------------
characterName = customtkinter.CTkLabel(frameFour, width = 440, text = "Ultimate", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 6, column = 0)

valueUltimateSlider = 1

ultimateTextbox = customtkinter.CTkTextbox(frameFour, width = 440, height = 85, font=("Roboto", 14)) #Init necessary

def sliderFunctionUltimate(value):
    global valueUltimateSlider
    valueUltimateSlider = value
    ultimateTextbox.configure(state="normal")
    ultimateTextbox.delete("0.0", tk.END) #Improperly configured damage since scaling isn't linear
    ultimateTextbox.insert("0.0","Uses a 3-hit attack and deals Imaginary DMG equal to " + str(168 + 12*valueUltimateSlider) + "% of Imbibitor Lunae's ATK to a single enemy target. At the same time, deals Imaginary DMG equal to " + str(round(78.4 + 5.6*valueUltimateSlider, 1)) + "%of Imbibitor Lunae's ATK to adjacent targets.")
    ultimateTextbox.configure(state="disabled")

sliderThree = customtkinter.CTkSlider(frameFour, from_=1, to=12, number_of_steps=11, command=sliderFunctionUltimate)
sliderThree.grid(row=7, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

ultimateTextbox.grid(row = 8, column = 0, padx = 10, pady = 5)

#------------------------------------------------------------------------------------------------------------------------------------
characterName = customtkinter.CTkLabel(frameFour, width = 440, text = "Talent", font=customtkinter.CTkFont(size=14, weight="bold"))
characterName.grid(row = 9, column = 0)

valueTalentSlider = 1

talentTextbox = customtkinter.CTkTextbox(frameFour, width = 440, height = 75, font=("Roboto", 14)) #Init necessary

def sliderFunctionTalent(value):
    global valueTalentSlider
    valueTalentSlider = value
    talentTextbox.configure(state="normal")
    talentTextbox.delete("0.0", tk.END) #Improperly configured damage since scaling isn't linear
    talentTextbox.insert("0.0","After each hit dealt during an attack, Imbibitor Lunae gains 1 stack of Righteous Heart, increasing his DMG by" + str(10 + 0.5*valueTalentSlider) + "%. This effect can stack up to 6 time(s), lasting until the end of his turn.")
    talentTextbox.configure(state="disabled")

sliderFour = customtkinter.CTkSlider(frameFour, from_=1, to=12, number_of_steps=11, command=sliderFunctionTalent)
sliderFour.grid(row=10, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

talentTextbox.grid(row = 11, column = 0, padx = 10, pady = 5)

root.mainloop()