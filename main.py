from optparse import Option
from tkinter import *
from tkinter import messagebox
from tkinter import font
import enigma as ee
import rotors as ro
import os
from configparser import ConfigParser
import random



class HelpWindow(Toplevel):
    global file_path_of_image

    def __init__(self, parent):

        def Table(total_rows, total_columns, row_jump, column_jump):
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(self, width=4, font=fontStyle)
                    self.e.grid(row=i + row_jump, column=j + column_jump, sticky=W)
                    self.e.insert(END, lst[i][j])

        super().__init__(parent)

        # CODE FOR QUICKLY CHANGING FONTS

        fontfamilylist = list(font.families())
        fontindex = 2
        fontStyle = font.Font(family=fontfamilylist[fontindex])

        self.title("Support")
        self.geometry("850x700")

        self.introduction1 = Label(self,
                                   text="QUICK INTRODUCTION: An engima cipher is a type of encryption method called polyalphabetic substitution.\n"
                                        "The reason why the enigma cipher is more secure is because it uses the combination of plugboards, ",
                                   font=fontStyle).grid(row=0, column=0, sticky=W, columnspan=26)

        self.paragraph = Label(self, text="we", font=fontStyle).grid(row=1, column=0, sticky=W)
            

class MainProgram(Tk):

# CHECKS IF config.ini HAS BEEN PRODUCED OR NOT.

    global opened_before
    config = ConfigParser()

    try:
        with open("config.ini", 'r') as f:  # if files does exist
            opened_before = True
    except IOError:  # if file doesnt exist
        opened_before = False
        config.read('config.ini')
        config.add_section('main')
        config.set('main', 'resolution', '700x375')
        with open('config.ini', 'w') as f:
            config.write(f)

    def __init__(self):

        super().__init__()


        # CODE FOR QUICKLY CHANGING FONTS


        fontfamilylist = list(font.families())
        fontindex = 2
        fontStyle = font.Font(family=fontfamilylist[fontindex])


        # ALLOWS THE METHOD THAT IS CLICKED IN THE MENU TO BE ASSIGNED TO A VARIABLE WHICH IN THIS CASE IS method_clicked


        methods = [
            "Encryption",
            "Decryption"
        ]

        self.method_clicked = StringVar()
        self.method_clicked.set(methods[0])


        # ALLOWS THE METHOD THAT IS CLICKED IN THE MENU TO BE ASSIGNED TO A VARIABLE WHICH IN THIS CASE IS rotor_positions_clicked


        rotor_positions = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" 
        ]

        self.previous_rotor_position_1 = StringVar()
        self.previous_rotor_position_1.set("-")

        self.previous_rotor_position_2 = StringVar()
        self.previous_rotor_position_2.set("-")

        self.previous_rotor_position_3 = StringVar()
        self.previous_rotor_position_3.set("-")


        self.rotor_position_clicked_1 = StringVar()
        self.rotor_position_clicked_1.set(rotor_positions[0])

        self.rotor_position_clicked_2 = StringVar()
        self.rotor_position_clicked_2.set(rotor_positions[0])

        self.rotor_position_clicked_3 = StringVar()
        self.rotor_position_clicked_3.set(rotor_positions[0])

        self.current_rotor_pos = ["-", "-", "-"]


        # ALLOWS THE ROTORS AND RELFECTOR THAT IS CHOSEN TO BE ASSIGNED TO A VARIABLE


        enigma_variation_options = ["Enigma D", "Enigma I", "Sonder Enigma"]

        self.variation_clicked = StringVar()
        self.variation_clicked.set("-")

        self.rotor_models_engima_d_commerical = ["Enigma D Rotor I", "Enigma D Rotor II", "Enigma D Rotor III"]
        self.rotor_models_enigma_i_wehrmacht = ["Enigma I Rotor I", "Enigma I Rotor II", "Enigma I Rotor III", "Enigma I Rotor IV", "Enigma I Rotor V"]
        self.rotor_model_sonder_engima = ["Sonder Enigma Rotor I", "Sonder Enigma Rotor II", "Sonder Enigma Rotor III"]

        self.model_rotor_1_clicked = StringVar()
        self.model_rotor_1_clicked.set("-")

        self.model_rotor_2_clicked = StringVar()
        self.model_rotor_2_clicked.set("-")

        self.model_rotor_3_clicked = StringVar()
        self.model_rotor_3_clicked.set("-")
        
        self.reflecter_models = ["Enigma D Reflector", "Enigma I Reflector A", "Enigma I Reflector B", "Enigma I Reflector C", "Sonder Enigma Reflector"]

        self.model_reflector_clicked = StringVar()
        self.model_reflector_clicked.set("-")


        # ALLOWS THE VALUES FOR THE PLUGBOARD THAT IS CLICKED IN THE MENU TO BE ASSIGNED TO A VARIABLE


        plugboard_settings_choices = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" 
        ]


        for i in range (1, 27):
            exec(f"self.plugboard_settings_option_{str(i)} = StringVar()")

        for i in range(1,27):
            exec("self.plugboard_settings_option_" + str(i) + '.set("-")' )


        # CONFIGURING ROOT WINDOW


        self.title("Enigma Machine")
        self.geometry("1300x850")


        self.welcomeLabel = Label(self, text="Enigma-Eldaw Machine", font=(fontfamilylist[2], 20)).grid(row=0,column=0, sticky=W)

        self.methodChosenLabel = Label(self, text="Method: ", font=(fontfamilylist[2], 15)).grid(row=1, column=0, pady=30, sticky=W)
        self.methodChosenValue = OptionMenu(self, self.method_clicked, *methods).grid(row=1, column=0, padx=70, sticky=W)


        # ENCRYPTION INPUT 


        self.encryptionInputLabel = Label(self, text="PLAIN TEXT: ", font=(fontfamilylist[2], 15)).grid(row=2, column=0, sticky=W)
        self.encryptionInputEntry = Entry(self, width=75, borderwidth=5)
        self.encryptionInputEntry.grid(row = 2, column = 0, padx=120, sticky=W)


        # ROTOR VALUES

        self.previousRotor1Label = Label(self, text="Previous Rotor 1 Value:", font=(fontfamilylist[2], 15)).grid(row=3, column=0, sticky=W)
        self.previousRotor1Value = OptionMenu(self, self.previous_rotor_position_1, *rotor_positions).grid(row=3, column=0, padx=235, sticky=W)

        self.previousRotor2Label = Label(self, text="Previous Rotor 2 Value:", font=(fontfamilylist[2], 15)).grid(row=4, column=0, sticky=W)
        self.previousRotor2Value = OptionMenu(self, self.previous_rotor_position_2, *rotor_positions).grid(row=4, column=0, padx=235, sticky=W)

        self.preivousRotor3Label = Label(self, text="Previous Rotor 3 Value:", font=(fontfamilylist[2], 15)).grid(row=5, column=0, sticky=W)
        self.previousRotor3Value = OptionMenu(self, self.previous_rotor_position_3, *rotor_positions).grid(row=5, column=0, padx=235, sticky=W)


        self.rotorLabel1 = Label(self, text="Rotor 1 Value: ", font=(fontfamilylist[2], 15)).grid(row=3, column=0, padx=300, pady=25, sticky=W)
        self.rotor1ChosenValue = OptionMenu(self, self.rotor_position_clicked_1, *rotor_positions).grid(row=3, column=0, padx=450, sticky=W)

        self.rotorLabel2 = Label(self, text="Rotor 2 Value:", font=(fontfamilylist[2], 15)).grid(row=4, column=0, padx=300, pady=25, sticky=W)
        self.rotor2ChosenValue = OptionMenu(self, self.rotor_position_clicked_2, *rotor_positions).grid(row=4, column=0, padx=450, sticky=W)

        self.rotorLabel3 = Label(self, text="Rotor 3 Value: ", font=(fontfamilylist[2], 15)).grid(row=5, column=0, padx=300, pady=25, sticky=W)
        self.rotor3ChosenValue = OptionMenu(self, self.rotor_position_clicked_3, *rotor_positions).grid(row=5, column=0, padx=450, sticky=W)

        self.resetRotorValues = Button(self, text="Reset", font=(fontfamilylist[2], 15)).grid(row=3, column=0, padx=500)

        

        # PLUGBOARD SETTINGS


        self.plugboardsettingsLabel = Label(self, text="Plugboard Settings: ", font=(fontfamilylist[2], 15)).grid(row=3, column=0, padx=600, sticky=W)

        self.plugboardsettingsOption1 = OptionMenu(self, self.plugboard_settings_option_1, *plugboard_settings_choices).grid(row=3, column=0, padx=800, sticky=W)
        self.plugboardsettingsOption2 = OptionMenu(self, self.plugboard_settings_option_2, *plugboard_settings_choices).grid(row=3, column=0, padx=850, sticky=W)

        self.plugboardsettingsOption3 = OptionMenu(self, self.plugboard_settings_option_3, *plugboard_settings_choices).grid(row=3, column=0, padx=925, sticky=W)
        self.plugboardsettingsOption4 = OptionMenu(self, self.plugboard_settings_option_4, *plugboard_settings_choices).grid(row=3, column=0, padx=975, sticky=W)

        self.plugboardsettingsOption5 = OptionMenu(self, self.plugboard_settings_option_5, *plugboard_settings_choices).grid(row=3, column=0, padx=1050, sticky=W)
        self.plugboardsettingsOption6 = OptionMenu(self, self.plugboard_settings_option_6, *plugboard_settings_choices).grid(row=3, column=0, padx=1100, sticky=W)

        self.plugboardsettingsOption7 = OptionMenu(self, self.plugboard_settings_option_7, *plugboard_settings_choices).grid(row=3, column=0, padx=1175, sticky=W)
        self.plugboardsettingsOption8 = OptionMenu(self, self.plugboard_settings_option_8, *plugboard_settings_choices).grid(row=3, column=0, padx=1225, sticky=W)

        self.plugboardsettingsOption9 = OptionMenu(self, self.plugboard_settings_option_9, *plugboard_settings_choices).grid(row=4, column=0, padx=800, sticky=W)
        self.plugboardsettingsOption10 = OptionMenu(self, self.plugboard_settings_option_10, *plugboard_settings_choices).grid(row=4, column=0, padx=850, sticky=W)

        self.plugboardsettingsOption11 = OptionMenu(self, self.plugboard_settings_option_11, *plugboard_settings_choices).grid(row=4, column=0, padx=925, sticky=W)
        self.plugboardsettingsOption12 = OptionMenu(self, self.plugboard_settings_option_12, *plugboard_settings_choices).grid(row=4, column=0, padx=975, sticky=W)

        self.plugboardsettingsOption13 = OptionMenu(self, self.plugboard_settings_option_13, *plugboard_settings_choices).grid(row=4, column=0, padx=1050, sticky=W)
        self.plugboardsettingsOption14 = OptionMenu(self, self.plugboard_settings_option_14, *plugboard_settings_choices).grid(row=4, column=0, padx=1100, sticky=W)

        self.plugboardsettingsOption15 = OptionMenu(self, self.plugboard_settings_option_15, *plugboard_settings_choices).grid(row=4, column=0, padx=1175, sticky=W)
        self.plugboardsettingsOption16 = OptionMenu(self, self.plugboard_settings_option_16, *plugboard_settings_choices).grid(row=4, column=0, padx=1225, sticky=W)

        self.plugboardsettingsOption17 = OptionMenu(self, self.plugboard_settings_option_17, *plugboard_settings_choices).grid(row=5, column=0, padx=800, sticky=W)
        self.plugboardsettingsOption18 = OptionMenu(self, self.plugboard_settings_option_18, *plugboard_settings_choices).grid(row=5, column=0, padx=850, sticky=W)

        self.plugboardsettingsOption19 = OptionMenu(self, self.plugboard_settings_option_19, *plugboard_settings_choices).grid(row=5, column=0, padx=925, sticky=W)
        self.plugboardsettingsOption20 = OptionMenu(self, self.plugboard_settings_option_20, *plugboard_settings_choices).grid(row=5, column=0, padx=975, sticky=W)

        self.plugboardsettingsOption21 = OptionMenu(self, self.plugboard_settings_option_21, *plugboard_settings_choices).grid(row=5, column=0, padx=1050, sticky=W)
        self.plugboardsettingsOption22 = OptionMenu(self, self.plugboard_settings_option_22, *plugboard_settings_choices).grid(row=5, column=0, padx=1100, sticky=W)

        self.plugboardsettingsOption23 = OptionMenu(self, self.plugboard_settings_option_23, *plugboard_settings_choices).grid(row=5, column=0, padx=1175, sticky=W)
        self.plugboardsettingsOption24 = OptionMenu(self, self.plugboard_settings_option_24, *plugboard_settings_choices).grid(row=5, column=0, padx=1225, sticky=W)

        self.plugboardsettingsOption25 = OptionMenu(self, self.plugboard_settings_option_25, *plugboard_settings_choices).grid(row=6, column=0, padx=987.5, sticky=W)
        self.plugboardsettingsOption26 = OptionMenu(self, self.plugboard_settings_option_26, *plugboard_settings_choices).grid(row=6, column=0, padx=1037.5, sticky=W)


        # FUNCTION FOR RANDOMISING AND RESETTING PLUGBOARD SETTINGS

        self.randomiseButton = Button(self, text="Randomise", font=(fontfamilylist[2], 10), command=self.randomisePlugboard).grid(row=2, column=0, padx=800, sticky=W)
        self.resetButton = Button(self, text="Reset", font=(fontfamilylist[2], 10), command=self.resetPlugboard).grid(row=2, column=0, padx=900, sticky=W)


        # CHOOSING ROTORS AND REFLECTORS

        self.model_main = Label(self, text="Choose which variation of the enigma machine you want: ", font=(fontfamilylist[2], 15)).grid(row=7, column=0, pady=25, sticky=W)
        self.modelMainValue = OptionMenu(self, self.variation_clicked, *enigma_variation_options).grid(row=7, column=0, padx=540, sticky=W)

        self.confirmationButton = Button(self, text="Confirm", font=(fontfamilylist[2], 10), command=self.confirmOption).grid(row=7, column=0, padx=670, sticky=W)

        
        self.model_rotor_1 = Label(self, text="Choose the model of your first rotor: ", font=(fontfamilylist[2], 15)).grid(row=8,column=0, pady=25, sticky=W)
        


        self.model_rotor_2 = Label(self, text="Choose the model of your second rotor: ", font=(fontfamilylist[2], 15)).grid(row=9,column=0, pady=25, sticky=W)
        


        self.model_rotor_3 = Label(self, text="Choose the model of your third rotor: ", font=(fontfamilylist[2], 15)).grid(row=10,column=0, pady=25, sticky=W)

        
        self.model_reflector = Label(self, text="Choose the model of your reflector: ", font=(fontfamilylist[2], 15)).grid(row=11,column=0, pady=25, sticky=W)
        self.modelReflectorValue = OptionMenu(self, self.model_reflector_clicked, *self.reflecter_models).grid(row=11, column=0, padx=400, sticky=W)


        # ENCRYPTOIN OUTPUT

        self.encryptionOutputLabel = Label(self, text="CIPHER TEXT:", font=(fontfamilylist[2], 15)).grid(row=12, column=0, sticky=W)
        self.encryptionOutputEntry = Entry(self, width=75, borderwidth=5)
        self.encryptionOutputEntry.grid(row=12, column = 0, sticky=W, padx=125)
        self.encryptButton = Button(self, text="Encrypt", font=(fontfamilylist[2], 10), command=self.encryptClick).grid(row=12, column=0, padx=590, sticky=W)


        # HELP BUTTON

        self.helpButton = Button(self, text="CLICK ME FOR HELP", font=(fontfamilylist[2], 10), command=self.open_support_window).grid(row=14, column=30, pady=20, sticky=E)
    
        

        # ASKS USER IF THEY NEED HELP WITH THE PROGRAM IF THIS IS THEIR FIRST TIME BOOTING UP THE PROGRAM

        if opened_before is False:
            answer = messagebox.askyesno("Welcome to the Enigma-Eldaw program! ",
                                         "If you know what you are doing, press NO to exit this box and never see this dialog box again. "
                                         "If you are new to this and need help explaining what it is, press YES to get support. \n\n"
                                         "DO YOU NEED HELP WITH THIS PROGRAM?")
            if answer is True:
                self.open_support_window()

    def randomisePlugboard(self):
        list_of_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for i in range(1, 27):
            letter = random.choice(list_of_letters)
            list_of_letters.remove(letter)
            exec("self.plugboard_settings_option_" + str(i) + '.set("' + str(letter) + '")')
            

    def resetPlugboard(self):
        for i in range(1,27):
            exec("self.plugboard_settings_option_" + str(i) + '.set("-")' )

    def open_support_window(self):
        supportWindow = HelpWindow(self)
        supportWindow.grab_set()

    def confirmOption(self):
        enigma_variant_chosen = self.variation_clicked.get()

        if enigma_variant_chosen == "Enigma D":
            self.modelRotor1Value = OptionMenu(self, self.model_rotor_1_clicked, *self.rotor_models_engima_d_commerical).grid(row=8, column=0, padx=400, sticky=W)
            self.modelRotor2Value = OptionMenu(self, self.model_rotor_2_clicked, *self.rotor_models_engima_d_commerical).grid(row=9, column=0, padx=400, sticky=W)
            self.modelRotor3Value = OptionMenu(self, self.model_rotor_3_clicked, *self.rotor_models_engima_d_commerical).grid(row=10, column=0, padx=400, sticky=W)

        elif enigma_variant_chosen == "Enigma I":
            self.modelRotor1Value = OptionMenu(self, self.model_rotor_1_clicked, *self.rotor_models_enigma_i_wehrmacht).grid(row=8, column=0, padx=400, sticky=W)
            self.modelRotor2Value = OptionMenu(self, self.model_rotor_2_clicked, *self.rotor_models_enigma_i_wehrmacht).grid(row=9, column=0, padx=400, sticky=W)
            self.modelRotor3Value = OptionMenu(self, self.model_rotor_3_clicked, *self.rotor_models_enigma_i_wehrmacht).grid(row=10, column=0, padx=400, sticky=W)

        elif enigma_variant_chosen == "Sonder Enigma":
            self.modelRotor1Value = OptionMenu(self, self.model_rotor_1_clicked, *self.rotor_model_sonder_engima).grid(row=8, column=0, padx=400, sticky=W)
            self.modelRotor2Value = OptionMenu(self, self.model_rotor_2_clicked, *self.rotor_model_sonder_engima).grid(row=9, column=0, padx=400, sticky=W)
            self.modelRotor3Value = OptionMenu(self, self.model_rotor_3_clicked, *self.rotor_model_sonder_engima).grid(row=10, column=0, padx=400, sticky=W)

        

    def encryptClick(self):



        
        
        reflector_values_dict = {"-" : 0,
                                "Enigma D Reflector" : ro.ENIGMA_D_COMMERCIAL_REFLECTOR, 
                                 "Enigma I Reflector A" : ro.ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_A, 
                                 "Enigma I Reflector B": ro.ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_B,
                                 "Enigma I Reflector C" : ro.ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_C,
                                 "Sonder Enigma Reflector" : ro.SONDER_ENGIMA_REFLECTOR}

        rotor_values_dict = {"-" : 0,
                             "Enigma D Rotor I" : ro.ENIGMA_D_COMMERCIAL_ROTOR_I,
                             "Enigma D Rotor II" : ro.ENIGMA_D_COMMERCIAL_ROTOR_II,
                             "Enigma D Rotor III" : ro.ENIGMA_D_COMMERCIAL_ROTOR_III,
                             "Enigma I Rotor I" : ro.ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_I,
                             "Enigma I Rotor II" : ro.ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_II,
                             "Enigma I Rotor III" : ro.ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_III,
                             "Enigma I Rotor IV" : ro.ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_IV,
                             "Enigma I Rotor V" : ro.ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_V,
                             "Sonder Enigma Rotor I" : ro.SONDER_ENGIMA_ROTOR_I,
                             "Sonder Enigma Rotor II" : ro.SONDER_ENGIMA_ROTOR_II,
                             "Sonder Enigma Rotor III" : ro.SONDER_ENGIMA_ROTOR_III}

        reflector_model = self.model_reflector_clicked.get()
        reflector_model = reflector_values_dict[reflector_model]

        rotor_1_model = self.model_rotor_1_clicked.get()
        rotor_1_model = rotor_values_dict[rotor_1_model]

        rotor_2_model = self.model_rotor_2_clicked.get()
        rotor_2_model = rotor_values_dict[rotor_2_model]

        rotor_3_model = self.model_rotor_3_clicked.get()
        rotor_3_model = rotor_values_dict[rotor_3_model]


        initialRotorValues = (f"{self.rotor_position_clicked_1.get()}{self.rotor_position_clicked_2.get()}{self.rotor_position_clicked_3.get()}")
        plugboardSettings = f"{self.plugboard_settings_option_1.get()}{self.plugboard_settings_option_2.get()} {self.plugboard_settings_option_3.get()}{self.plugboard_settings_option_4.get()} {self.plugboard_settings_option_5.get()}{self.plugboard_settings_option_6.get()} {self.plugboard_settings_option_7.get()}{self.plugboard_settings_option_8.get()} {self.plugboard_settings_option_9.get()}{self.plugboard_settings_option_10.get()} {self.plugboard_settings_option_11.get()}{self.plugboard_settings_option_12.get()} {self.plugboard_settings_option_13.get()}{self.plugboard_settings_option_14.get()} {self.plugboard_settings_option_15.get()}{self.plugboard_settings_option_16.get()} {self.plugboard_settings_option_17.get()}{self.plugboard_settings_option_18.get()} {self.plugboard_settings_option_19.get()}{self.plugboard_settings_option_20.get()} {self.plugboard_settings_option_21.get()}{self.plugboard_settings_option_22.get()} {self.plugboard_settings_option_23.get()}{self.plugboard_settings_option_24.get()}"
        self.encryptionOutputEntry.delete(0, END)
        encryption_enigma_machine = ee.Enigma(reflector = reflector_model, rotor1 = rotor_1_model, rotor2 = rotor_2_model, rotor3 = rotor_3_model, initial_pos = initialRotorValues, plugboard = plugboardSettings)
        self.encryptionOutputEntry.insert(END, encryption_enigma_machine.encipher(plaintext_in=self.encryptionInputEntry.get()))


        self.previous_rotor_position_1.set(self.current_rotor_pos[0])
        self.previous_rotor_position_2.set(self.current_rotor_pos[1])
        self.previous_rotor_position_3.set(self.current_rotor_pos[2])
        
        self.current_rotor_pos = encryption_enigma_machine.returnRotorPositions()

        self.rotor_position_clicked_1.set(self.current_rotor_pos[0])
        self.rotor_position_clicked_2.set(self.current_rotor_pos[1])
        self.rotor_position_clicked_3.set(self.current_rotor_pos[2])


    


if __name__ == "__main__":
    mainProgram = MainProgram()
    mainProgram.mainloop()

