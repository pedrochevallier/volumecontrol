from __future__ import print_function
import customtkinter
from volume import setVolume
import yaml
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

processes = []


sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    out = str(session.Process).lower()
    out = out.split("'")
    try:
        out = out[1]
        processes.append(out)
    except:
        IndexError
        pass
    

print(processes)
with open('preferences.yaml', 'r') as file:
    preferences = yaml.safe_load(file)


option1 = preferences['preferences']['option_1']
option2 = preferences['preferences']['option_2']
option3 = preferences['preferences']['option_3']


def set_option(value):
    print("option 1 changed to " + value)
    global option1
    option1 = value

def send_volume(value):
    print("changing volume of " + option1 + " to " + str(value))
    setVolume.setVolume(value, option1)

def root():
    root = customtkinter.CTk()
    root.geometry("500x500")

    root.grid_columnconfigure((0,1,2,3), weight=1)
    root.grid_rowconfigure((1), weight=1)


    optionmenu_1 = customtkinter.CTkOptionMenu(master=root, values=["master", "chrome", "discord"], command=set_option)
    optionmenu_1.grid(row=0,column=0)

   # slider1 = customtkinter.CTkSlider(master=root, from_=0, to=1, command=send_volume, orientation="vertical")
   # slider1.grid(row=1,column=0)


    optionmenu_2 = customtkinter.CTkOptionMenu(master=root, values=["master", "chrome", "discord"], command=set_option)
    optionmenu_2.grid(row=0,column=1)

   # slider2 = customtkinter.CTkSlider(master=root, from_=0, to=1, command=send_volume, orientation="vertical")
   # slider2.grid(row=1,column=1)

    optionmenu_3 = customtkinter.CTkOptionMenu(master=root, values=["master", "chrome", "discord"], command=set_option)
    optionmenu_3.grid(row=0, column=2)

   # slider3 = customtkinter.CTkSlider(master=root, from_=0, to=1, command=send_volume, orientation="vertical")
   # slider3.grid(row=1, column=2)


    root.mainloop()