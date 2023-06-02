
# ASSIGNING A CLASS TO EACH MECHANISM WITH THE ENIGMA MACHINE;

class Reflector(object):
    
    # CLASS SPECIFIC TO THE REFLECTOR

    def __init__(self, wiring):
        self.wiring = wiring    # Takes in the specific wiring for whichever reflector model I choose from the options available

    def encipher (self, key):
        shift = (ord(self.state) - ord('A'))    # If current rotor state was B, then the shift would be the ord(B) - which is 66 - minus the ord(A) - which is 65 = 1
        index = (ord(key) - ord('A'))%26    # The index value would then be later used to calculate what the ord(letter) would be. This is taken by calculating the (ord(letter) - ord(A)) % 26
        index = (index + shift)%26  # This would then be used in combination with the shift specified to give the index of the letter in the list selflwiring

        letter = self.wiring[index]     # This would then return the letter of the index specified within the wiring of the specified reflector.
        out = chr(ord('A')+(ord(letter) - ord('A') +26 - shift)%26)     # This would then take the ord(A)
        return out


class Rotor(object):

    # CLASS SPECIFIC TO THE ROTORS

    def __init__(self, wiring, notch, state="A", ring="A"):
        self.wiring = wiring    # Takes in the specific wiring for whichever rotor model I choose from the options available
        self.rwiring = ["0"] * 26   # Creating a list with 26 entries
        for i in range(0, len(self.wiring)):    # LOOPING THROUGH THE WIRING LIST
            self.rwiring[ord(self.wiring[i]) - ord('A')]= chr(ord('A') + i)     # THIS TAKES THE ORD() OF THE ith TERM OF THE WIRING LIST, THEN SUBTRACTING THE ORD(A), AND EQUATING IT TO THE CHAR() OF THE ORD(A) + THE ith TERM
        
        self.notch = notch
        self.state = state
        self.ring = ring

    def encipher_right(self, key):
        shift = (ord(self.state) - ord(self.ring))
        index = (ord(key) - ord('A'))%26
        index = (index + shift)%26

        letter = self.wiring[index]
        out = chr(ord('A')+(ord(letter) - ord('A') +26 - shift)%26)

        return out

    def encipher_left(self, key):
        shift = (ord(self.state) - ord(self.ring))
        index = (ord(key) - ord('A'))%26
        index = (index + shift)%26

        letter = self.rwiring[index]
        out = chr(ord('A')+(ord(letter) - ord('A') + 26 - shift)%26)

        return out

    def notch_function(self, offset=1):
        self.state = chr((ord(self.state) + offset - ord('A')) % 26 + ord('A'))

    def is_in_turnover_pos(self):
        return chr((ord(self.state) + 1 - ord('A')) % 26 + ord('A')) in self.notch



ENIGMA_D_COMMERCIAL_ROTOR_I = Rotor(wiring="LPGSZMHAEOQKVXRFYBUTNICJDW",notch="G")
ENIGMA_D_COMMERCIAL_ROTOR_II = Rotor(wiring="SLVGBTFXJQOHEWIRZYAMKPCNDU",notch="M")
ENIGMA_D_COMMERCIAL_ROTOR_III = Rotor(wiring="CJGDPSHKTURAWZXFMYNQOBVLIE",notch="V")
ENIGMA_D_COMMERCIAL_REFLECTOR = Reflector(wiring="IMETCGFRAYSQBZXWLHKDVUPOJN")

ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Y")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="M")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="D")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", notch="R")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", notch="H")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_A = Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_B = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_C = Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL")

SONDER_ENGIMA_ROTOR_I = Rotor(wiring="VEOSIRZUJDQCKGWYPNXAFLTHMB",notch="Y")
SONDER_ENGIMA_ROTOR_II = Rotor(wiring="UEMOATQLSHPKCYFWJZBGVXINDR",notch="M")
SONDER_ENGIMA_ROTOR_III = Rotor(wiring="TZHXMBSIPNURJFDKEQVCWGLAOY",notch="D")
SONDER_ENGIMA_REFLECTOR = Reflector(wiring="CIAGSNDRBYTPZFULVHEKOQXWJM")

NORWAY_ENIGMA_ROTOR_I = Rotor(wiring="WTOKASUYVRBXJHQCPZEFMDINLG", notch="Y")
NORWAY_ENIGMA_ROTOR_II = Rotor(wiring="GJLPUBSWEMCTQVHXAOFZDRKYNI", notch="M")
NORWAY_ENIGMA_ROTOR_III = Rotor(wiring="JWFMHNBPUSDYTIXVZGRQLAOEKC", notch="D")
NORWAY_ENIGMA_ROTOR_IV = Rotor(wiring="FGZJMVXEPBWSHQTLIUDYKCNRAO", notch="R")
NORWAY_ENIGMA_ROTOR_V = Rotor(wiring="HEJXQOTZBVFDASCILWPGYNMURK", notch="N")
NORWAY_ENIGMA_REFLECTOR = Reflector(wiring="MOWJYPUXNDSRAIBFVLKZGQCHET")




















