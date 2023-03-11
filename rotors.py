
# ASSIGNING A CLASS TO EACH MECHANISM WITH THE ENIGMA MACHINE;

class Reflector(object):
    
    # CLASS SPECIFIC TO THE REFLECTOR

    def __init__(self, wiring):
        self.wiring = wiring    # TAKES IN THE SPECIFIC WIRING FOR WHICHEVER REFLECTOR MODEL I CHOOSE FROM THE OPTIONS AVAILABLE

    def encipher (self, key):
        shift = (ord(self.state) - ord('A'))    # If current rotor state was B, then the shift would be the ord(B) - which is 66 - minus the ord(A) - which is 65 = 1
        index = (ord(key) - ord('A'))%26    # The index value would then be later used to calculate what the ord(letter) would be. This is taken by calculating the (ord(letter) - ord(A)) % 26, simliar to how the caesar shift works.
        index = (index + shift)%26  # This would then be used in combination with the shift specified to give the index of the letter in the list selflwiring

        letter = self.wiring[index]     # This would then return the letter of the index specified within the wiring of the specified reflector.
        out = chr(ord('A')+(ord(letter) - ord('A') +26 - shift)%26)     # This would then take the ord(A)
        return out


class Rotor(object):

    # CLASS SPECIFIC TO THE ROTORS

    def __init__(self, wiring, notchs, state="A", ring="A"):
        self.wiring = wiring    # TAKES IN THE SPECIFIC WIRING FOR WHICHVER ROTOR MODEL I CHOOSE FROM THE OPTIONS AVAILABLE
        self.rwiring = ["0"] * 26   # Creating a list with 26 entries
        print(self.rwiring)
        print(self.wiring)
        for i in range(0, len(self.wiring)):    # LOOPING THROUGH THE WIRING LIST
            self.rwiring[ord(self.wiring[i]) - ord('A')]= chr(ord('A') + i)     # THIS TAKES THE ORD() OF THE ith TERM OF THE WIRING LIST, THEN SUBTRACTING THE ORD(A), AND EQUATING IT TO THE CHAR() OF THE ORD(A) + THE ith TERM
            print(self.rwiring)
        
        self.notchs = notchs
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
        return chr((ord(self.state) + 1 - ord('A')) % 26 + ord('A')) in self.notchs



ENIGMA_D_COMMERCIAL_ROTOR_I = Rotor(wiring="LPGSZMHAEOQKVXRFYBUTNICJDW",notchs="G")
ENIGMA_D_COMMERCIAL_ROTOR_II = Rotor(wiring="SLVGBTFXJQOHEWIRZYAMKPCNDU",notchs="M")
ENIGMA_D_COMMERCIAL_ROTOR_III = Rotor(wiring="CJGDPSHKTURAWZXFMYNQOBVLIE",notchs="V")
ENIGMA_D_COMMERCIAL_REFLECTOR = Reflector(wiring="IMETCGFRAYSQBZXWLHKDVUPOJN")

ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notchs="Y")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", notchs="M")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", notchs="D")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", notchs="R")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", notchs="H")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_A = Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_B = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_C = Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL")

SONDER_ENGIMA_ROTOR_I = Rotor(wiring="VEOSIRZUJDQCKGWYPNXAFLTHMB",notchs="Y")
SONDER_ENGIMA_ROTOR_II = Rotor(wiring="UEMOATQLSHPKCYFWJZBGVXINDR",notchs="M")
SONDER_ENGIMA_ROTOR_III = Rotor(wiring="TZHXMBSIPNURJFDKEQVCWGLAOY",notchs="D")
SONDER_ENGIMA_REFLECTOR = Reflector(wiring="CIAGSNDRBYTPZFULVHEKOQXWJM")

NORWAY_ENIGMA_ROTOR_I = Rotor(wiring="WTOKASUYVRBXJHQCPZEFMDINLG", notchs="Y")
NORWAY_ENIGMA_ROTOR_II = Rotor(wiring="GJLPUBSWEMCTQVHXAOFZDRKYNI", notchs="M")
NORWAY_ENIGMA_ROTOR_III = Rotor(wiring="JWFMHNBPUSDYTIXVZGRQLAOEKC", notchs="D")
NORWAY_ENIGMA_ROTOR_IV = Rotor(wiring="FGZJMVXEPBWSHQTLIUDYKCNRAO", notchs="R")
NORWAY_ENIGMA_ROTOR_V = Rotor(wiring="HEJXQOTZBVFDASCILWPGYNMURK", notchs="N")
NORWAY_ENIGMA_REFLECTOR = Reflector(wiring="MOWJYPUXNDSRAIBFVLKZGQCHET")




















