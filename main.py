class mainProgram():

    def __init__(self, plugboard = {" " : " "}, rotor_1 = None, rotor_2 = None, rotor_3 = None):
        alphabet_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        if rotor_1 != None and rotor_2 != None and rotor_3 != None and plugboard != None:
            if type(plugboard) != dict:
                self.plugboard = {" " : " "}
            self.rotor_1 = rotor_1
            self.rotor_2 = rotor_2
            self.rotor_3 = rotor_3
        else:
            if type(plugboard) != dict:
                self.plugboard = {" ": " "}
            self.rotor_1 = 0
            self.rotor_2 = 0
            self.rotor_3 = 0


if __name__ == "__main__":
    method = input("Enter whether you want to encrypt or decrypt: ")
    if method.lower() == "encrypt":
        rotor_settings = input("Do you want to specify the enigma settings yourself (Y) or use default settings (N): ")
        if rotor_settings.lower() == "Y":
            plugboard = input("Enter the plugboard settings: ")
            rotor_1 = int(input("Enter the value of rotor 1: "))
            rotor_2 = int(input("Enter the value of rotor 2: "))
            rotor_3 = int(input("Enter the value of rotor 3: "))
            mainProgram(plugboard, rotor_1, rotor_2, rotor_3)
        elif rotor_settings.lower() == "N":
            mainProgram()
    elif method.lower() == "decrypt":
        plugboard = input("Enter the plugboard settings: ")
        rotor_1 = int(input("Enter the value of rotor 1: "))
        rotor_2 = int(input("Enter the value of rotor 2: "))
        rotor_3 = int(input("Enter the value of rotor 3: "))
        mainProgram(plugboard, rotor_1, rotor_2, rotor_3)


    