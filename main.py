import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Honkai Star Rail Damage Simulator")

width = 1920
height = 1080

root.geometry("1920x1080")

tabview = customtkinter.CTkTabview(root, width=4*450, height=height*0.9)
tabview.grid(row=0, column=0, padx=50)
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
characterImage = customtkinter.CTkImage(dark_image=Image.open("C:/Users/HP/Desktop/honkaiSim/charIcons/ImbibitorLunae.png"), size=(90,90))
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


root.mainloop()